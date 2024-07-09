from socket import MsgFlag
import paramiko
import time

import gc
import os
from ncclient import manager, xml_
from ncclient.operations.rpc import RPCError
# from getpass import getpass
import logging
import re
import xml.etree.ElementTree as ET
from lxml import etree, objectify
import pandas as pd
from datetime import datetime
import string
import random
import traceback
import pandas as pd
try:
    from pygnmi.client import gNMIclient,telemetryParser
except:
    #print("Warning:  Please run pip install protobuf==3.20.* (See install doc)")
    pass
import json
# from RestLibs.PLGD.PLGDRestLib import PLGDRestLib
import requests
# from requests.packages.urllib3.exceptions import InsecureRequestWarning  #CPIXI
from requests.auth import HTTPBasicAuth
try:
    import xmltodict
except:
    print("Warning: xmltodict library not installed. GX Netconf API will not function properly. Please run pixi_full_update.bat if you would like to use the PIXI GX Netconf API.")
from xml.dom.minidom import parseString
import sys
from cliCodec.libs import plogger
from collections import defaultdict
from cliCodec.testsets.ont import ONT
import yaml 

from cliCodec.libs import pixi

gLoadedTestList = "No_xlsxTestList_Loaded"
_abortOnFail = False

_stashData = {}
gSetupData = dict()

global locals_dict, testCache, suite_name, _TEST_title_2
testCache = {}
locals_dict = {}
suite_name = ""
_excelsheet = "no-sheet"
currentsheetrow = "no-row"
_currentSheetRow = "no-row"
_TEST_title_2 = "no-test-title"

def step(title, result, details = ""):
   # import ipdb; ipdb.set_trace()
   pQueue = pixi.PIXIQueue()
   pQueue.put({
      "command": "step",
      "data": {
         "title": title,
         "result": result,
         "details": details
      }
   })

def stashData(action,name,value=""):
   # import ipdb; ipdb.set_trace()
   """
      --------------------

         action get,set,clear
         
         name the name of the stash
         
         variable - the variable name -> value to stash
         
         save name
         
         use name all to clear all saved data (happens at beginning of each test)

      --------------------  
   """
   global _stashData

   if action == "set":
      try:
         _stashData[name] = value
      except:
         print("value into rex.stashData does not exist")
         return(False)
      return(True)
   elif action == "get":
      try:
         return _stashData[name]
      except:
         return None
   elif action == "clear":
      if name == "all":
         try:
            _stashData.clear()
         except:
            noop = 1
      else:
         try:
            _stashData.pop(name)
         except:
            noop = 1
   else:
      print("Invalid acton",action,"passed to rex.stashData")
      return(False)
   return(False)

def comparePairs(stash,*args):
   # import ipdb; ipdb.set_trace()
   """
      -------------
         
         stash - notStash ( used in module based programming)
         
         string-stash-name ( used in sheet based programming and works in module based programming too)

         The pairs are actual-1,expected-1,actual-2,expected-2, ....

         "notStash" case:
    
            a variable length list of pairs to compare, variables or values: a,b,c,"dog",d[1],"cat"
    
            Example: 
            
            rex.comparePairs("notStash"a,b,c,"dog",d[1],"cat")
            
            or
            
            ret = g40cli.sendRcv('cli1', 'show inventory', step=True)  
            
            rsltDict = g40cli.retDataToTables(ret)  
            
            rex.comparePairs("notStash",rsltDict['inventory-1-PEM-3']['actual-subtype'],'DC',rsltDict['inventory-1-PE
            
         "stashName" case:
            
            a variable length list of pairs to compare, where all expected refer elements in a single named stash.
            
            Designed to be used with stashed dictionary (or list) indexed data as returned from *cli.retDataToTables and sheets.
            
            Example: rex.comparePairs("Tables1","[card1][adminState]","unlocked","[card1][cardType]","XMM")
 
         Note, stashed indexes must be strings and not, for example integers.

      ----------------------


   """

   # using a stash
   
   if stash != "notStash":
      varName = stashData("get",stash)
      varr = eval("varName")
      # will append to list elements.
      # index of data
      
   count = 1
   for arg in args:
      # if odd, this is actual
      if count%2 == 1:
         actual1 = arg
         if stash != "notStash":
            # in this case ( stash data, actual is an index)
            try:
               actual = eval("varr"+actual1)
            #    log("Index -"+actual1+"-")
               print("Index -"+actual1+"-")
               
            except Exception as msg:
               print("******** Exception begin ***********")
               print(msg)
               print("********  Exception end   **********")
               print("variable value",varName)
               actual = "stashRetrieveError:stash="+stash+".  "+"index="+actual+"."
      # if even, this is expected
      else:
         expected = arg
         # after even, compare.
         compareStep(actual1,expected)
      count = count + 1
      
def compareStep(a,b,stash=False):
   # import ipdb; ipdb.set_trace()
   """
      -------------

         a is the actual data, either a variable or a stash string name.
         
         If using a string-stash-name, then set stash=True
         
         b is the expected data, a variable name or a value.

      --------------
 
   """

   if stash == True:
     innerA = stashData("get",a)
     # use a going forward
     a = innerA
   
   if a == b:
      step("Compare","passed","verified -"+str(a)+"-")
   else:
      step("Compare","failed","-"+str(a)+"- not equal to -"+str(b)+"-")

def debugPrint(setGet,str=""):
#
#
# 
# 
   global _fullDebugPrintSet
   if setGet == "get":
      return _fullDebugPrintSet
   elif  setGet == "set":
      _fullDebugPrintSet = True
      return _fullDebugPrintSet
   elif  setGet == "clear":
      _fullDebugPrintSet = False
      return _fullDebugPrintSet
   elif  setGet == "print":
      if debugPrint("get"):
         print(str)
   else:
      #print("Invalid setGet",setGet,"passed to rex.debugPrint")
      # need standard for fail - difft type?
      return 0