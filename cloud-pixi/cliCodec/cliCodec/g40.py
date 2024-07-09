# import vsh
# import rex
import re
import os
import time
import webbrowser
import paramiko
import threading
import ipdb

from cliCodec.vsh import create_handle, conns, sim, _sim, disconnect as dis, create_handle as cre_han

from cliCodec.rex import stashData, debugPrint as dp, step


def connectNE(handle, ip, user, pw, **args):
   
   """
    **Example**
   
    ::

       g40cli.connNEretry("cli1","172.17.1.80","secadmin","Infinera@1",retry=600)
        
       optional arg, step=False(default)|True(report a pixie/rex step)
         
       optional: port 2222 (sims for example)
         
       prompt ( and changable, sticky)
         
       optional: retry=600, retry for 600 seconds.
       default is 0, no retry.
    
    :param handle: Connection handle
    :type handle: string
    :param ip: NE IP address
    :type ip: string
    :param user: NE username
    :type user: string
    :param pw: NE password
    :type pw: string
    :return: True -> Pass, False -> Fail
    :rtype: boolean
    """   
   # import ipdb; ipdb.set_trace()
#    try:
#     #    disconnect(handle)
#    except:
#        noop = 1
   retry = args.get("retry", 0)
   retry = int(retry)
    
   if retry == 0:
       try:
          rslt = _connNE_internal(handle, ip, user, pw, **args)
       except Exception as e:
          print("Exception raised while trying to connect: ", e)
          rslt = False
       if rslt is False:
           try:
               disconnect(handle)
           except:
               noop = 1
       else:
           return rslt
   else:
       retry = int(retry)
       t1 = time.time()
       t2 = t1 + retry
       while(time.time() < t2):
          try:
             rslt = _connNE_internal(handle, ip, user, pw, **args)
          except Exception as e:
             print("Exception raised while trying to connect: ", e)
             rslt = False
          if rslt is False:
             try:
                disconnect(handle)
             except:
                noop = 1
          else:
             return True
          print("Waiting 5 seconds before retrying connect...")
          time.sleep(5)
       print("Connect with retry timed-out")
       return False
           
def _connNE_internal(handle, ip, user, pw, **args):
    """
    **Example**

    ::

       g40cli.connectNE("cli1","172.17.1.80","secadmin","Infinera@1")
       
       optional arg, step=False(default)|True(report a pixie/rex step)
       optional: port, prompt ( and changable, sticky)
        

    :param handle: Connection handle
    :type handle: string
    :param ip: NE IP address
    :type ip: string
    :param user: NE username
    :type user: string
    :param pw: NE password
    :type pw: string
    :return: True -> Connected, False -> Connection Failed
    :rtype: Boolean
    """    
    result = {}
    #gCLI1 = rexui.App.conn1Frame()
    step = args.get("step", False)
    print(step)
    port = args.get("port", "22")
    print(port)
    print(handle, ip, user, pw)
    if create_handle(handle) is not None:
        if conns[handle].connect(ip, port, user, pw) == 1:
         rslt = conns[handle].sendRcv("\n")
         result["\n"]= rslt
         rslt = conns[handle].sendRcv("show software-load\n")
         result["show software-load"] = rslt
         rslt = conns[handle].sendRcv("show inventory\n")
         result["show inventory"] = rslt
         rslt = conns[handle].sendRcv("show controller-card redundancy-status\n")
         result["show controller-card redundancy-status"] = rslt
         rslt = conns[handle].sendRcv("\n")
         result["\n"] = rslt
         
         if rslt != 0:
            print(result)

            # Printing the result
            return result
         else:
               # if step:
               #    step("g40cli.connect " + handle,"failed","did not see prompt on connection")
               # else:
               #    print("Connect failed, did not see prompt for handle:", handle)
               return False
        else:
            # if step:
            #    step("g40cli.connect " + handle,"failed","connect failed")
            # else:
            #    print("Connect failed for handle:", handle)
            return False

def sendRcv(handle, cmd, **kwargs):
   #  import ipdb; ipdb.set_trace()
    """

    A method to send command to NE (CLI /SSH) and verify the prompt is returned.
    The output from the command is returned as a string.

    :param handle: handle string used with connect
    :type handle: 
    :param cmd: the command string to send on the cli, a \\n will be appended to this string. ( if this is not always desired, we will add an option to skip)
    :type cmd: 
    :return: None -> Fail, Actual result - Passed
    :rtype: String

   **Example**

    ::
     
         g40cli.sendRcv('cli1','show xcon')

    :Optional parameters:
         
      None
   """    

    # verify handle exists !!!

    # pass along certain kwargs !!!
    timeout = kwargs.get("timeout", 20)
    timeout = int(timeout)
    confirmI = kwargs.get("confirm", False)
    step = kwargs.get("step", False)
    match = kwargs.get("match", None)
    poll = kwargs.get("poll", False)
    stash = kwargs.get("stash", None)
    mode = kwargs.get("mode", "ssh")
    
    sendOnly=kwargs.get("sendOnly", False)
    rcvOnly=kwargs.get("rcvOnly", False)
    
    terminator = "\r" if mode == "telnet" else "\n"
    
   #  conns[handle] = cre_han(handle)
   #  print(f"conns handle will be ::::::::::::::: {conns[handle]}")
    # if normal send rcv ( btw should be in vsh layer)
    # rcv only first, need timeout to be fast.
   #  print(f"First recieve onl comming here : {rcvOnly}")
   #  print(f"before rcvOnly : {conns[handle]}")
    if rcvOnly is False:
        conns[handle].sendRcv("not sending this", rcvOnly=True,timeout=0)
    
    if confirmI:
        cmdWn = cmd+terminator
        rslt1 = conns[handle].sendRcv(cmdWn, sendOnly=True,**kwargs)
        # should verify the y before continuing!!!
        rslt = conns[handle].sendRcv('y'+terminator)
        return rslt
    else:
        tnow = time.time()
        tmax = tnow + int(timeout)
        cmdWn = cmd+terminator
        rslt = conns[handle].sendRcv(cmdWn,**kwargs)
        print("result -",rslt,"-")
        if match != None:
            matchRslt = re.search(match,rslt,re.DOTALL)
            if matchRslt is None:
                if poll is False:
                   if step:
                     #   step("g40cli.sendRcv " + handle + " " + cmd,"failed","verify did not match result")
                     print("Match not found")
                   if stash is not None:
                     #  stashData("set",stash,None)
                     print("Set Data")
                   return None
                else:
                   #kwargs = { "a":"b" , "timeout":100 }
                   newL = kwargs.items()
                   kwargs = {}
                   for a,v in newL:
                      if a != "timeout":
                         kwargs[a] = v
                      else:
                         # timeout / command hard coded to 30 sec / iteration for now
                         kwargs[a] = 30
                   while tnow < tmax:
                      #print("tnow tmax",tnow," ",tmax)
                      #print("Poll wait 5 sec - ",end='')
                     #  cont = sleep(5,newline=False)
                      cont = time.sleep(5)
                      if cont is False:
                         # 
                         if step:
                           #  step("g40cli.sendRcv " + handle + " " + cmd,"aborted","")
                           print("request aborted")
                         return None
                      rslt = conns[handle].sendRcv(cmdWn,**kwargs)
                      matchRslt = re.search(match,rslt,re.DOTALL)
                      if matchRslt is None:
                         # keep trying
                         noop = 1
                         ret = None
                      else:
                         ret = matchRslt.group()
                         if step:
                           #  step("g40cli.sendRcv " + handle + " " + cmd,"passed","verify matched result")
                           print("Verify match result")
                         return ret
                      if sim("get"):
                         if step:
                           #  step("g40cli.sendRcv " + handle + " " + cmd,"passed","sim verify matched result")
                           print("Sim verify Match result")
                         return "sim str"   
                      tnow = time.time()
                  #  log("")
                   if step:
                     #  step("g40cli.sendRcv " + handle + " " + cmd,"failed","verify matched result")
                     print("Verify Match Result")
                   return ret
                   # if got here, failed:
                   if step:
                     #  step("g40cli.sendRcv " + handle + " " + cmd,"failed","verify did not match result")
                     print("Verify didnt match")
                   return None
            else:
               # check none
               ret = matchRslt.group()
               if step:
                  #  step("g40cli.sendRcv " + handle + " " + cmd,"passed","verify matched result")
                  print("verify matched result")
               if stash is not None:
                  # stashData("set",stash,ret)
                  print("stash data")
               return ret
        else:
            if step:
               if rslt is '0':
                  # step("g40cli.sendRcv " + handle + " " + cmd,"failed","prompt not returned")
                  print("prompt not returned")
               else:
                  # step("g40cli.sendRcv " + handle + " " + cmd,"passed","prompt returned")
                  print("prompt returned")
            if stash is not None:
               # stashData("set",stash,rslt)
               print("stash result")
            return rslt


def debugPrint(print,text):
#
#
#
   try:
      dp(print,text)
   except:
      # load rex to use debugPrint
      noop = 1


def disconnect(handle,step=False):
   
   """     
   disconnect("<handle name>"): Method to close a session by its handle name. The handles are created by create_handle function 

   **Example**
                  
      ::    

          disconnect('cli1')  # closes a session with handle name 'cli1'
            
          disconnect('netconf1')  # closes a session with handle name 'netconf1'
            
          disconnect('all')  # closes ALL sessions which are active

   :param handle: session handle name - This is the session handle created by **create_handle()** method
   :type handle: string
   :param step: _description_, defaults to False
   :type step: bool, optional
   """   
   rslt = dis(handle)
   # if step:
   #      #step("Disconnect: "+handle,"passed")   #CPIXIS
   
   return rslt

def retDataToTables(rslt,fromStash=False,toStash=False,printCompares=True):
   # import ipdb; ipdb.set_trace()

   """
    Works with tables with headers for now will process multiple tables returned

    **Example**

    ::

       ret = g40cli.sendRcv('cli1', 'show inventory', step=True)  
            
       rsltDict = g40cli.retDataToTables(ret)  
            
       comparePairs("notStash",rsltDict['3']['inventory-1-PEM-3']['actual-subtype'],'DC',rsltDict['3']['inventory-1-PEM-3']['fw-status'],'not-applicable')
            
       printCompares (optional):
            
       rsltDict = g40cli.retDataToTables(ret, printCompares='rsltDict')
            
       print compareTablePairs statements that will result in verification of the given data via rex

    :param rslt: Data as retrieved from sendRcv show command
    :type rslt: string
    :param fromStash: Pull from stash data, defaults to False
    :type fromStash: bool, optional
    :param toStash: Store to stash data, defaults to False
    :type toStash: bool, optional
    :param printCompares: Variable name of data for printing compare calls that can be pasted into a user sheet, defaults to True
    :type printCompares: bool, optional
    :return: Dictionary with parsed table data
    :rtype: dict
   """   

   if fromStash:
      rslt = stashData("get",rslt)
   
   myDict = {}
   lineNum = 1
   tableState = "none"
   numCols = "none"
   tableNum = 0
   for line in rslt.split("\n"):
       # ignore first line, is the command echo - but always?!!!
       debugPrint("print","tableState "+tableState)
       debugPrint("print","line "+str(line))
       if lineNum >= 1:
           #print("*****row *****")
           colNum = 1
           # Store original line so we can calculate length correctly
           origLine = line
           # replace single spaces with special char, then switch back.
           line = re.sub("([^\s])\s([^\s])","\\1_pixieTempSpace_\\2",line)
           line = re.sub("([^\s])\s([^\s])","\\1_pixieTempSpace_\\2",line)
           debugPrint("print","line2 "+line)
           lsplit = line.split()
           numCols = len(lsplit)
           debugPrint("print","numCols "+str(numCols))
           if numCols <= 1:
               tableState = "none"
           elif numCols >= 2:
               # handle the no header case!!!
               if tableState is "none":
                   tableState = "headers-maybe" 
                   headers = lsplit
               elif tableState is "headers-maybe":
                   tableState = "headers-stored"
                   # 
                   #colWidths = {}
                   for col in lsplit:
                       regm = re.match("^-+$",col)
                       debugPrint("print","col should be - "+col+" -"+"regm "+str(regm))
                       if regm is None:
                           # did not match just dashes "----"
                           # not handled !!!
                           debugPrint("print","is not None")
                           # leave as headers maybe 
                           tableState = "headers-maybe"
                           headers = lsplit
                           break
                       else:
                           debugPrint("print","is None")
                   if tableState is "headers-stored":
                       tableNum = tableNum + 1
                       myDict[str(tableNum)] = {}
                       myDict[str(tableNum)]["metaColWidths"] = []
                       for col in lsplit:
                          myDict[str(tableNum)]["metaColWidths"].append(len(col))
                       tableState = "headers-data"
                   if tableState is "headers-maybe":
                      #print("Table State is headers-maybe")
                      tableNum = tableNum + 1
                      myDict[str(tableNum)] = {}
                      myDict[str(tableNum)]["metaColWidths"] = []
                      for col in lsplit:
                          myDict[str(tableNum)]["metaColWidths"].append(len(col))
                      tableState = "headers-data"
                       
               elif tableState is "headers-data":
                   # store data row. if not blank
                   colZero = lsplit[0]
                   colZero = re.sub("_pixieTempSpace_"," ",colZero)
                   myDict[str(tableNum)][colZero] = {}
                   
                   myDict[str(tableNum)]["metaAllCols"] = headers
                   myDict[str(tableNum)]["metaFirstCol"] = headers[0]
                   myDict[str(tableNum)]["metaOtherCols"] = "not done!"
                   
                   colNum = 1
                   headerNum = 1
                   for col in lsplit:
                       myData = lsplit[colNum]
                       myData = re.sub("_pixieTempSpace_"," ",myData)
                       prevCols = myDict[str(tableNum)]['metaColWidths'][:headerNum]
                       # Add each column width plus double space separator to find column index
                       searchIndex = sum(prevCols) + (len(prevCols) * 2)
                       foundIndex = origLine.find(myData, searchIndex)
                       if foundIndex < 0:
                          # Set unit
                          myDict[str(tableNum)][colZero]['unit'] = myData
                          colNum = colNum + 1
                          continue
                       else:
                          while foundIndex - searchIndex > myDict[str(tableNum)]['metaColWidths'][headerNum]:
                             debugPrint("print", f"Next item is too far out. {searchIndex} {foundIndex}")
                             myHeader = headers[headerNum]
                             myHeader = re.sub("_pixieTempSpace_"," ",myHeader)
                             # Set empty column to blank string
                             myDict[str(tableNum)][colZero][myHeader] = ""
                             headerNum = headerNum + 1
                             prevCols = myDict[str(tableNum)]['metaColWidths'][:headerNum]
                             searchIndex = sum(prevCols) + (len(prevCols) * 2)
                          myHeader = headers[headerNum]
                          myHeader = re.sub("_pixieTempSpace_"," ",myHeader)
                          myDict[str(tableNum)][colZero][myHeader] = myData
                          #print( tableNum, lsplit[0], headers[headerNum], lsplit[colNum] )
                          colNum = colNum + 1
                          headerNum = headerNum + 1
                          if colNum >= len(lsplit):
                             break
                   myDict["metaNumTables"] = tableNum
       lineNum = lineNum + 1
   if toStash is not False:
      debugPrint("print","toStash "+str(toStash))
      stashData("set",toStash,myDict)
   else:
      debugPrint("print","toStash "+str(toStash))
   #print(myDict)
   newMyDict=_reorderDict(myDict)
   #print(newMyDict)
   if printCompares:
      _printCompares(newMyDict, printCompares)
   return newMyDict

def _reorderDict(myDict):
   """
   This function reorders the structure of mydict from 
   ret['1']['card-1-1']['chassis-name']
   to this
   ret['card-1-1']['chassis-name']

   :param myDict: _description_
   :type myDict: _type_
   :return: _description_
   :rtype: _type_
   """   
   restructured_data = {}
   if len(myDict)==0:
      print("Empty Dictionary")
      return restructured_data
   myDict2=myDict['1']
   res=list(myDict2.keys())[1]
   inner_key_value=res[:res.find("-")+1]#Extracting if its show inventory or show card or show port,etc  values in dictionary
   for key, value in myDict.items():
    if key.isdigit():
        for inner_key, inner_value in value.items():
            if inner_key.startswith(inner_key_value):
                #print(inner_key)
                #print(inner_value)
                if inner_key in restructured_data:
                    my_list = [(key, value) for key, value in inner_value.items()]
                    #print(my_list)
                    my_list_2=restructured_data[inner_key]
                    #print(my_list_2)
                    my_list_3=[(key, value) for key, value in my_list_2.items()]
                    #print(my_list_3)
                    my_list_3.extend(my_list)
                    my_list_3+=my_list
                    #print(my_list_3)
                    restructured_data[inner_key]=dict(my_list_3)
                else:
                    restructured_data[inner_key] = inner_value
   return restructured_data


def _printCompares(data, varName):
    print(">>> Begin compares")
    for key in data:
       pairsList=[]
       keyData=data[key]
       for(key1,value1) in keyData.items():
         pairsList.append((f"{key1}",f"{value1}"))
       print(f"g40cli.compareTablePairs({varName},  '{key}', {pairsList})")
    """
    for (tableId, tableData) in data.items():
        if 'meta' not in tableId:
            realKeys = [k for k in tableData if not k.startswith('meta')]
            for lineId in realKeys:
                pairsList = []
                lineData = tableData[lineId]
                for (lineKey, lineVal) in lineData.items():
                    pairsList.append((f"{lineKey}", f"{lineVal}"))
                print(f"g40cli.compareTablePairs({varName}, '{tableId}', '{lineId}', {pairsList})")
    """
    print(">>> End compares")


def compareTablePairs(data, tableId, rowName, pairsList):
   """
   **Example**
   ::

      g40cli.compareTablePairs(data, '3', 'inventory-1-FAN-1', [('actual-subtype', 'counter-rotating')])
        
         CLI Show Example:
            
            inventory              actual-subtype    
            
            ---------------------  ----------------             
            inventory-1-FAN-1      counter-rotating

   :param data: dictionary of data to compare
   :type data: dict
   :param tableId: index of table in cli show command
   :type tableId: string
   :param rowName: name of row (column zero) to compare
   :type rowName: string
   :param pairsList: list of tuples (key, expectedValue) 
            key should point to a valid key in dictionary and correspond to a table column name expectedValue is the value expected in that location
   :type pairsList: list
   """   

   for (key, expected) in pairsList:
      actual="not-yet-set"
      try:
         actual = data[rowName][key]
         print(rowName+" "+key)
         if(actual==expected):
            #compareStep(actual, expected)
            step("Compare "+rowName+" "+key,"passed"," Expected "+expected+" Actual "+actual)
         else:
            step("Compare "+rowName+" "+key,"failed"," Expected "+expected+" Actual "+actual)
      except Exception as e:
         print(e)
         step("Compare "+rowName+" "+key,"failed"," Expected "+expected+" Actual "+actual)

def retDataToTwoCols(rslt):
   
   """
   
   Useful with show command that does not return headers, but does have cols.
   - only the two col data is returned here, lines with other number of cols ( i.e. 1) are igored.
 
   **Example**

   ::

       If your data has headers, please use g40cli.retDataToTables.

       rslt = g40cli.sendRcv("cli1","show")
         
       dResult = g40cli.retDataToTwoCols(rslt) 
         
       rex.comparePairs("notStash",dResult['altitude'],'0 meters',dResult['oper-state'],'enabled')

       for rowKey in dResult["metaTwoColRows"]:
            
         print("rowKey ",rowKey," ",eval("dResult[rowKey]"))

   :param rslt: Data as returned by sendRcv command
   :type rslt: string
   :return: Dictionary of parsed table data
   :rtype: dict
   """   
   
   myDict = {}
   lineNum = 1
   numCols = "none"
   myDict["metaTwoColRows"] = []
   for line in rslt.split("\n"):
       # ignore first line, is the command echo - but always?!!!
       debugPrint("print","line "+str(line))
       if lineNum >= 1:
           #print("*****row *****")
           colNum = 1
           # replace single spaces with special char, then switch back.
           line = re.sub("([^\s])\s([^\s])","\\1_pixieTempSpace_\\2",line)
           line = re.sub("([^\s])\s([^\s])","\\1_pixieTempSpace_\\2",line)
           debugPrint("print","line2 "+line)
           lsplit = line.split()
           numCols = len(lsplit)
           debugPrint("print","numCols "+str(numCols))
           if numCols>2:
              col0 = lsplit[0]
              col0 = re.sub("_pixieTempSpace_"," ",col0) 
              myDict["metaTwoColRows"].append(col0)
              a=rslt.find("'")
              b=rslt.rfind("'")
              #print(rslt[a:b+1])
              col1 = rslt[a:b+1]
              col1=re.sub("\n"," ",col1)
              col1 = re.sub("_pixieTempSpace_"," ",col1)
              myDict[col0] = col1
           elif numCols != 2:
               tableState = "none"
           else:
               col0 = lsplit[0]
               print(col0)
               col0 = re.sub("_pixieTempSpace_"," ",col0)
               print(col0)
               myDict["metaTwoColRows"].append(col0)
               col1 = lsplit[1]
               col1 = re.sub("_pixieTempSpace_"," ",col1)
               myDict[col0] = col1
       lineNum = lineNum + 1
   return myDict