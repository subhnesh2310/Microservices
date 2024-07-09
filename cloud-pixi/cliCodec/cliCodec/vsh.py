from socket import MsgFlag
import paramiko
import time

import tkinter
from tkinter import ttk
# import sv_ttk   #CPIXI

import gc
import os
from ncclient import manager, xml_
from ncclient.operations.rpc import RPCError
# from getpass import getpass
import logging
from pprint import pformat
from bs4 import BeautifulSoup
import re
import xml.etree.ElementTree as ET
from lxml import etree, objectify
import pandas as pd
from datetime import datetime
import string
import random
import pandas as pd
try:
    from pygnmi.client import gNMIclient,telemetryParser
except:
    #print("Warning:  Please run pip install protobuf==3.20.* (See install doc)")
    pass
import json
# import plotly.graph_objects as go
import webbrowser
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

# ???
# import rexui
#import rex
from cliCodec.libs import pixi


# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# f_handler = logging.FileHandler('execution_Logs.log')
# f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# f_handler.setLevel(logging.INFO)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  #CPIXI

# !!! - see settings at end of file!


class Vsh:
    """
    ----------------------
    Vsh - **Virtual Shell**
    
    This is the main connection class with the methods appropriate for the various operations such as
        - CLI operations
        - NETCONF operations
        - gRPC operations
        - RESTCONF operations
    The objects of the class is handles of different connections/sessions managed by PiXie
    ----------------------
    """
    _connIDs = []
    _connDict = {}

    def __init__(self, connId, logger, handle):
        self.connId = connId
        self._connIDs.append(connId)
        self.handle = handle
        self.logger = logger
        self.ssh = {}
        self.chan = {}
        self.chann = {}
        self.bufStr = {}
        self.debug = "TRUE"
        #
        # self.sim = True
        self._sim = False
        return None
    
    def _get_dco_config(self,object = None):
        object = object
        os.system('start cmd /D /C "python netclient.py && pause"')

    def _get_setupEnvironment(self,sut = None,option = None, local = False):
        # Use Input.yml set via PIXI_LOCAL_INPUT if set, otherwise use default pixi-provided copy
        pixi_home = pixi.home()
        env_path = pixi.local_input()
        if pixi_home and env_path:
            input_path = os.path.join(pixi_home, env_path)
        else:
            input_path = 'Input.yml'
        with open(input_path, 'r') as file:
            config_env = yaml.safe_load(file)
        return (config_env.get(sut, {}).get(option))
    
    def _netConnector (self, **kwargs):
        connId = self.connId
        keys = [k for k, v in connsdb.items() if connId in v]

        protocol = kwargs.get('protocol', None)
        sut = kwargs.get('sut', None)
        local = kwargs.get('local', False)
        ip = kwargs.get('ip', None)
        username = kwargs.get('username', None)
        password = kwargs.get('password', None)
        
        if protocol == "netconf":
            if sut:
                login_parameters = pixi.get_setupEnvironment(sut = sut, option = 'Login', local = local)
                ip = login_parameters['IpAddress']
                username = login_parameters['UserName']
                password = login_parameters['Password']
            conn_manager =  manager.connect(host = ip,
                                    port = 830,
                                    username = username,
                                    password = password,
                                    #  device_params={'name': 'infinera'},
                                    hostkey_verify = False,
                                    allow_agent = False,
                                    look_for_keys = False,
                                    timeout = 90)
        if protocol == "grpc":
            skip_verify = kwargs.get('skip_verify', False)
            port = kwargs.get('port', "50051")
            if sut:
                login_parameters = pixi.get_setupEnvironment(sut = sut, option = 'Login', local = local)
                interface_parameters = pixi.get_setupEnvironment(sut = sut, option = 'Interface', local = local)
                ip = login_parameters['IpAddress']
                username = login_parameters['UserName']
                password = login_parameters['Password']
                port = login_parameters['gRPCPort']
            if skip_verify:
                conn_manager = gNMIclient(target = (ip, port),
                                username = username,
                                password = password,
                                skip_verify = True,
                                timeout = 90)
            else:
                conn_manager = gNMIclient(target = (login_parameters['IpAddress'],login_parameters['gRPCPort']),
                                username = login_parameters['UserName'],
                                password = login_parameters['Password'],
                                path_root = login_parameters.get('ClientCertificateRoot', None),
                                path_cert = login_parameters['ClientCertificateFileName'],
                                path_key = login_parameters.get('ClientCertificateKey', None),
                                override = interface_parameters['OverrideParameter'],
                                timeout = 90)

        if protocol == "restconf":
            conn_manager = requests.Session()
            conn_manager.auth = (username, password)

        if protocol == "xr_restconf":
            data = {'username': f'{username}',
                    'password': f'{password}',
                    'grant_type': 'password',
                    'client_secret': 'xr-web-client',
                    'client_id': 'xr-web-client'
                    }
            response = requests.post(
                f'https://{ip}/realms/xr-cm/protocol/openid-connect/token', data=data, verify=False)
            token = response.json().get("access_token")
            conn_manager = requests.Session()
            conn_manager.headers.update({'Authorization': f'Bearer {token}'})
            
        if protocol == "testset":
            login_parameters = pixi.get_setupEnvironment(sut = sut,option = 'Login', local = local) 
            conn_manager = ONT( logger_handle = keys[0], ipaddress = login_parameters['IpAddress'],
                                ont_portConf = login_parameters['PortConf'],
                                ont_mode = login_parameters['DeviceMode'],
                                chassis = login_parameters['Chassis'],
                                slot = login_parameters['Slot'],
                                port = login_parameters['Port'],
                                port_type = login_parameters['Rate']) 
        return conn_manager

    def ts_connect(self,**kwargs):
        """
        ----------------------
            ts_connect()
        
        Method to connect to the ONT testset using the connectionhandle. This creates a connection object which is unique for each session. 
            
            Parameters:
            None
        **Example :** 

            conns['ts'].ts_connect()
        ----------------------
        """
        sut = kwargs.get('sut', None)
        local = kwargs.get('local', False)
        connId = self.connId
        self.ssh[connId] = self._netConnector(protocol = 'testset', sut = sut, local = local)
        return 1 


    def grpc_connect(self,**kwargs):
        """
        ----------------------
            grpc_connect()
        
        Method to connect to the CM using the handle. This creates a connection object which is unique for each session. 
            
            Parameters:
            None
        **Example :** 

            conns['grpc'].grpc_connect()
        ----------------------
        """
        sut = kwargs.get('sut', None)
        local = kwargs.get('local', False)
        ip = kwargs.get('ip', None)
        username = kwargs.get('username', None)
        password = kwargs.get('password', None)
        skip_verify = kwargs.get('skip_verify', False)
    
        connId = self.connId
        use_rexui = True
        #use_rexui = False     
        try:
            #gCLI1 = rexui.App.notebookRoot()
            gCLI1 = rexui.gCLI1

        except:
            use_rexui = False
        
        if use_rexui:
            pQueue = pixi.PIXIQueue()
            pQueue.put({
                "command": "create_window",
                "data": {
                    "handle": self.handle,
                    "vsh": self
                }
            })
            #self.frame3 = ttk.Frame(self.notebook, width=150, height=250)
            #self.frame3.pack(fill='both', expand=True)
            #self.notebook.add(self.frame3, text='Conn1')
            """
            self.frame = ttk.Frame(gCLI1, width=150, height=250)
            self.rootn = self.frame
            self.frame.pack(fill='both', expand=True)
            gCLI1.add(self.frame, text=str(self.handle))

            self.Tn = tkinter.Text(
                self.frame, height=18, width=100, bg="black", fg="white"
            )
            
            self.Tn.pack()

            self.scroll_bar = tkinter.Scrollbar(self.frame)
            self.scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
            self.scroll_bar.config(command=self.Tn.yview)
            self.Tn.config(yscrollcommand=self.scroll_bar.set)
            
            self.frame1 = tkinter.Frame(self.frame)
            self.frame1.pack(side=tkinter.TOP)

            self.entry = tkinter.Entry(self.frame1, width=60)
            self.entry.pack(side=tkinter.RIGHT)
            self.entry.bind('<Return>',self._sndButton)
            """
            
        else:
            rootn = "root" + str(connId)
            self.rootn = tkinter.Tk()
            # cstr = "vsh connection #" + str(connId)
            cstr = "vsh connection #" + str(self.handle)
            self.rootn.title(cstr)
            Tn = "T" + str(connId)
            # 1/17 - was 96 for a bit
            self.Tn = tkinter.Text(
                self.rootn, height=10, width=100, bg="black", fg="white"
            )

            # new
            # self.scroll?!!!
            scroll_bar = tkinter.Scrollbar(self.rootn)
            #!!! self.rootn , tkinter
            scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
            scroll_bar.config(command=self.Tn.yview)
            self.Tn.config(yscrollcommand=scroll_bar.set)

            #  command = nada
            # should be self.frame1???
            self.frame1 = tkinter.Frame(self.rootn)
            self.frame1.pack(side=tkinter.TOP)

            self.entry = tkinter.Entry(self.frame1, width=60)
            self.entry.pack(side=tkinter.LEFT)

            self.sendButton = tkinter.Button(
                self.frame1, height=2, width=6, text="Send", command=self._sndButton
            )
            self.sendButton.pack(side=tkinter.RIGHT)
            # new end

            self.Tn.pack(side=tkinter.LEFT)
        ####### copy paste from connect( end

        self.ssh[connId] = self._netConnector(protocol = 'grpc', sut=sut, local=local, ip=ip, username=username, password=password, skip_verify=skip_verify)
        self.ssh[connId].connect()
        return 1 

 
    def xr_connect(self,**kwargs):
        """
        ----------------------
            xr_connect()
        
        Method to connect to the CM using the handle. This creates a connection object which is unique for each session. 
            
            Parameters:
            None
        **Example :** 

            conns['xr'].xr_connect()
        ----------------------
        """
 
        ############### copy paste from connect( _connect_ui_part ( not working to call)
        #_connect_ui_part(self, **kwargs)

        ip = kwargs.get('ip', None)
        username = kwargs.get('username', None)
        password = kwargs.get('password', None)
    
        connId = self.connId
        use_rexui = True
        #use_rexui = False     
        try:
            #gCLI1 = rexui.App.notebookRoot()
            gCLI1 = rexui.gCLI1

        except:
            use_rexui = False
        
        if use_rexui:
            pQueue = pixi.PIXIQueue()
            pQueue.put({
                "command": "create_window",
                "data": {
                    "handle": self.handle,
                    "vsh": self
                }
            })
            #self.frame3 = ttk.Frame(self.notebook, width=150, height=250)
            #self.frame3.pack(fill='both', expand=True)
            #self.notebook.add(self.frame3, text='Conn1')
            """
            self.frame = ttk.Frame(gCLI1, width=150, height=250)
            self.rootn = self.frame
            self.frame.pack(fill='both', expand=True)
            gCLI1.add(self.frame, text=str(self.handle))

            self.Tn = tkinter.Text(
                self.frame, height=18, width=100, bg="black", fg="white"
            )
            
            self.Tn.pack()

            self.scroll_bar = tkinter.Scrollbar(self.frame)
            self.scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
            self.scroll_bar.config(command=self.Tn.yview)
            self.Tn.config(yscrollcommand=self.scroll_bar.set)
            
            self.frame1 = tkinter.Frame(self.frame)
            self.frame1.pack(side=tkinter.TOP)

            self.entry = tkinter.Entry(self.frame1, width=60)
            self.entry.pack(side=tkinter.RIGHT)
            self.entry.bind('<Return>',self._sndButton)
            """
        else:
            rootn = "root" + str(connId)
            self.rootn = tkinter.Tk()
            # cstr = "vsh connection #" + str(connId)
            cstr = "vsh connection #" + str(self.handle)
            self.rootn.title(cstr)
            Tn = "T" + str(connId)
            # 1/17 - was 96 for a bit
            self.Tn = tkinter.Text(
                self.rootn, height=10, width=100, bg="black", fg="white"
            )

            # new
            # self.scroll?!!!
            scroll_bar = tkinter.Scrollbar(self.rootn)
            #!!! self.rootn , tkinter
            scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
            scroll_bar.config(command=self.Tn.yview)
            self.Tn.config(yscrollcommand=scroll_bar.set)

            #  command = nada
            # should be self.frame1???
            self.frame1 = tkinter.Frame(self.rootn)
            self.frame1.pack(side=tkinter.TOP)

            self.entry = tkinter.Entry(self.frame1, width=60)
            self.entry.pack(side=tkinter.LEFT)

            self.sendButton = tkinter.Button(
                self.frame1, height=2, width=6, text="Send", command=self._sndButton
            )
            self.sendButton.pack(side=tkinter.RIGHT)
            # new end

            self.Tn.pack(side=tkinter.LEFT)
        ####### copy paste from connect( end
        self.ssh[connId] = self._netConnector(protocol = 'xr_restconf', ip=ip, username=username, password=password)
        return 1 
    
    def restconf_connect(self,**kwargs):
        """
        ----------------------
            restconf_connect()
        
        Method to connect to the GX G40 NE using the handle over the RESTCONF interface
            
            Parameters:
            None
        **Example :** 

            conns['g40'].restconf_connect()
        ----------------------
        """
        ############### copy paste from connect( _connect_ui_part ( not working to call)
        #_connect_ui_part(self, **kwargs)
        username = kwargs.get('username', None)
        password = kwargs.get('password', None)
    
        connId = self.connId
        use_rexui = True
        #use_rexui = False     
        try:
            #gCLI1 = rexui.App.notebookRoot()
            gCLI1 = rexui.gCLI1

        except:
            use_rexui = False
        
        if use_rexui:
            pQueue = pixi.PIXIQueue()
            pQueue.put({
                "command": "create_window",
                "data": {
                    "handle": self.handle,
                    "vsh": self
                }
            })
            #self.frame3 = ttk.Frame(self.notebook, width=150, height=250)
            #self.frame3.pack(fill='both', expand=True)
            #self.notebook.add(self.frame3, text='Conn1')
            """
            self.frame = ttk.Frame(gCLI1, width=150, height=250)
            self.rootn = self.frame
            self.frame.pack(fill='both', expand=True)
            gCLI1.add(self.frame, text=str(self.handle))

            self.Tn = tkinter.Text(
                self.frame, height=18, width=100, bg="black", fg="white"
            )
            
            self.Tn.pack()

            self.scroll_bar = tkinter.Scrollbar(self.frame)
            self.scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
            self.scroll_bar.config(command=self.Tn.yview)
            self.Tn.config(yscrollcommand=self.scroll_bar.set)
            
            self.frame1 = tkinter.Frame(self.frame)
            self.frame1.pack(side=tkinter.TOP)

            self.entry = tkinter.Entry(self.frame1, width=60)
            self.entry.pack(side=tkinter.RIGHT)
            self.entry.bind('<Return>',self._sndButton)
            """
        else:
            rootn = "root" + str(connId)
            self.rootn = tkinter.Tk()
            # cstr = "vsh connection #" + str(connId)
            cstr = "vsh connection #" + str(self.handle)
            self.rootn.title(cstr)
            Tn = "T" + str(connId)
            # 1/17 - was 96 for a bit
            self.Tn = tkinter.Text(
                self.rootn, height=10, width=100, bg="black", fg="white"
            )

            # new
            # self.scroll?!!!
            scroll_bar = tkinter.Scrollbar(self.rootn)
            #!!! self.rootn , tkinter
            scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
            scroll_bar.config(command=self.Tn.yview)
            self.Tn.config(yscrollcommand=scroll_bar.set)

            #  command = nada
            # should be self.frame1???
            self.frame1 = tkinter.Frame(self.rootn)
            self.frame1.pack(side=tkinter.TOP)

            self.entry = tkinter.Entry(self.frame1, width=60)
            self.entry.pack(side=tkinter.LEFT)

            self.sendButton = tkinter.Button(
                self.frame1, height=2, width=6, text="Send", command=self._sndButton
            )
            self.sendButton.pack(side=tkinter.RIGHT)
            # new end

            self.Tn.pack(side=tkinter.LEFT)
        ####### copy paste from connect( end
        self.ssh[connId] = self._netConnector(protocol = 'restconf', username = username, password = password)
        return 1
        
    # def netconf_connect(self, sut = None, port= None, username = None, password=None, **kwargs):
    def netconf_connect(self, **kwargs):
        """
        ----------------------
            netconf_connect()
        
        Method to connect to the NE with NETCONF using the handle. This creates a connection object which is unique for each session. 
            
            Parameters:
            None
        **Example :** 

            conns['netconf1'].netconf_connect()
        ----
        """
        sut = kwargs.get('sut', None)
        local = kwargs.get('local', False)
        ip = kwargs.get('ip', None)
        username = kwargs.get('username', None)
        password = kwargs.get('password', None)
        
        ############### copy paste from connect( _connect_ui_part ( not working to call)
        #_connect_ui_part(self, **kwargs)
    
        connId = self.connId
        use_rexui = True
        #use_rexui = False     
        try:
            #gCLI1 = rexui.App.notebookRoot()
            gCLI1 = rexui.gCLI1

        except:
            use_rexui = False
        
        if use_rexui:
            pQueue = pixi.PIXIQueue()
            pQueue.put({
                "command": "create_window",
                "data": {
                    "handle": self.handle,
                    "vsh": self
                }
            })
            #self.frame3 = ttk.Frame(self.notebook, width=150, height=250)
            #self.frame3.pack(fill='both', expand=True)
            #self.notebook.add(self.frame3, text='Conn1')
            """
            self.frame = ttk.Frame(gCLI1, width=150, height=250)
            self.rootn = self.frame
            self.frame.pack(fill='both', expand=True)
            gCLI1.add(self.frame, text=str(self.handle))

            self.Tn = tkinter.Text(
                self.frame, height=18, width=100, bg="black", fg="white"
            )
            
            self.Tn.pack()

            self.scroll_bar = tkinter.Scrollbar(self.frame)
            self.scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
            self.scroll_bar.config(command=self.Tn.yview)
            self.Tn.config(yscrollcommand=self.scroll_bar.set)
            
            self.frame1 = tkinter.Frame(self.frame)
            self.frame1.pack(side=tkinter.TOP)

            self.entry = tkinter.Entry(self.frame1, width=60)
            self.entry.pack(side=tkinter.RIGHT)
            self.entry.bind('<Return>',self._sndButton)
            """
        else:
            rootn = "root" + str(connId)
            self.rootn = tkinter.Tk()
            # cstr = "vsh connection #" + str(connId)
            cstr = "vsh connection #" + str(self.handle)
            self.rootn.title(cstr)
            Tn = "T" + str(connId)
            # 1/17 - was 96 for a bit
            self.Tn = tkinter.Text(
                self.rootn, height=10, width=100, bg="black", fg="white"
            )

            # new
            # self.scroll?!!!
            scroll_bar = tkinter.Scrollbar(self.rootn)
            #!!! self.rootn , tkinter
            scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
            scroll_bar.config(command=self.Tn.yview)
            self.Tn.config(yscrollcommand=scroll_bar.set)

            #  command = nada
            # should be self.frame1???
            self.frame1 = tkinter.Frame(self.rootn)
            self.frame1.pack(side=tkinter.TOP)

            self.entry = tkinter.Entry(self.frame1, width=60)
            self.entry.pack(side=tkinter.LEFT)

            self.sendButton = tkinter.Button(
                self.frame1, height=2, width=6, text="Send", command=self._sndButton
            )
            self.sendButton.pack(side=tkinter.RIGHT)
            # new end

            self.Tn.pack(side=tkinter.LEFT)
        ####### copy paste from connect( end
        self.ssh[connId] = self._netConnector(sut=sut , protocol='netconf', local=local, ip=ip, username=username, password=password)
        return 1 

    def _fetch_uri(self, **kwargs):
        resp = ''
        connection_handle = {
            "device_type": "terminal_server",
            "ip":  kwargs.get('server_Ip', None),
            "username":  kwargs.get('username', None),
            "port": 22,
            "password":  kwargs.get('password', None),
            "verbose": False,
        }
        fetch_obj = kwargs.get('object', None)
        try:
            my_cmd = "convert restconf-json \"show " + fetch_obj + "\""
            net_connect = paramiko.SSHClient()
            net_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            net_connect.connect(hostname=connection_handle['ip'],username=connection_handle['username'], password=connection_handle['password'], port=connection_handle['port'], look_for_keys=False, allow_agent=False)
            time.sleep(1)
            nc = net_connect.invoke_shell()
            output = nc.recv(1000)
            nc.send("terminal length 0\n")
            time.sleep(1)
            output = nc.recv(1000)
            nc.send("\n")
            nc.send(my_cmd+"\n")
            time.sleep(1)
            resp = nc.recv(5000).decode('ascii')
            net_connect.close()
            
        except Exception as e:
            plogger.error_log(handle ='cli1',msg = e )
        return resp

    def _fetch_xr_uri(self, object_name, server_ip, name):
        uri = ""
        connId = self.connId
        if self._connDict['xr_version'] == '0.7':
            if object_name == "hosts":
                uri = '/api/v1/hosts'
            if object_name == "host" :
                uri = '/api/v1/hosts/' +  name
            if object_name == "ports" :
                uri = '/api/v1/hosts/' +  name + "/ports"
            if object_name == "port" :
                uri = '/api/v1/hosts/' +  name.split('%')[0] + "/ports/" + name.split('%')[1]
            if object_name == "networks":
                uri = '/api/v1/xr-networks'
            if object_name == "networks-hub" :
                uri = '/api/v1/xr-networks/' + name + '/hubModule'
            if object_name == "networks-leaf" :
                uri = '/api/v1/xr-networks/' + name + '/leafModules'
            if object_name == "reachable-modules" :
                uri = '/api/v1/xr-networks/' + name + '/reachableModules'
            if object_name == "reachable-module" :
                uri = '/api/v1/xr-networks/' + name.split('%')[0]  + '/reachableModules/' +name.split('%')[1]
            if object_name == "modules":
                uri = '/api/v1/modules'
            if object_name == "module-ports":
                uri = '/api/v1/modules/' + name + '/ports'
            if object_name == "module-port":
                uri = '/api/v1/modules/' + name.split('%')[0] + '/ports/' + name.split('%')[1]
            if object_name == "transport-capacities" :
                uri = '/api/v1/transport-capacities'
            if object_name == "discovered-devices" :
                uri = '/api/v1/obt/devices'
            if object_name == "network-connections":
                uri = "/api/v1/network-connections"
            if object_name == "network-connection":
                uri = "/api/v1/network-connections/"
        if self._connDict['xr_version'] == '0.5':
            if object_name == "hosts":
                uri = '/api/v1/hms/hosts'
            if object_name == "host" :
                uri = '/api/v1/hms/hosts/' +  name
            if object_name == "ports" :
                uri = '/api/v1/hms/hosts/' +  name + "/ports"
            if object_name == "port" :
                uri = '/api/v1/hms/hosts/' +  name.split('%')[0] + "/ports/" + name.split('%')[1]
            if object_name == "networks":
                uri = '/api/v1/ns/xr-networks'
            if object_name == "networks-hub" :
                uri = '/api/v1/ns/xr-networks/' + name + '/hubModule'
            if object_name == "networks-leaf" :
                uri = '/api/v1/ns/xr-networks/' + name + '/leafModules'
            if object_name == "reachable-modules" :
                uri = '/api/v1/ns/xr-networks/' + name + '/reachableModules'
            if object_name == "reachable-module" :
                uri = '/api/v1/ns/xr-networks/' + name.split('%')[0]  + '/reachableModules/' +name.split('%')[1]
            if object_name == "modules":
                uri = '/api/v1/mm/modules'
            if object_name == "module-ports":
                uri = '/api/v1/mm/modules/' + name + '/ports'
            if object_name == "module-port":
                uri = '/api/v1/mm/modules/' + name.split('%')[0] + '/ports/' + name.split('%')[1]
            if object_name == "transport-capacities" :
                uri = '/api/v1/ns/transport-capacities'
            if object_name == "discovered-devices" :
                uri = '/api/v1/obt/devices'
            if object_name == "network-connections":
                uri = "/api/v1/ncs/network-connections"
            if object_name == "network-connection":
                uri = "/api/v1/ncs/network-connections/"
        return uri

    def configTestset(self,**kwargs):
        """
        ----------------------
            configTestset(rate = <rate>, frame_size= <for the ethernet traffic>)
        
        Method to configure the ONT-602 testset as per the configurations defined in the input.yaml

        **Example :** 

            conns['ts'].configTestset(rate= '100GBE',frame_size = 2000)
        ----------------------
        """  
        connId = self.connId
        rate = kwargs.get('rate', None)
        frame_size = kwargs.get('frame_size', None)
        keys = [k for k, v in connsdb.items() if connId in v]
        result = self.ssh[connId].configureTestset(keys[0],rate,FrameSize=frame_size)
        return result

    def startMeasurement(self,**kwargs):
        """
        ----------------------
            startMeasurement()
        
        Method to START the test measurement on the ONT-602 remotely

        **Example :** 

            conns['ts'].startMeaurement()
        ----------------------
        """  
        connId = self.connId
        keys = [k for k, v in connsdb.items() if connId in v]
        self.ssh[connId].start_measurement(keys[0])
        return

    def stopMeasurement(self,**kwargs):
        """
        ----------------------
            stopMeasurement()
        
        Method to STOP the test measurement on the ONT-602 remotely

        **Example :** 
            `conns['ts'].stopMeaurement()`
        ----------------------
        """  
        connId = self.connId
        keys = [k for k, v in connsdb.items() if connId in v]
        self.ssh[connId].stop_measurement(keys[0])
        return

    def releaseTestset(self,**kwargs):
        """
        ----------------------
            releaseTestset()
        
        Method to unload the application and release the testset ports and testset connection - method only for ONT-602
        This method also unloads the application

        **Example :** 

            conns['ts'].releaseTestset()
        ----------------------
        """  
        connId = self.connId
        keys = [k for k, v in connsdb.items() if connId in v]
        self.ssh[connId].release(keys[0])
        return

    def releaseOnlyTestset(self,**kwargs):
        """
        ----------------------
            releaseOnlyTestset()
        
        Method to unload the application and release the testset ports and testset connection - method only for ONT-602
        This method doesn't unload the application

        **Example :** 

            conns['ts'].releaseOnlyTestset()
        ----------------------
        """  
        connId = self.connId
        keys = [k for k, v in connsdb.items() if connId in v]
        self.ssh[connId].releaseOnly(keys[0])
        return


    def checkTrafficCurrent(self, **kwargs):
        """
        ----------------------
            checkTrafficCurrent()
        
        Method to check if there are any outstanding alarm/error on any layer ? \
        This is helpful in knowing if there is any alarm/error after soak tests\
        This method only gives if it has alarm/error or not , it doesn't tell you\
        how many errors/ what errors/alarms are present - method only for ONT-602

            Parameters:
            : expctAlmErr -> boolean 
                            options :
                                True    # In case of alarm/errors injection, you expect them to present
                                False   # In case of clear soak test , you dont expect alarm/errors

        **Example :** 

            conns['ts'].checkTrafficCurrent(expectAlarmError = False)
        ----------------------
        """  
        connId = self.connId
        expctAlmErr = kwargs.get('expectAlarmError', None)
        keys = [k for k, v in connsdb.items() if connId in v]
        result = self.ssh[connId].check_traffic_current(keys[0],expctAlmErr = expctAlmErr)
        return result


    def injectAlarm(self, **kwargs):
        """
        ----------------------
            injectAlarm()
        
        Method to inset an alarm on a specific layer \
        For this release it's only for 100GbE alarms insertion\
        This means any alarms on PHYS or PCS or MAC layer alarms\
        - method only for ONT-602

            Parameters:
            : logger_handle -> testset handle name  -> string
            : Alarm -> Alarm to be inserted  -> string
                            options : 
                                    phys_alarm = ["LOS"]
                                    pcs_alarm = ["LOBL", "LOAML", "HIBER", "LOC_FAULT", "REM_FAULT", "LOAMPS", 
                                                 "LOC_DSER", "REM_DSER", "HSER", "LOA", "LOLM"]
                                    mac_alarm = ["IFS"]
            : Layer -> Layer at which alarm is inserted  -> string
                            options :
                                PHYS # This is the Phy layer alarm
                                PCS  # this is the PCS layer alarm
                                MAC  # This is the MAC layer alarm
            : Duration -> How long the alarm needs to be injected  -> int
                            Default : 0
            : Mode -> Mode of the alarm   -> string
                            Default : 'CONT'

        **Example :** 

            conns['ts'].injectAlarm(Alarm="LOC_FAULT",Duration="CONT",layer="PCS")\n
            conns['ts'].injectAlarm(Alarm="LOAML",Duration=10,Mode = "CONT",Layer="PCS")\n
            conns['ts'].injectAlarm(Alarm="LOS",Duration=10,Mode = "CONT",Layer="PHYS")\n
        ----------------------
        """  
        connId = self.connId
        alarm = kwargs.get('Alarm', None)
        layer = kwargs.get('Layer', None)
        duration = kwargs.get('Duration', None)
        mode = kwargs.get('Mode', None)
        keys = [k for k, v in connsdb.items() if connId in v]
        result = self.ssh[connId].insertAlarm(keys[0],Alarm=alarm,Mode=mode,Layer=layer,Duration = duration)
        return result


    def injectErrors(self, **kwargs):
        """
        ----------------------
            injectErrors()
        
        Method to inset errors at a specific layer \
        For this release it's only for 100GbE alarms insertion\
        This means any alarms on PHYS or PCS or MAC layer alarms\
        - method only for ONT-602

            Parameters:
            : logger_handle -> testset handle name  -> string
            : Error -> Alarm to be inserted  -> string
                            options :
                                phys_error = ['BIT_ERROR']
                                pcs_error = ['SYNC_HEADER_INV', 'IAM', 'BIP8', 'ITB', 'FEC_CORR', 
                                            'FEC_UNCORR', 'USER_AM_SEQ', 'BLOC_TYPE_INV']
                                mac_error = ['RUNT', 'OV', 'FCS', 'SFD', 'JABB', 'FLOS', 'DUPL', 'MIS', 'SWAP']
            : Layer -> Layer at which alarm is inserted  -> string
                            options :
                                PHYS # This is the Phy layer errors
                                PCS  # this is the PCS layer errors
                                MAC  # This is the MAC layer errors
            : Duration -> How long the errors needs to be injected (seconds) -> int
                            Default : 0
            : Rate -> Rate of Error if applicable -> string 
            : ActiveErrorFrames -> Errored Frames -> int
            : InactiveErrorFrames -> Error free franes ->int
            : Mode -> Mode of the alarm   -> string
                            Default : 'CONT'

        **Example :** 

            conns['ts'].injectErrors(Error="RUNT", Layer="MAC", Mode="BURST_CONT", ActiveErrorFrames=2000, InactiveErrorFrames=2000, Duration  = 5)\n
            conns['ts'].injectErrors(Error="RUNT", Layer="MAC", Mode="CONT", ActiveErrorFrames=0, InactiveErrorFrames=0, Duration  = 5)\n
            conns['ts'].injectErrors(Error="FLOS", Layer="MAC", Mode="CONT", ActiveErrorFrames=0, InactiveErrorFrames=0, Duration  = 5)\n
            conns['ts'].injectErrors(Error="FCS", Layer="MAC", Mode="CONT", ActiveErrorFrames=0, InactiveErrorFrames=0, Duration  = 5)\n
            conns['ts'].injectErrors(Error="BIP8", Layer="PCS", Rate="1.0E-4", lane = 1 , Mode = "RATE", ActiveErrorFrames=0, InactiveErrorFrames=0,Duration  = 5)\n
            conns['ts'].injectErrors(Error="RUNT", Layer="MAC", Mode="ONCE", Duration  = 5)\n
        ----------------------
        """  
        connId = self.connId
        error = kwargs.get('Error', None)
        layer = kwargs.get('Layer', None)
        duration = kwargs.get('Duration', 5)
        mode = kwargs.get('Mode', "CONT")
        activeErrorFrames = kwargs.get('ActiveErrorFrames', 0)
        inactiveErrorFrames = kwargs.get('InactiveErrorFrames', 0)
        rate = kwargs.get('Rate', None)
        keys = [k for k, v in connsdb.items() if connId in v]
        result = self.ssh[connId].insertError(keys[0],Error=error,Mode=mode,Layer=layer,Duration = duration , \
                            ActErrorFrame = activeErrorFrames,InactErrorFrame = inactiveErrorFrames,Rate = rate) 
        return result

    def getAlarms(self, **kwargs):
        """
        ----------------------
            getAlarms()
        
        Method to get the alarms present at  a specific layer \
        For this release it's only for 100GbE alarms retrieval\
        This means any alarms on PHYS or PCS or MAC layer alarms\
        - method only for ONT-602

            Parameters:
            : logger_handle -> testset handle name  -> string
            : Layer -> Layer at which alarm is inserted  -> string
                            options :
                                PHYS # This is the Phy layer alarms
                                OTL  # This is the OTL layer alarms
                                OTN  # This is the OTN layer alarms
                                PCS  # this is the PCS layer alarms
                                MAC  # This is the MAC layer alarms

        **Example :** 

            getAlarms(Layer="PHYS")\n
            getAlarms(Layer="PCS")\n
            getAlarms(Layer="MAC")\n

        ----------------------
        """  
        connId = self.connId
        layer = kwargs.get('Layer', None)
        keys = [k for k, v in connsdb.items() if connId in v]
        result = self.ssh[connId].getLayerAlarms(keys[0],Layer=layer) 
        return result
        
    def _grpc_capabilities (self,**kwargs):
        """
        ----------------------
            grpc_capabilities()
        
        Method to GET the gRPC capabilities of an NE. 
            
            Parameters:
            None
        **Example :** 

            conns['grpc'].grpc_capabilities()
        ----
        """
        sut = kwargs.get('sut', None)
        try:
            connId = self.connId
            cmd = 'gRPC_capabilities'
            interface = "GRPC" #InterfaceType.GRPC.value
            operation_method = 'gRPC_capabilities'
            driver_method = 'capabilities'
            driver_method_args_dict = {}
            return self._execute_cmd(sut= sut, cmd=cmd, toVerify=None, interface=interface,
                                    operation_method=operation_method, driver_method=driver_method,
                                    driver_method_args_dict=driver_method_args_dict)
        except Exception as e:
            # logger.error(e)
            keys = [k for k, v in connsdb.items() if connId in v]
            plogger.error_log(handle =keys[0],msg = e )

    def __create_dict(self,*args):
        return dict({i:eval(i) for i in args})

    def grpc_subscribe(self,**kwargs):
        """
        ----------------------
            grpc_subscribe(path = <path namespace>, sample_interval = <sample interval>,hearbeat_interval = <heartbeat interval>, subscription_mode = <subscriptiong mode>,mode = <streaming mode>)
        
        Method to create the gRPC subscription of an object.  Used to do the PM /Alarm telemetry. 
            
            Parameters:
            : path                  -> string (e.g. '/pm/real-time-pm-data/real-time-pm[AID=1-PEM-1][parameter=temperature]')
            : sample_interval       : Sample interval in nanoseconds  -> int (e.g. 10000000000)
            : hearbeat_interval     : Hearbeat interval in nanoseconds-> int (e.g. 30000000000)
            : subscription_mode -> string ()
                            options :
                                TARGET_DEFINED # The target selects the relevant mode for each element.
                                ON_CHANGE      # The target sends an update on element value change.
                                SAMPLE         # The target samples values according to the interval.
            : mode        -> string
                            options:
                                STREAM  # stream the subscription
                                ONCE    # once only
                                POLL    # poll certain
            : filename        -> string
        **Example :**
            conns['grpc'].grpc_subscribe(path  = '/pm/real-time-pm-data/real-time-pm[AID=1-PEM-1][parameter=temperature]', sample_interval = 10000000000, hearbeat_interval = 30000000000, subscription_mode = 'sample',mode = 'once')
        ----
        """
        sut = kwargs.get('sut', None)
        local_sut = kwargs.get('local_sut', None)
        subs_list = []
        path = str(kwargs.get('path', None))
        local = False
        if local_sut:
            sut = local_sut
            local = True
        subscription_mode = kwargs.get('subscription_mode', None)
        sample_interval =  kwargs.get('sample_interval', 5000000000)
        heartbeat_interval =  kwargs.get('heartbeat_interval', 0)
        filename =  kwargs.get('filename', None)
        mode = kwargs.get('mode', 'once')
        setup_parameters = pixi.get_setupEnvironment(sut = sut, option = 'Interface', local = local)
        print (setup_parameters)
        file_path_abs = setup_parameters ['gRPCSubscriptionLogPath']
        filepath = os.path.join(file_path_abs,filename)
        # subs_vars1 = ["path", "subscription_mode","sample_interval","heartbeat_interval"]
        # create_dict = {i:eval(i) for i in subs_vars1}
        # create_dict = lambda *args: {i:eval(i) for i in args}
        inner_dict = {'path': path,
                      'mode': subscription_mode,
                      'sample_interval': sample_interval,
                      'heartbeat_interval': heartbeat_interval}
        subs_list.append(inner_dict)
        subscribe_config = {
            'subscription': subs_list,
            'use_aliases': True,
            'mode': mode,
            'encoding': 'json_ietf',
            'filepath': filepath
        }
        self._create_subscription(sut = sut, subscription_list=subscribe_config)
            # df.to_csv("pm-subscription.csv", sep=',', mode='a',header=False,encoding='utf-8')
        # df1 = pd.read_csv('pm-subscription_plot.csv')
        return True

    def gnmi_get(self,**kwargs):
        """
        ----------------------
            gnmi_get(sut = <sut>,path = <path namespace>, sample_interval = <sample interval>,hearbeat_interval = <heartbeat interval>, subscription_mode = <subscriptiong mode>,mode = <streaming mode>)
        
        Method to create the gRPC subscription of an object.  Used to do the PM /Alarm telemetry. 
            
            Parameters:
            : path                  -> list (e.g. ['openconfig:/terminal-device/','openconfig:/components/component[name=card-1-PEM-1]/properties/property[name=admin-state]/config/value'])
            : data_type       : Sample interval in nanoseconds  -> int (e.g. 10000000000)

        **Example :**
            conns['grpc'].gnmi_get(path = '/pm/real-time-pm-data/real-time-pm[AID=1-PEM-1][parameter=temperature]', data_type = 'config')
        ----
        """
        # paths = str(kwargs.get('path', None))
        paths= re.findall (r"([\w.:/\[\]\-=]+)",str(kwargs.get('path', None)))
        data_type = str(kwargs.get('data_type', None))
        # setup_parameters = self._get_setupEnvironment(sut = sut,option = 'Interface')
        # override = setup_parameters ['OverrideParameter']
        result = self._gRPC_get_request (paths = paths,data_type = data_type)
        return result

    def gnmi_set(self,**kwargs):
        """
        ----------------------
            gnmi_set(sut = <sut>,path = <path namespace>, sample_interval = <sample interval>,hearbeat_interval = <heartbeat interval>, subscription_mode = <subscriptiong mode>,mode = <streaming mode>)
        
        Method to create the gRPC subscription of an object.  Used to do the PM /Alarm telemetry. 
            
            Parameters:
            : path                  -> list (e.g. ['openconfig:/terminal-device/','openconfig:/components/component[name=card-1-PEM-1]/properties/property[name=admin-state]/config/value'])
            : data_type       : Sample interval in nanoseconds  -> int (e.g. 10000000000)

        **Example :**
            conns['grpc'].gnmi_set(sut = 'LabSim',path  = '/pm/real-time-pm-data/real-time-pm[AID=1-PEM-1][parameter=temperature]', data_type = 'config')
        ----
        """
        sut = kwargs.get('sut', None)
        # paths = str(kwargs.get('path', None))
        conf_data = kwargs.get('conf_data', None)
        json_file = kwargs.get('json_file', None)
        setup_parameters = self._get_setupEnvironment(sut = sut,option = 'Interface')
        file_path_abs = setup_parameters ['gRPCSetDataFilePath']
        filepath = os.path.join(file_path_abs,json_file)
        new_data = []
        f = open(filepath)
        data = json.load(f)
        f.close()
        for items in data[conf_data]:
            new_data.append(tuple(items))

        response = self._gRPC_set_request (conf_data = new_data)
        # return True

        return response

    def gnmi_delete(self,**kwargs):
        """
        ----------------------
            gnmi_delete(path = <path namespace>, sample_interval = <sample interval>,hearbeat_interval = <heartbeat interval>, subscription_mode = <subscriptiong mode>,mode = <streaming mode>)

        Method to create the gRPC subscription of an object.  Used to do the PM /Alarm telemetry. 
            
            Parameters:
            : path                  -> list (e.g. ['openconfig:/terminal-device/','openconfig:/components/component[name=card-1-PEM-1]/properties/property[name=admin-state]/config/value'])
            : data_type       : Sample interval in nanoseconds  -> int (e.g. 10000000000)

        **Example :**
            conns['grpc'].gnmi_set(path  = '/pm/real-time-pm-data/real-time-pm[AID=1-PEM-1][parameter=temperature]', data_type = 'config')
        ----
        """

        sut = kwargs.get('sut', None)
        paths= re.findall (r"([\w.:/\[\]\-=]+)",str(kwargs.get('path', None)))
        result = self._gRPC_delete_request (paths = paths)
        return result

    def gnmi_direct_set(self, **kwargs):
        """
        ----------------------
            gnmi_direct_set(sut = <sut>, conf_data = <python data structure to set via gNMI>)
        
        Method to pass in a block of data to set via gRPC gNMI, as opposed to pointing to that data in a JSON file
            
            Parameters:
            : conf_data       : list of xpath keypairs to set via gNMI

        **Example :**
            rslt = vsh.conns[handle].gnmi_direct_set(conf_data = set_data)
        ----
        """
        conf_data = kwargs.get('conf_data', None)
        new_data = []
        for items in conf_data:
            new_data.append(tuple(items))

        response = self._gRPC_set_request (conf_data = new_data)

        return response

    def _gRPC_delete_request(self, paths=None):
        connId = self.connId
        driver_method_args_dict = {'path': paths                                
                                   }  
        cmd = 'gnmi_delete' 
        interface = 'GRPC'
        operation_method = 'gnmi_delete'
        driver_method = 'gnmi_delete'
        msg = " Input Command    : {} \n gRPC SET config   : {}  ".format(cmd,pformat(driver_method_args_dict))
        keys = [k for k, v in connsdb.items() if connId in v]
        plogger.info_log(handle =keys[0],msg = msg )
        return self._execute_cmd(cmd=cmd, interface=interface, operation_method=operation_method, 
                       driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)

    def _gRPC_get_request(self, paths=None, data_type = 'all'):
        connId = self.connId
        cmd = 'gnmi_get' 
        interface = 'GRPC'
        operation_method = 'gnmi_get'
        driver_method = 'gnmi_get'
        driver_method_args_dict = {'path': paths,
                                   'data_type': data_type
                                   }
        msg = " Input Command    : {} \n gRPC GET  : {}  ".format(cmd,pformat(driver_method_args_dict))
        keys = [k for k, v in connsdb.items() if connId in v]
        plogger.info_log(handle =keys[0],msg = msg )
        return self._execute_cmd(cmd=cmd, interface=interface, operation_method=operation_method, 
                       driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)

    def _gRPC_set_request(self, conf_data=None):
        connId = self.connId
        cmd = 'gnmi_set' 
        interface = 'GRPC'
        operation_method = 'gnmi_set'
        driver_method = 'gnmi_set'
        driver_method_args_dict = {'conf_data': conf_data,
                                   }
        msg = " Input Command    : {} \n gRPC SET config   : {}  ".format(cmd,pformat(driver_method_args_dict))
        keys = [k for k, v in connsdb.items() if connId in v]
        plogger.info_log(handle =keys[0],msg = msg )
        return self._execute_cmd(cmd=cmd, interface=interface, operation_method=operation_method, 
                       driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)

    def _gRPC_subscribe(self, conf_data=None):
        connId = self.connId
        cmd = 'gnmi_subscribe' 
        interface = 'GRPC'
        operation_method = 'gnmi_subscribe'
        driver_method = 'gnmi_subscribe'
        driver_method_args_dict = conf_data
        msg = " Input Command    : {} \n gRPC SET config   : {}  ".format(cmd,pformat(driver_method_args_dict))
        keys = [k for k, v in connsdb.items() if connId in v]
        plogger.info_log(handle =keys[0],msg = msg )

        return self._execute_cmd(cmd=cmd, interface=interface, operation_method=operation_method, 
                       driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)

    def _create_subscription(self,sut, subscription_list=None,**kwargs):
        connId = self.connId
        cmd = 'create_subscription'
        interface = "GRPC" #InterfaceType.GRPC.value
        operation_method = 'create_subscription'
        driver_method = 'subscription'
        driver_method_args_dict = subscription_list
        msg = " Input Command    : {} \n Subscription summary    : {}  ".format(cmd,pformat(driver_method_args_dict))
        keys = [k for k, v in connsdb.items() if connId in v]
        plogger.info_log(handle =keys[0],msg = msg )
        return self._execute_cmd(sut=sut, cmd=cmd, interface=interface, operation_method=operation_method, 
                       driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)

    def _get_raw_requests (self,**kwargs):
        raw_data = kwargs.get('raw_data', None)
        print('{}\n{}\r\n{}\r\n\r\n{}'.format(
            '-----------START-----------',
            raw_data.method + ' ' + raw_data.url,
            '\r\n'.join('{}: {}'.format(k, v) for k, v in raw_data.headers.items()),
            raw_data.body,
        ))
        return

    def _is_valid_uuid(self, uuid_str):
        match = re.match('\w{8}\-\w{4}\-\w{4}\-\w{4}\-\w{12}', uuid_str)
        rslt = True if match else False
        return rslt
        
    def _execute_cmd(self,**kwargs):
        if self.ssh == {}:
            print("Please connect first")
            return 0
        else : 
            facilities = ['odu','optical-carrier','super-channel']
            connId = self.connId
            keys = [k for k, v in connsdb.items() if connId in v]
            driver_method_args_dict = kwargs.get('driver_method_args_dict',None)
            response = False
            pQueue = pixi.PIXIQueue()
            # result = ''
            try:
                if kwargs['interface'] == "GRPC":
                    # gc = self._netConnector (protocol = 'grpc',sut =  kwargs.get('sut', None))
                    # print (gc)
                    if kwargs.get('driver_method',None) == 'subscription':
                        print (driver_method_args_dict)
                        filepath = driver_method_args_dict['filepath']
                        # _f_handler = open(filepath, "w")
                        driver_method_args_dict.pop('filepath', None)
                        if driver_method_args_dict['mode'] == 'once':
                            ''' 
                            the below commented lines were original revert if try - finally code block has issues
                            '''
                            # telemetry_stream = self.ssh[connId].subscribe(subscribe=driver_method_args_dict)
                            # telemetry_entry = telemetry_stream.__next__()
                            # tele_data = json.dumps(telemetryParser(telemetry_entry)["update"], indent=4, sort_keys=True)
                            temporarydata = []
                            try:
                                telemetry_stream = self.ssh[connId].subscribe(subscribe=driver_method_args_dict)
                                while True:
                                    try:
                                        telemetry_entry = telemetry_stream.next()
                                        print(telemetryParser(telemetry_entry))
                                        temporarydata.append(telemetryParser(telemetry_entry)["update"])
                                    except Exception as e:
                                        break

                            finally:
                                print ("ONCE DONE!")
                                # self.ssh[connId].close()
                            tele_data = json.dumps(temporarydata, indent=4, sort_keys=True)
                            self.Tn.insert(tkinter.END, 40*"-" +"\n")
                            # keys = [k for k, v in connsdb.items() if connId in v]
                            plogger.debug_log(handle = keys[0],msg = " >> received message : " + tele_data )
                            with open(filepath, 'a') as _f_handler:
                                for line in tele_data:
                                    self.Tn.insert(tkinter.END, line)
                                    _f_handler.write(line) 
                            self.Tn.insert(tkinter.END, "\n"+40*"-" +"\n")
                            # df = pd.json_normalize((telemetryParser(telemetry_entry))["update"]["update"])
                            # df.to_csv("pm-subscription.csv", sep=',', mode='a',header=False,encoding='utf-8')
                        elif driver_method_args_dict['mode'] == 'stream':
                            telemetry_stream = self.ssh[connId].subscribe2(subscribe=driver_method_args_dict)
                            pPool = pixi.PIXIPool()
                            def watch_telemetry(stream):
                                for telemetry_entry in stream:
                                    myPool = pixi.PIXIPool()
                                    if myPool.cancel:
                                        break
                                    tele_data = json.dumps(telemetry_entry["update"], indent=4, sort_keys=True)
                                    plogger.debug_log(handle = keys[0],msg = " >> received message : " + tele_data )
                                    pQueue.put({"command": "log_inbound", "data": {"handle": self.handle, "text": tele_data + "\n"}})
                                    with open(filepath, 'a') as _f_handler:
                                        _f_handler.write(tele_data) 
                            try:
                                pPool.submit(watch_telemetry, telemetry_stream)
                            except RuntimeError as ex:
                                return f"Error: {ex}"
                        # _f_handler.close()
                    if kwargs.get('driver_method',None) == 'capabilities':
                        result = self.ssh[connId].capabilities()
                        print(json.dumps(result, indent=4, sort_keys=True))
                        return result
                    # self.ssh[connId].close()
                    if kwargs.get('driver_method', None) == 'gnmi_subscribe':
                        '''
                        Example subscription data for gNMI:
                            {
                                'subscription': [
                                    {
                                        'path': '/ne/equipment/card[name=*]/admin-state',
                                        'mode': 'ON_CHANGE',
                                        'sample_interval': 10000000000
                                    }
                                ],
                                'use_aliases': True,
                                'mode': 'stream',
                                'encoding': 'json'
                            }
                        '''
                        telemetry_stream = self.ssh[connId].subscribe2(subscribe=driver_method_args_dict)
                        return telemetry_stream
                        
                    if kwargs.get('driver_method',None) == 'gnmi_get':
                        if driver_method_args_dict['data_type'] is not None:
                            pQueue.put({"command": "log_outbound", "data": {"handle": self.handle, "text": f"GET: {driver_method_args_dict['path']}\n"}})
                            plogger.info_log(handle = keys[0],msg = f" >> get requested for : {driver_method_args_dict['path']}")
                            try:
                                get_resp = self.ssh[connId].get(path = driver_method_args_dict['path'],datatype=driver_method_args_dict['data_type'],encoding = 'json')
                                get_resp_data = json.dumps(get_resp, indent=4, sort_keys=True)
                                plogger.info_log(handle = keys[0],msg = " >> received message : " + get_resp_data )
                                pQueue.put({"command": "log_inbound", "data": {"handle": self.handle, "text": get_resp_data + '\n'}})
                                response = get_resp
                            except Exception as ex:
                                pQueue.put({"command": "log_inbound", "data": {"handle": self.handle, "text": str(ex) + '\n'}})
                                plogger.info_log(handle = keys[0], msg = " >> Error received :\n{}".format(str(ex)))
                                return f"Error: {str(ex)}"

                    if kwargs.get('driver_method',None) == 'gnmi_set':
                        log_data = json.dumps(driver_method_args_dict['conf_data'], indent=4)
                        pQueue.put({"command": "log_outbound", "data": {"handle": self.handle, "text": f"SET: \n{log_data}\n"}})
                        plogger.info_log(handle = keys[0],msg = f" >> update requested for : {log_data}")
                        try:
                            _resp = self.ssh[connId].set(update = driver_method_args_dict['conf_data'],encoding = 'json_ietf')
                            get_resp_data = json.dumps(_resp, indent=4, sort_keys=True)
                            pQueue.put({"command": "log_inbound", "data": {"handle": self.handle, "text": get_resp_data + '\n'}})
                            plogger.info_log(handle = keys[0],msg = " >> received message : " + get_resp_data )
                            response = _resp
                        except Exception as ex:
                            pQueue.put({"command": "log_inbound", "data": {"handle": self.handle, "text": str(ex) + '\n'}})
                            plogger.info_log(handle = keys[0], msg = " >> Error received :\n{}".format(str(ex)))
                            return f"Error: {str(ex)}"

                    if kwargs.get('driver_method',None) == 'gnmi_delete':
                        pQueue.put({"command": "log_outbound", "data": {"handle": self.handle, "text": f"DELETE: \n{driver_method_args_dict['path']}\n"}})
                        plogger.info_log(handle = keys[0],msg = f" >> delete requested for : {driver_method_args_dict['path']}")
                        try:
                            _resp = self.ssh[connId].set(delete = driver_method_args_dict['path'],encoding = 'json_ietf')
                            get_resp_data = json.dumps(_resp, indent=4, sort_keys=True)
                            pQueue.put({"command": "log_inbound", "data": {"handle": self.handle, "text": get_resp_data + '\n'}})
                            plogger.debug_log(handle = keys[0],msg = " >> received message : " + get_resp_data )
                            response = _resp
                        except Exception as ex:
                            pQueue.put({"command": "log_inbound", "data": {"handle": self.handle, "text": str(ex) + '\n'}})
                            plogger.info_log(handle = keys[0], msg = " >> Error received :\n{}".format(str(ex)))
                            return f"Error: {str(ex)}"

                if kwargs['interface'] == "RESTCONF":
                    if kwargs.get('driver_method', None) == 'restconf_yang_execute_xr':
                        log_str = f"Method: {driver_method_args_dict['method']}\n"
                        log_str += f"URL: {driver_method_args_dict['url']}\n"
                        if driver_method_args_dict.get('body', None):
                            body = driver_method_args_dict['body']
                            json_str = json.dumps(body, indent=4)
                            log_str += json_str + '\n'
                        pQueue.put({"command": "log_outbound", "data": {"handle": self.handle, "text": log_str}})
                        plogger.info_log(handle = keys[0],msg = " >> message sent :\n{}".format(log_str))
                        response = self.ssh[connId].request(
                            method = driver_method_args_dict['method'],
                            url = driver_method_args_dict['url'],
                            json = driver_method_args_dict.get('body', None),
                            verify=False
                        )
                        if 'application/json' in response.headers.get('Content-Type', ''):
                            json_response = response.json()
                            response_text = json.dumps(json_response, indent=4)
                        else:
                            response_text = response.text
                        plogger.info_log(handle = keys[0], msg = f"<< Response Code {response.status_code}")
                        plogger.info_log(handle = keys[0], msg = " << reply received :\n{}".format(response_text))
                        log_str = f"Response Code {response.status_code}\n"
                        log_str += response_text + '\n'
                        pQueue.put({"command": "log_inbound", "data": {"handle": self.handle, "text": log_str}})

                    if kwargs.get('driver_method', None) == 'restconf_yang_execute_gx':
                        log_str = f"Method: {driver_method_args_dict['method']}\n"
                        log_str += f"URL: {driver_method_args_dict['url']}\n"
                        if driver_method_args_dict.get('body', None):
                            body = driver_method_args_dict['body']
                            json_str = json.dumps(body, indent=4)
                            log_str += json_str + '\n'
                        pQueue.put({"command": "log_outbound", "data": {"handle": self.handle, "text": log_str}})
                        plogger.info_log(handle = keys[0],msg = " >> message sent :\n{}".format(log_str))
                        response = self.ssh[connId].request(
                            method = driver_method_args_dict['method'],
                            url = driver_method_args_dict['url'],
                            json = driver_method_args_dict.get('body', None),
                            verify=False
                        )
                        if 'application/json' in response.headers.get('Content-Type', ''):
                            json_response = response.json()
                            response_text = json.dumps(json_response, indent=4)
                        else:
                            response_text = response.text
                        plogger.info_log(handle = keys[0], msg = f"<< Response Code {response.status_code}")
                        plogger.info_log(handle = keys[0], msg = " << reply received :\n{}".format(response_text))
                        log_str = f"Response Code {response.status_code}"
                        log_str += response_text + '\n'
                        pQueue.put({"command": "log_inbound", "data": {"handle": self.handle, "text": log_str}})

                    if kwargs.get('driver_method', None) == 'restconf_yang_subscribe_xr':
                        json_str = json.dumps(driver_method_args_dict['body'], indent=4)
                        log_str = f"Method: {driver_method_args_dict['method']}\n"
                        log_str += f"URL: {driver_method_args_dict['url']}\n"
                        log_str += json_str + '\n'
                        pQueue.put({"command": "log_outbound", "data": {"handle": self.handle, "text": log_str}})
                        response = self.ssh[connId].request(
                            method = 'POST',
                            url = driver_method_args_dict['url'],
                            json = driver_method_args_dict['body'],
                            verify = False
                        )
                        if 'application/json' in response.headers.get('Content-Type', ''):
                            json_response = response.json()
                            response_text = json.dumps(json_response, indent=4)
                        else:
                            response_text = response.text
                        plogger.info_log(handle = keys[0], msg = " >> reply received :\n{}".format(response_text))
                        log_str = f"Response Code {response.status_code}"
                        log_str += response_text + '\n'
                        pQueue.put({"command": "log_inbound", "data": {"handle": self.handle, "text": log_str}})

                    setup_parameters = self._get_setupEnvironment(sut = kwargs.get('sut', None),option = 'Login')
                    if kwargs.get('driver_method', None) == 'restconf_yang_execute_g40':
                        username = setup_parameters ['UserName']
                        password = setup_parameters ['Password']
                        server_ip = setup_parameters ['IpAddress']
                        conf_data = driver_method_args_dict['conf_data']
                        headers = {'Accept': 'application/yang-data+json'}
                        uri = "https://" + server_ip + ":8181" + conf_data['path']
                        if 'body' in conf_data:
                            print(f"Sending:\n{conf_data['method']} {uri}\n{headers}\n{json.dumps(conf_data['body'])}")
                            response = self.ssh[connId].request(
                                conf_data['method'], uri,
                                auth=HTTPBasicAuth(username, password),
                                headers=headers, data=json.dumps(conf_data['body']),
                                verify=False
                            )
                        else:
                            print(f"Sending:\n{conf_data['method']} {uri}\n{headers}")
                            response = self.ssh[connId].request(
                                conf_data['method'], uri,
                                auth=HTTPBasicAuth(username, password),
                                headers=headers,
                                verify=False
                            )
                        plogger.debug_log(handle = keys[0],msg = " >> received message : " + response.text )
                        self.Tn.insert(tkinter.END, 40*"-" +"\n")
                        for get_resp_lines in response.text:
                            self.Tn.insert(tkinter.END, get_resp_lines)
                        self.Tn.insert(tkinter.END, "\n"+40*"-" +"\n")

                    if kwargs.get('driver_method', None) == 'restconf_yang_get_g40':
                        username = setup_parameters ['UserName']
                        password = setup_parameters ['Password']
                        server_ip = setup_parameters ['IpAddress']
                        path = driver_method_args_dict['path']
                        headers = {'Accept': 'application/yang-data+json'}
                        uri = "https://" + server_ip + ":8181" + path
                        response = self.ssh[connId].get(uri, auth=HTTPBasicAuth(username, password), headers=headers, verify=False)
                        print(response.json())

                    if kwargs['operation_method'] == 'restconf_get' and  kwargs['driver_method'] == 'restconf_get_g40':
                        # requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        # keys = [k for k, v in connsdb.items() if connId in v]
                        response = ''
                        username = setup_parameters ['UserName']
                        password = setup_parameters ['Password']
                        server_ip = setup_parameters ['IpAddress']
                        object = driver_method_args_dict["object"]
                        name = driver_method_args_dict["name"]
                        query = driver_method_args_dict["query"]
                        filter = driver_method_args_dict["filter"]
                        headers = {'Accept': 'application/yang-data+json'}
                        data = self._fetch_uri(object = object,server_Ip = server_ip , username = username , password = password)
                        print(f"Data: {data}")
                        uri = re.findall(r"/rest.*", data)
                        uri = "https://" + server_ip + ":8181" + uri[0]
                        uri  = str(uri).strip()
                        # req = requests.Request('GET',uri,headers=headers)
                        # self._get_raw_requests(raw_data=req.prepare())
                        plogger.info_log(handle = keys[0],msg = " >> send message :  \n\t Method : 'GET' \n\t URL : {} ".format(uri))
                        response = self.ssh[connId].get(uri,  auth=HTTPBasicAuth(username, password),headers=headers,verify=False)
                        jsondata = json.loads(response.text)
                        data = json.dumps(jsondata, indent=2)
                        self.Tn.insert(tkinter.END, 40*"-" +"\n")  
                        plogger.debug_log(handle = keys[0],msg = " >> received message : " + data )
                        for line in data:
                            self.Tn.insert(tkinter.END, line)
                        self.Tn.insert(tkinter.END, "\n"+40*"-" +"\n")
                    
                    if kwargs['operation_method'] == 'restconf_get' and  kwargs['driver_method'] == 'restconf_get_g40':
                        # requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        # keys = [k for k, v in connsdb.items() if connId in v]
                        response = ''
                        username = setup_parameters ['UserName']
                        password = setup_parameters ['Password']
                        server_ip = setup_parameters ['IpAddress']
                        object = driver_method_args_dict["object"]
                        name = driver_method_args_dict["name"]
                        query = driver_method_args_dict["query"]
                        filter = driver_method_args_dict["filter"]
                        headers = {'Accept': 'application/yang-data+json'}
                        data = self._fetch_uri(object = object,server_Ip = server_ip , username = username , password = password)
                        uri = re.findall(r"/rest.*", data)
                        uri = "https://" + server_ip + ":8181" + uri[0]
                        uri  = str(uri).strip()
                        # req = requests.Request('GET',uri,headers=headers)
                        # self._get_raw_requests(raw_data=req.prepare())
                        plogger.info_log(handle = keys[0],msg = " >> send message :  \n\t Method : 'GET' \n\t URL : {} ".format(uri))
                        response = self.ssh[connId].get(uri,  auth=HTTPBasicAuth(username, password),headers=headers,verify=False)
                        jsondata = json.loads(response.text)
                        data = json.dumps(jsondata, indent=2)
                        self.Tn.insert(tkinter.END, 40*"-" +"\n")  
                        plogger.debug_log(handle = keys[0],msg = " >> received message : " + data )
                        for line in data:
                            self.Tn.insert(tkinter.END, line)
                        self.Tn.insert(tkinter.END, "\n"+40*"-" +"\n")
                    
                    if kwargs['operation_method'] == 'restconf_get' and  kwargs['driver_method'] == 'restconf_get_xr':
                        # requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        
                        token = driver_method_args_dict["token"]
                        object = driver_method_args_dict["object"]
                        name = driver_method_args_dict["name"]
                        query = driver_method_args_dict["query"]
                        filter = driver_method_args_dict["filter"]
                        headers = {'Content-Type': 'application/json'}
                        if self._connDict['xr_version'] == '0.7':
                            headers['Authorization'] = f'Bearer {token}'
                        else:
                            headers['apikey'] = token
                        
                        server_ip = setup_parameters ['IpAddress']
                        # print (name)
                        ## START - move this piece to env / data structure 
                        uri = self._fetch_xr_uri(object, server_ip, name)

                        if object == "network-connection":
                            if self._connDict['xr_version'] == '0.7':
                                lookup_uri = 'https://' + server_ip + "/api/v1/ncs/network-connections/?content=all"
                            else:
                                lookup_uri = 'https://' + server_ip + "/api/v1/network-connections/?content=all"
                            conn_uri = name
                            if not self._is_valid_uuid(conn_uri):
                                response = self.ssh[connId].get('https://' + server_ip + "/api/v1/network-connections/?content=all",headers=headers,verify=False)
                                for elem in response.json():
                                    if "name" in elem["config"]:
                                        if elem["config"]["name"] == name:
                                            conn_uri = elem["id"]
                                            break
                            uri = uri + conn_uri

                                
                        if query == "expanded":
                            uri = uri + '?content=expanded'
                        if query == "all":
                            uri = uri + '?content=all'
                        ## END
                        # uri = '/api/v1/hms/hosts?content=expanded' # change it to uri
                        uri = 'https://' + server_ip + uri
                        plogger.info_log(handle = keys[0],msg = " >> send message :  \n\t Method : 'GET' \n\t URL : {}".format(uri))
                        response = self.ssh[connId].get(uri,headers=headers,verify=False) 
                        jsondata = json.loads(response.text)
                        data = json.dumps(jsondata, indent=2)
                        if len(filter) :
                            for item in filter:
                                if item == "hosts_list":
                                    hostdata = {}
                                    hostcount = 0
                                    
                                    for key in jsondata :
                                        host_mem = "host"+str(hostcount)
                                        host = key['id']
                                        hostdata[host_mem] = host
                                        hostcount += 1
                                    data = json.dumps(hostdata, indent = 2) 
                                    response = hostdata
                                if item == "ports_list":
                                    portdata = {}
                                    hostcount = 0
                                    
                                    for key in jsondata :
                                        port_mem = key['state']['moduleIf']['clientIfAid']
                                        port = key['id']
                                        portdata[port_mem] = port
                                    data = json.dumps(portdata, indent = 2) 
                                    response = portdata
                        self.Tn.insert(tkinter.END, 40*"-" +"\n")
                        # keys = [k for k, v in connsdb.items() if connId in v]
                        plogger.debug_log(handle = keys[0],msg = " >> received message : " + data )
                        for line in data:
                            self.Tn.insert(tkinter.END, line)
                        self.Tn.insert(tkinter.END, "\n"+40*"-" +"\n")
                        
                    if kwargs['operation_method'] == 'restconf_post' and  kwargs['driver_method'] == 'restconf_get_xr':
                        if kwargs['cmd']== 'xr_create_link':
                            token = driver_method_args_dict["token"]
                            object = driver_method_args_dict["object"]
                            name = driver_method_args_dict["name"]
                            # label = driver_method_args_dict["label"]
                            src_type = driver_method_args_dict["src_type"]
                            src_parameter = driver_method_args_dict["src_val"]
                            dst_type = driver_method_args_dict["dst_type"]
                            dst_parameter = driver_method_args_dict["dst_val"]
                            print (driver_method_args_dict)
                            headers = {'Content-Type': 'application/json'}
                            if self._connDict['xr_version'] == '0.7':
                                headers['Authorization'] = f'Bearer {token}'
                            else:
                                headers['apikey'] = token
                            server_ip = setup_parameters ['IpAddress']
                            d1 = dict()
                            # XR 0.7 removes the 'config' object, i.e. d1[0]["config"]["name"] -> d1[0]["name"] 
                            if self._connDict['xr_version'] == '0.7':
                                with open("libs/ref_libs/json/create_network_connection.json", 'r') as jsfile:
                                    d1 = json.load(jsfile)
                                    d1[0]["name"] = name
                            elif self._connDict['xr_version'] == '0.5':
                                with open("libs/ref_libs/json/create_network_connection_0.5.json", 'r') as jsfile:
                                    d1 = json.load(jsfile)
                                    d1[0]["config"]["name"] = name
                            d2 = d1
                            # d1[0]["config"]["labels"] = {'key1': 'label'}
                            d2[0]["endpoints"][0]["selector"]= defaultdict(dict)
                            d2[0]["endpoints"][1]["selector"] = defaultdict(dict)
                            for key,val in src_parameter.items():
                                d2[0]["endpoints"][0]["selector"]["moduleIfSelectorBy"+src_type][key] = val
        
                            for key,val in dst_parameter.items():
                                d2[0]["endpoints"][1]["selector"]["moduleIfSelectorBy"+dst_type][key] = val
    
                            d1[0]["endpoints"][0]["selector"]= {k: dict(v) for k, v in d2[0]["endpoints"][0]["selector"].items()}
                            d1[0]["endpoints"][1]["selector"]= {k: dict(v) for k, v in d2[0]["endpoints"][1]["selector"].items()}

                            uri = "https://"+server_ip + "/api/v1/network-connections"
                            # plogger.info_log(handle = keys[0],msg = " >> send message : " + uri )

                            response = self.ssh[connId].request("POST", uri, headers=headers, data=json.dumps(d1))
                            plogger.info_log(handle = keys[0],msg = " >> send message :  \n\t Method : 'POST' \n\t URL : {} \n\t  Body : {}".format(uri, response.request.body))
                            jsondata = json.loads(response.text)
                            data = json.dumps(jsondata, indent = 2)
                            self.Tn.insert(tkinter.END, 40*"-" +"\n")
                            # keys = [k for k, v in connsdb.items() if connId in v]

                            plogger.debug_log(handle = keys[0],msg = " >> received message : " + data )
                            for line in data:
                                self.Tn.insert(tkinter.END, line)
                            self.Tn.insert(tkinter.END, "\n"+40*"-" +"\n")
                    
                if kwargs['interface'] == "NETCONF":

                    if kwargs.get('driver_method', None) == 'netconf_yang_execute_g40':
                        xml_data = xmltodict.unparse(driver_method_args_dict['conf_data'], pretty=True)
                        plogger.info_log(handle = keys[0],msg = " >> message sent :\n{}".format(xml_data))
                        pQueue.put({"command": "log_outbound", "data": {"handle": self.handle, "text": xml_data}})
                        try:
                            xml_data = xml_data.replace("?>", " standalone=\"yes\"?>")
                            result = self.ssh[connId].edit_config(target='running', config=xml_data).xml
                            plogger.info_log(handle = keys[0], msg = " >> reply received :\n{}".format(result))
                            pQueue.put({"command": "log_inbound", "data": {"handle": self.handle, "text": result}})
                            dict_result = xmltodict.parse(result, xml_attribs=False)
                            if 'rpc-reply' in dict_result:
                                dict_result = dict_result['rpc-reply']
                            return dict_result
                        except RPCError as ex:
                            print(f"Error: {str(ex)}")
                            pQueue.put({"command": "log_inbound", "data": {"handle": self.handle, "text": str(ex)}})
                            plogger.info_log(handle = keys[0], msg = " >> Error received :\n{}".format(str(ex)))
                            return f"Error: {str(ex)}"
                    
                    if kwargs.get('driver_method', None) == 'netconf_yang_rpc_g40':
                        xml_data = xmltodict.unparse(driver_method_args_dict['conf_data'], pretty=True)
                        plogger.info_log(handle = keys[0],msg = " >> message sent :\n{}".format(xml_data))
                        pQueue.put({"command": "log_outbound", "data": {"handle": self.handle, "text": xml_data}})
                        try:
                            result = self.ssh[connId].dispatch(xml_.to_ele(xml_data))
                            plogger.info_log(handle = keys[0], msg = " >> reply received :\n{}".format(result))
                            pQueue.put({"command": "log_outbound", "data": {"handle": self.handle, "text": result}})
                            ret_data = xmltodict.parse(str(result), xml_attribs=False)
                            if 'rpc-reply' in ret_data:
                                ret_data = ret_data['rpc-reply']
                            return(ret_data)
                        except RPCError as ex:
                            print(f"Error: {str(ex)}")
                            plogger.info_log(handle = keys[0], msg = " >> Error received :\n{}".format(str(ex)))
                            return f"Error: {str(ex)}"

                    if kwargs.get('driver_method', None) == 'netconf_yang_get_g40':
                        print(json.dumps(driver_method_args_dict, indent=4))
                        filter_dict = driver_method_args_dict['filter']
                        filter_type = driver_method_args_dict.get('type', 'subtree')
                        xml_data = xmltodict.unparse(filter_dict, pretty=True)
                        plogger.info_log(handle = keys[0],msg = " >> message sent :\n{}".format(xml_data))
                        pQueue.put({"command": "log_outbound", "data": {"handle": self.handle, "text": xml_data}})
                        try:
                            result = self.ssh[connId].get((filter_type, xml_data)).xml
                            plogger.info_log(handle = keys[0], msg = " >> reply received :\n{}".format(result))
                            pQueue.put({"command": "log_inbound", "data": {"handle": self.handle, "text": result}})
                            dict_result = xmltodict.parse(result, xml_attribs=False)
                            if 'rpc-reply' in dict_result and 'data'in dict_result['rpc-reply']:
                                dict_result = dict_result['rpc-reply']['data']
                            return dict_result
                        except RPCError as ex:
                            print(f"Error: {str(ex)}")
                            plogger.info_log(handle = keys[0], msg = " >> Error received :\n{}".format(str(ex)))
                            return f"Error: {str(ex)}"
                    
                    if kwargs.get('driver_method', None) == 'netconf_yang_delete_g40':
                        driver_method_args_dict['filter']['@xmlns:nc'] = "urn:ietf:params:xml:ns:netconf:base:1.0"
                        data = {'nc:config': driver_method_args_dict['filter']}
                        xml_data = xmltodict.unparse(data, pretty=True)
                        plogger.info_log(handle = keys[0],msg = " >> message sent :\n{}".format(xml_data))
                        pQueue.put({"command": "log_outbound", "data": {"handle": self.handle, "text": xml_data}})
                        try:
                            result = self.ssh[connId].edit_config(target='running', config=xml_data)
                            plogger.info_log(handle = keys[0], msg = " >> reply received :\n{}".format(result))
                            pQueue.put({"command": "log_inbound", "data": {"handle": self.handle, "text": result}})
                            return str(result)
                        except RPCError as ex:
                            print(f"Error: {str(ex)}")
                            plogger.info_log(handle = keys[0], msg = " >> Error received :\n{}".format(str(ex)))
                            return f"Error: {str(ex)}"

                    if kwargs.get('driver_method', None) == 'netconf_yang_subscribe_g40':
                        try:
                            stream = driver_method_args_dict.get('stream', None)
                            filter_dict = driver_method_args_dict.get('filter', None)
                            filter_xml = None
                            if filter_dict:
                                filter_xml = xmltodict.unparse(filter_dict, pretty=True)
                            result = self.ssh[connId].create_subscription(stream_name=stream, filter=('subtree', filter_xml))
                            return result
                        except Exception as ex:
                            print(f"Error: {str(ex)}")
                            plogger.info_log(handle = keys[0], msg = " >> Error received :\n{}".format(str(ex)))
                            return f"Error: {str(ex)}"

                    if kwargs.get('driver_method', None) == 'netconf_yang_get_streams_g40':
                        filter_dict = {
                                "netconf": {
                                    "@xmlns": "urn:ietf:params:xml:ns:netmod:notification",
                                    "streams": {}
                                }
                        }
                        xml_data = xmltodict.unparse(filter_dict, pretty=True)
                        plogger.info_log(handle = keys[0],msg = " >> message sent :\n{}".format(xml_data))
                        pQueue.put({"command": "log_outbound", "data": {"handle": self.handle, "text": xml_data}})
                        try:
                            result = self.ssh[connId].get(('subtree', xml_data)).xml
                            plogger.info_log(handle = keys[0], msg = " >> reply received :\n{}".format(result))
                            pQueue.put({"command": "log_inbound", "data": {"handle": self.handle, "text": result}})
                            dict_result = xmltodict.parse(result)
                            if 'rpc-reply' in dict_result and 'data'in dict_result['rpc-reply']:
                                dict_result = dict_result['rpc-reply']['data']
                            return dict_result
                        except RPCError as ex:
                            print(f"Error: {str(ex)}")
                            plogger.info_log(handle = keys[0], msg = " >> Error received :\n{}".format(str(ex)))
                            return f"Error: {str(ex)}"

                    if kwargs.get('driver_method', None) == 'netconf_yang_notification_g40':
                        try:
                            timeout = driver_method_args_dict.get('timeout', 30)
                            block = driver_method_args_dict.get('block', True)
                            result = self.ssh[connId].take_notification(block=block, timeout=timeout)
                            if result:
                                plogger.info_log(handle = keys[0], msg = " >> notification received :\n{}".format(result))
                                pQueue.put({"command": "log_inbound", "data": {"handle": self.handle, "text": result.notification_xml}})
                                result = xmltodict.parse(result.notification_xml)
                            return result
                        except Exception as ex:
                            print(f"Error: {str(ex)}")
                            plogger.info_log(handle = keys[0], msg = " >> Error received :\n{}".format(str(ex)))
                            return f"Error: {str(ex)}"

                    if kwargs['operation_method'] == 'netconf_delete':
                        f = open("libs/ref_libs/xml/netconf_delete.xml", "r")
                        string = f.read()
                        if list(driver_method_args_dict.keys())[0].lower() == 'xcon' :
                            string = string.replace("tag1","services")
                            string = string.replace("tag2","xcon")
                        if list(driver_method_args_dict.keys())[0].lower() in facilities :
                            string = string.replace("tag1","facilities")
                            string = string.replace("tag2",list(driver_method_args_dict.keys())[0].lower())
                        delete_String = re.sub(r'(\>(.*?)\<)','>'+str(list(driver_method_args_dict.values())[0])+'<', string)
                        f.close()
                        plogger.info_log(handle = keys[0],msg = " >> send message : " + delete_String )
                        data = self.ssh[connId].edit_config(target='running', config=delete_String)
                        # logger.info('- %s - Deleted successfully !! ',str(list(driver_method_args_dict.values())[0]))
                        # keys = [k for k, v in connsdb.items() if connId in v]
                        plogger.debug_log(handle = keys[0],msg = {str(list(driver_method_args_dict.values())[0])} +' - Deleted successfully !! ' )
                        plogger.debug_log(handle = keys[0],msg = " >> received message : " + data )
                        return data
                    
                    if kwargs['operation_method'] == 'netconf_get':
                        f = open("libs/ref_libs/xml/get_on_object.xml", "r")
                        string = f.read()
                        if list(driver_method_args_dict.values())[0].lower() != "all":
                            string = string.replace("test",str(list(driver_method_args_dict.values())[0]))
                        else:
                            string = string.replace("<name>test</name>","")
                        if list(driver_method_args_dict.keys())[0].lower() == 'xcon' :
                            string = string.replace("tag1","services")
                            string = string.replace("tag2","xcon")
                        if list(driver_method_args_dict.keys())[0].lower() in facilities :
                            string = string.replace("tag1","facilities")
                            string = string.replace("tag2",list(driver_method_args_dict.keys())[0].lower())
                        f.close()
                        plogger.info_log(handle = keys[0],msg = " >> send message :  \n\t Method : 'GET' \n\t RPC : {}".format(string))
                        data=self.ssh[connId].get(("subtree",string)).data_xml
                        
                        plogger.debug_log(handle = keys[0],msg = " >> received message : " + data )
                        for line in data:
                            self.Tn.insert(tkinter.END, line)
                        return data
                    
                    if kwargs['operation_method'] == 'netconf_get_pm':
                            filename = kwargs.get('saveToFile', None)
                            for key,val in driver_method_args_dict.items():
                                aid =  val['aid'][0]
                                parameter = val['parameter']
                                pm_period = val['pm_period']
                                interval = val['interval']
                            f = open("libs/ref_libs/xml/get_pm.xml", "r")
                            string = f.read()
                            string = string.replace("test",aid)
                            string = string.replace("pmobj",parameter)
                            f.close()
                            pm_period_unit = pm_period[-1]
                            pm_period_val = int(pm_period[:-1])
                            
                            unit_multiplier = {'s' : 1, 'm' : 60 , 'h':3600}
                            actual_period = pm_period_val*unit_multiplier[pm_period_unit]
                            print( pm_period_unit,pm_period_val,actual_period)
                            iterations = int(actual_period/interval)
                            i = 0
                            print( iterations)
                            plogger.info_log(handle = keys[0],msg = " >> send message :  \n\t Method : 'GET' \n\t RPC : {}".format(string))
                            while True:
                                if i != iterations:
                                    print(">>>> interation #{}".format(i))
                                    i += 1
                                    data = self.ssh[connId].get(("subtree",string)).data_xml
                                    xml_file = self._remove_namespace(data)
                                    table = self._get_data_to_table(xml_file)
                                    curr_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                                    table['DateTime'] = curr_time
                                    if filename != None:
                                        if i ==1 :
                                            table.to_csv(filename, sep=',', mode='a',encoding='utf-8')
                                        else:
                                            table.to_csv(filename, sep=',', mode='a',header=False,encoding='utf-8')

                                    self.Tn.insert(tkinter.END, table)
                                    self.Tn.see("end")
                                    rootn = "root" + str(connId)
                                    self.rootn.update()
                                    msg = '- {} - Fetched all successfully !! '.format(list(driver_method_args_dict.values())[0])
                                    # keys = [k for k, v in connsdb.items() if connId in v]
                                    plogger.info_log(handle =keys[0],msg = msg )
                                    time.sleep(interval)
                                else:
                                    break
                            return data
                    
            except Exception as e:
                # plogger.error_log(handle = keys[0],msg = e )
                keys = [k for k, v in connsdb.items() if connId in v]
                plogger.error_log(handle =keys[0],msg = e )
                # logger.error(e)
                trace_back = sys.exc_info()[2]
                line = trace_back.tb_lineno
                print("Process Exception in line {}".format(line), e)
                response = e
            # return df
            return response
        
    def _command_logger(self,connId,method , log_data):
        log_data ['method '] = method
        keys = [k for k, v in connsdb.items() if connId in v]
        plogger.info_log(handle = keys[0],msg = log_data )
        return

    def _remove_namespace(self,data):
        with open("libs/ref_libs/xml/data.xml",'w') as f:
            f.write(data)
        srcdata = 'libs/ref_libs/xml/data.xml'
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(srcdata, parser)
        root = tree.getroot()
        ####    
        for elem in root.getiterator():
            if not hasattr(elem.tag, 'find'): continue
            i = elem.tag.find('}')
            if i >= 0:
                elem.tag = elem.tag[i+1:]
        objectify.deannotate(root, cleanup_namespaces=True)
        ####
        tree.write('libs/ref_libs/xml/get_NoNS.xml',pretty_print=True, xml_declaration=True, encoding='UTF-8')
        return ('libs/ref_libs/xml/get_NoNS.xml')

    def _get_data_to_table (self,filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        objlist = []
        for child in root:
            for child_level2 in child:
                for child_level3 in child_level2:
                    for child_level4 in child_level3:
        #                 print(child_level4.tag, child_level4.attrib)
                        if child_level4.tag not in objlist:
                            objlist.append(child_level4.tag)
        df = pd.DataFrame()
        fd = open(filename, 'r')
        xml_file = fd.read()
        soup = BeautifulSoup(xml_file, 'lxml')
        for item in objlist:
            if soup.find(item) is not None:
                dfcolumn = []
                lst= []
                if item != "current-advanced-parameter":
                    key = soup.find(item).text
                else:
                    for tag in soup.findAll("current-advanced-parameter"):
                        lst.append(tag.text)
                    key= str(lst)
                dfcolumn.append(key)
                df_add = pd.DataFrame({ item: dfcolumn})
                df = pd.concat([df, df_add], axis=1)
        fd.close()
        return df        
        
    def netconf_get_pm (self,**kwargs):
        """
        ----------------------
            netconf_get_pm(object = <object name>, aid = <AID>, parameter = <parameter name>, interval = <pm_retrival_inerval> , pm_period = <time frame to collect pm>,saveToFile = <filename>)
        
        Method to GET the values/config of any object (e.g. xcon , ethernet, TOM, ODU etc) through NETCONF 
            
            Parameters:
            : object     -> string (e.g. 'optical-carrier')
            : aid        -> string (e.g. '1-6-L1-1')
            : parameter  -> string (e.g. 'pre-fec-q')
            : interval   -> integer in seconds(e.g. 10 means fetch every 10 seconds)
            : pm_period  -> string (e.g. 30s = collect for 30 seconds
                                        30m = collect for 30 minutes
                                        3h = collect for 3 hours )
            : saveToFile -> string (Default = None ,
                                name of a csv file e.g. mytest.csv)
        **Example :** 

            conns['netconf1'].netconf_get_pm(object = 'optical-carrier', aid = '1-6-L1-1', parameter = 'pre-fec-q', interval = 10 , pm_period = '10h',saveToFile = 'pmdata.csv')
        ----------------------
        """
        connId = self.connId
        try:
            subs_list = []
            aid = kwargs.get('aid', None).upper()
            parameter = kwargs.get('parameter', None).lower()
            interval = kwargs.get('interval', None)
            pm_period = kwargs.get('pm_period', None).lower()
            subs_list.append(aid)
            parsed_data = { kwargs.get('object', None) : {'aid': subs_list, 'parameter': parameter,'interval' : interval, 'pm_period' :pm_period }}
            cmd = 'netconf_get_pm' 
            interface = 'NETCONF' #InterfaceType.NETCONF.value 
            operation_method = 'netconf_get_pm'
            driver_method = 'netconf_get_pm'
            driver_method_args_dict = parsed_data # netconf_delete(sut = 'LocalNode', object = 'xcon', name = 'myxcon')
            # print(driver_method_args_dict)
            return self._execute_cmd(sut= "LocalNode", cmd=cmd, interface=interface, operation_method=operation_method, 
                        driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)
        except Exception as e:
            keys = [k for k, v in connsdb.items() if connId in v]
            plogger.error_log(handle =keys[0],msg = e )
            # logger.error(e)
            return False
            
    def xr_get_token(self,**kwargs):
        """
        ----------------------
            xr_get_token()
        
        Method to GET the token to authenticate the APIs from  CM 
            
            Parameters:
            None
        **Example :**

            token = conns['xr'].xr_get_token()
        ----------------------
        """
        connId = self.connId
        keys = [k for k, v in connsdb.items() if connId in v]
        setup_parameters = self._get_setupEnvironment(sut = kwargs.get('sut', None),option = 'Login')
        # plgd = PLGDRestLib('10.220.74.133','/auth/realms/xr-cm/protocol/openid-connect/token')
        # token = plgd.plgd_get_token()
        server_ip = setup_parameters['IpAddress']
        v5_auth_uri = '/auth/realms/xr-cm/protocol/openid-connect/token'
        v7_auth_uri = '/realms/xr-cm/protocol/openid-connect/token'

        client_id = setup_parameters['Client_Id']
        client_secret = setup_parameters['Client_Secret']
        username = setup_parameters['UserName']
        password = setup_parameters['Password']

        payload = {
            'grant_type': 'password',
            'client_id': client_id,
            'client_secret': client_secret,
            'username': username,
            'password': password
        }

        headers = {'Accept':  'application/json'}
        uri = 'https://'+server_ip + v7_auth_uri
        response = self.ssh[connId].post(uri,data=payload, verify=False)
        self._connDict['xr_version'] = '0.7'
        if response.status_code == 405:
            uri = 'https://'+server_ip + v5_auth_uri
            response = self.ssh[connId].post(uri,data=payload, verify=False)
            self._connDict['xr_version'] = '0.5'
            if response.status_code > 399:
                plogger.error_log(handle = keys[0],msg = " Error encountered while connecting : {} : {}".format(response.status_code, response.text))
                print("Error encountered while connecting : {} : {}".format(response.status_code, response.text))
                return False
        elif response.status_code > 399:
            plogger.error_log(handle = keys[0],msg = " Error encountered while connecting : {} : {}".format(response.status_code, response.text))
            print("Error encountered while connecting : {} : {}".format(response.status_code, response.text))
            return False
        plogger.info_log(handle = keys[0],msg = " >> send message :  \n\t Method : 'POST' \n\t URL : {} \n\t  Body : {}".format(uri, response.request.body))
        # print(response.request.body)
        token = response.json()['access_token']
        # print(token)
        
        log_data = {'method ' : 'xr_get_token'}
        plogger.info_log(handle = keys[0],msg = log_data )
        
        plogger.debug_log(handle = keys[0],msg = token )
        return token
    
    def xr_request(self, **kwargs):
        connId = self.connId
        method = kwargs.get('method', None)
        url = kwargs.get('url', None)
        body = kwargs.get('request_body', None)
        try:
            cmd = 'restconf_get' 
            interface = 'RESTCONF'
            operation_method = 'restconf_post'
            driver_method = 'restconf_yang_execute_xr'
            driver_method_args_dict = {
                "method": method,
                "url": url,
                "body": body
            }
            self._command_logger(connId,'xr_post' , driver_method_args_dict)
            return self._execute_cmd(sut=None, cmd=cmd, interface=interface, operation_method=operation_method, 
                        driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)
        except Exception as e:
            # logger.error(e)
            keys = [k for k, v in connsdb.items() if connId in v]
            plogger.error_log(handle = keys[0],msg = e )
            return False

    def xr_subscribe(self, **kwargs):
        connId = self.connId
        url = kwargs.get('url', None)
        name = kwargs.get('name', None)
        filters = kwargs.get('filters', [{}])
        try:
            cmd = 'restconf_subscribe'
            interface = 'RESTCONF'
            operation_method = 'restconf_subscribe'
            driver_method = 'restconf_yang_subscribe_xr'
            driver_method_args_dict = {
                "url": url,
                "body": [{
                    "subscriptionName": name,
                    "subscriptionFilters": filters
                }]
            }
            self._command_logger(connId, 'xr_subscribe', driver_method_args_dict)
            return self._execute_cmd(sut=None, cmd=cmd, interface=interface, operation_method=operation_method, 
                        driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)
        except Exception as e:
            # logger.error(e)
            keys = [k for k, v in connsdb.items() if connId in v]
            plogger.error_log(handle = keys[0],msg = e )
            return False

    def xr_post(self, **kwargs):
        connId = self.connId
        url = kwargs.get('url', None)
        body = kwargs.get('request_body', None)
        try:
            cmd = 'restconf_get' 
            interface = 'RESTCONF'
            operation_method = 'restconf_post'
            driver_method = 'restconf_yang_execute_xr'
            driver_method_args_dict = {
                "method": "GET",
                "url": url,
                "body": body
            }
            self._command_logger( connId,'xr_post' , driver_method_args_dict)
            return self._execute_cmd(sut= sut, cmd=cmd, interface=interface, operation_method=operation_method, 
                        driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)
        except Exception as e:
            # logger.error(e)
            keys = [k for k, v in connsdb.items() if connId in v]
            plogger.error_log(handle = keys[0],msg = e )
            return False


    def xr_get(self,**kwargs):
        """
        ----------------------
            xr_get(sut = <sut>, object = <object>, name= <name>, query = <query type> , filter = <filter type>,token = <token string>)
        
        Method to GET the XR objects. This is the generic GET request 
            
            Parameters:
            object : supported object ['hosts','host','ports','port','networks','networks-hub','networks-leaf','reachable-modules','reachable-module','modules','module-ports','module-port','transport-capacities',''network-connections','network-connection']
            name : name can be a variable or  value (such as UUID) or  parent child UUID separated by % or a string (such as network connection name)
            query : ['expanded','all']
            filter : ['hosts_list', 'ports_list']
        **Example :** 

            hosts = conns['xr1'].xr_get(sut = 'xr_sim',object = 'hosts', query = 'expanded',token = token1)
        ----------------------
        """
        connId = self.connId
        # plgd = PLGDRestLib('10.220.74.133','/auth/realms/xr-cm/protocol/openid-connect/token')
        # token = plgd.plgd_get_token()
        url = kwargs.get('url', None)
        body = kwargs.get('request_body', None)
        try:
            cmd = 'restconf_get' 
            interface = 'RESTCONF' #InterfaceType.NETCONF.value 
            operation_method = 'restconf_get'
            driver_method = 'restconf_yang_execute_xr'
            driver_method_args_dict = {
                "method": "GET",
                "url": url,
                "body": body
            }
            # print(driver_method_args_dict)
            self._command_logger( connId,'xr_get' , driver_method_args_dict)
            return self._execute_cmd(sut= sut, cmd=cmd, interface=interface, operation_method=operation_method, 
                        driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)
        except Exception as e:
            # logger.error(e)
            keys = [k for k, v in connsdb.items() if connId in v]
            plogger.error_log(handle = keys[0],msg = e )
            return False

    def xr_put(self, **kwargs):
        """
        ----------------------
            xr_put(sut = <sut>, object = <object>, name= <name>, body = <body> , token = <token string>)

        Method to PUT (update) the XR objects. This is the generic PUT request

            Parameters:
            object : supported object ['device','network-connection']
            name : name can be a variable or  value (such as UUID) or  parent child UUID separated by % or a string (such as network connection name)
            id : ID of object
            body : Generic body of PUT request
        **Example :**
            `conns['xr1'].xr_put(sut = 'xr_sim',object = 'device', id = '<UUID>' , body = {'status': 'onboarded'}, token = token1)`
        ----------------------
        """
        connId = self.connId
        url = kwargs.get('url', None)
        body = kwargs.get('request_body', None)
        try:
            cmd = 'restconf_get' 
            interface = 'RESTCONF' #InterfaceType.NETCONF.value 
            operation_method = 'restconf_put'
            driver_method = 'restconf_yang_execute_xr'
            driver_method_args_dict = {
                "method": "GET",
                "url": url,
                "body": body
            } 
            self._command_logger( connId,'xr_get' , driver_method_args_dict)
            return self._execute_cmd(sut= sut, cmd=cmd, interface=interface, operation_method=operation_method,
                        driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)
        except Exception as e:
            # logger.error(e)
            keys = [k for k, v in connsdb.items() if connId in v]
            plogger.error_log(handle = keys[0],msg = e )
            return False

    def g40_restconf_request(self, **kwargs):
        """
        ----------------------
            g40_request_body(sut = <sut>, ref_key = <key to request data>, json_file = <file containing request data>)
        
        Method to send RESTCONF POST/PATCH requests with pre-calculated data to G40 
            
            Parameters:
            : 
            : 

        **Example :**
            conns[handle].g40_request_body(sut = sut, ref_key = ref_key, json_file = json_file)
        ----
        """
        connId = self.connId
        method = kwargs.get('method', None)
        url = kwargs.get('url', None)
        body = kwargs.get('request_body', None)
        try:
            cmd = 'restconf_get' 
            interface = 'RESTCONF'
            operation_method = 'restconf_post'
            driver_method = 'restconf_yang_execute_gx'
            driver_method_args_dict = {
                "method": method,
                "url": url,
                "body": body
            }
            self._command_logger(connId,'xr_post' , driver_method_args_dict)
            return self._execute_cmd(sut=None, cmd=cmd, interface=interface, operation_method=operation_method, 
                        driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)
        except Exception as e:
            # logger.error(e)
            keys = [k for k, v in connsdb.items() if connId in v]
            plogger.error_log(handle = keys[0],msg = e )
            return False

    def _g40rest_execute(self, sut=None, conf_data=None):
        connId = self.connId
        cmd = 'restconf_execute' 
        interface = 'RESTCONF' #InterfaceType.NETCONF.value 
        operation_method = 'restconf_execute'
        driver_method = 'restconf_yang_execute_g40'
        driver_method_args_dict = {'conf_data': conf_data}
        msg = " Input Command    : {} \n g40rest Execute config   : {}  ".format(cmd,pformat(driver_method_args_dict))
        keys = [k for k, v in connsdb.items() if connId in v]
        plogger.info_log(handle =keys[0],msg = msg )
        return self._execute_cmd(sut=sut, cmd=cmd, interface=interface, operation_method=operation_method, 
                       driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)  

    def g40_get(self,**kwargs):
        """
        ----------------------
            g40_get(sut = <sut>,object = <object>)
        
        Method to GET the GX G40 objects. This is the generic GET request for GX G40 NE over the RESTCONF interface
            
            Parameters:
            object : Any object name as defined in the GX CLI
        **Examples :** 
            `conns['g40'].g40_get(sut = 'G40_1',object='equipment')
            
            conns['g40'].g40_get(sut = 'G40_1',object='alarm')
            
            conns['g40'].g40_get(sut = 'G40_1',object='slot-1-1')
            
            conns['g40'].g40_get(sut = 'G40_1',object='security')
            
            conns['g40'].g40_get(sut = 'G40_1',object='security-policies')
            
            
        ----------------------
        """
        connId = self.connId
        try:
            sut = kwargs.get('sut', None)
            cmd = 'restconf_get' 
            interface = 'RESTCONF' #InterfaceType.NETCONF.value 
            operation_method = 'restconf_get'
            driver_method = 'restconf_yang_get_g40'
            driver_method_args_dict = {"path" :  kwargs.get('path', None)} 
            # print(driver_method_args_dict)
            self._command_logger( connId,'g40_get' , driver_method_args_dict)
            return self._execute_cmd(sut= sut, cmd=cmd, interface=interface, operation_method=operation_method, 
                        driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)
        except Exception as e:
            # logger.error(e)
            keys = [k for k, v in connsdb.items() if connId in v]
            plogger.error_log(handle = keys[0],msg = e )
            return False

    def g40_netconf_request(self, **kwargs):
        """
        ----------------------
            g40_request_body(sut = <sut>, ref_key = <key to request data>, json_file = <file containing request data>)
        
        Method to send RESTCONF POST/PATCH requests with pre-calculated data to G40 
            
            Parameters:
            : 
            : 

        **Example :**
            conns[handle].g40_request_body(sut = sut, ref_key = ref_key, json_file = json_file)
        ----
        """
        # paths = str(kwargs.get('path', None))
        ref_key = kwargs.get('ref_key', None)
        xml_filepath = kwargs.get('xml_filepath', None)
        xml_data = {}
        with open(xml_filepath) as fh:
            xml_data = fh.read()
        parse_data = xmltodict.parse(xml_data)
        return self._g40netconf_execute(conf_data = parse_data['data'][ref_key])

    def _g40netconf_execute(self, conf_data=None):
        connId = self.connId
        cmd = 'netconf_execute' 
        interface = 'NETCONF' #InterfaceType.NETCONF.value 
        operation_method = 'netconf_yang_execute'
        driver_method = 'netconf_yang_execute_g40'
        driver_method_args_dict = {'conf_data': conf_data}
        msg = " Input Command : {} \n g40netconf Execute config : {}  ".format(cmd,pformat(driver_method_args_dict))
        keys = [k for k, v in connsdb.items() if connId in v]
        plogger.info_log(handle =keys[0],msg = msg )
        return self._execute_cmd(cmd=cmd, interface=interface, operation_method=operation_method, 
                       driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)
    
    def g40_netconf_rpc(self, **kwargs):
        """
        ----------------------
            g40_request_body(sut = <sut>, ref_key = <key to request data>, json_file = <file containing request data>)
        
        Method to send RESTCONF POST/PATCH requests with pre-calculated data to G40 
            
            Parameters:
            : 
            : 

        **Example :**
            conns[handle].g40_request_body(sut = sut, ref_key = ref_key, json_file = json_file)
        ----
        """
        # paths = str(kwargs.get('path', None))
        ref_key = kwargs.get('ref_key', None)
        xml_filepath = kwargs.get('xml_filepath', None)
        xml_data = {}
        with open(xml_filepath) as fh:
            xml_data = fh.read()
        parse_data = xmltodict.parse(xml_data)
        return self._g40netconf_execute_rpc(sut = sut, conf_data = parse_data['data'][ref_key])
    
    def _g40netconf_execute_rpc(self, conf_data=None):
        connId = self.connId
        cmd = 'netconf_execute'
        interface = 'NETCONF' #InterfaceType.NETCONF.value
        operation_method = 'netconf_yang_execute'
        driver_method = 'netconf_yang_rpc_g40'
        driver_method_args_dict = {'conf_data': conf_data}
        msg = " Input Command : {} \n g40netconf RPC config : {}  ".format(cmd,pformat(driver_method_args_dict))
        keys = [k for k, v in connsdb.items() if connId in v]
        plogger.info_log(handle =keys[0],msg = msg )
        return self._execute_cmd(cmd=cmd, interface=interface, operation_method=operation_method, 
                       driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)

    def g40_netconf_subscribe(self, stream=None, filter=None):
        connId = self.connId
        cmd = 'netconf_execute'
        interface = 'NETCONF' #InterfaceType.NETCONF.value
        operation_method = 'netconf_yang_subscribe'
        driver_method = 'netconf_yang_subscribe_g40'
        driver_method_args_dict = {'stream': stream, 'filter': filter}
        msg = " Input Command : {} \n g40netconf Subscribe config : {}  ".format(cmd,pformat(driver_method_args_dict))
        keys = [k for k, v in connsdb.items() if connId in v]
        plogger.info_log(handle =keys[0],msg = msg )
        return self._execute_cmd(cmd=cmd, interface=interface, operation_method=operation_method,
                       driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)

    def g40_netconf_get_streams(self):
        connId = self.connId
        cmd = 'netconf_execute'
        interface = 'NETCONF' #InterfaceType.NETCONF.value
        operation_method = 'netconf_yang_stream'
        driver_method = 'netconf_yang_get_streams_g40'
        driver_method_args_dict = {}
        msg = " Input Command : {} \n g40netconf Subscribe config : {}  ".format(cmd,pformat(driver_method_args_dict))
        keys = [k for k, v in connsdb.items() if connId in v]
        plogger.info_log(handle =keys[0],msg = msg )
        return self._execute_cmd(cmd=cmd, interface=interface, operation_method=operation_method,
                       driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)

    def g40_netconf_notification(self, timeout=30):
        connId = self.connId
        cmd = 'netconf_execute'
        interface = 'NETCONF' #InterfaceType.NETCONF.value
        operation_method = 'netconf_yang_notification'
        driver_method = 'netconf_yang_notification_g40'
        driver_method_args_dict = {'timeout': timeout}
        msg = " Input Command : {} \n g40netconf Notification config : {}  ".format(cmd,pformat(driver_method_args_dict))
        keys = [k for k, v in connsdb.items() if connId in v]
        #plogger.info_log(handle =keys[0],msg = msg )
        return self._execute_cmd(cmd=cmd, interface=interface, operation_method=operation_method,
                       driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)
    
    def g40_netconf_get(self, **kwargs):
        """
        ----------------------
            g40_request_body(sut = <sut>, ref_key = <key to request data>, json_file = <file containing request data>)
        
        Method to send RESTCONF POST/PATCH requests with pre-calculated data to G40 
            
            Parameters:
            : 
            : 

        **Example :**
            conns[handle].g40_request_body(sut = sut, ref_key = ref_key, json_file = json_file)
        ----
        """
        ref_key = kwargs.get('ref_key', None)
        xml_filepath = kwargs.get('xml_filepath', None)
        xml_data = {}
        with open(xml_filepath) as fh:
            xml_data = fh.read()
        parse_data = xmltodict.parse(xml_data)

        return self._g40_netconf_get(conf_data = parse_data['data'][ref_key])

    def _g40_netconf_get(self, conf_data=None):
        connId = self.connId
        cmd = 'netconf_get' 
        interface = 'NETCONF' #InterfaceType.NETCONF.value 
        operation_method = 'netconf_yang_get'
        driver_method = 'netconf_yang_get_g40'
        filter_data = conf_data['nc:filter']
        driver_method_args_dict = {'filter': filter_data}
        if '@type' in filter_data:
            driver_method_args_dict['type'] = filter_data['@type']
            del filter_data['@type']
        msg = " Input Command : {} \n g40netconf Get : {}  ".format(cmd,pformat(driver_method_args_dict))
        keys = [k for k, v in connsdb.items() if connId in v]
        plogger.info_log(handle =keys[0],msg = msg )
        return self._execute_cmd(cmd=cmd, interface=interface, operation_method=operation_method, 
                       driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)

    def g40_netconf_delete(self, **kwargs):
        """
        ----------------------
            g40_request_body(sut = <sut>, ref_key = <key to request data>, json_file = <file containing request data>)
        
        Method to send RESTCONF POST/PATCH requests with pre-calculated data to G40 
            
            Parameters:
            : 
            : 

        **Example :**
            conns[handle].g40_request_body(sut = sut, ref_key = ref_key, json_file = json_file)
        ----
        """
        filter_dict = kwargs.get('filter', None)

        connId = self.connId
        cmd = 'netconf_delete' 
        interface = 'NETCONF' #InterfaceType.NETCONF.value 
        operation_method = 'netconf_yang_delete'
        driver_method = 'netconf_yang_delete_g40'
        driver_method_args_dict = {'filter': filter_dict}
        msg = " Input Command : {} \n g40netconf Delete : {}  ".format(cmd,pformat(driver_method_args_dict))
        keys = [k for k, v in connsdb.items() if connId in v]
        plogger.info_log(handle =keys[0],msg = msg )
        return self._execute_cmd(cmd=cmd, interface=interface, operation_method=operation_method, 
                       driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)

    def xr_create_link(self,**kwargs):
        """
        ----------------------
            xr_create_link(object = 'network-connection', name= <name of connection>, src_type = <source obj type> , src_val = <source obj parameters >,dst_tyoe = <dest  obj type>, dst_val = <dest obj parameters>,token = <token string>)
        
        Method to CREATE the Network Connection between 2 endpoints

            Parameters:
            object : 'network-connection'
            name : name of the network connection -> str
            src_type : source endpoint Type -> str
                supported options : {"HostName" , "HostPortId" ,"HostSysName","HostPortSourceMAC",  "ModuleId" , "ModuleName", "ModuleMAC" , "ModuleSerialNumber"  }
            src_val : source endpoint parameters -> dict (see options)
            dst_type : dest endpoint Type -> str
                supported options : {"HostName" , "HostPortId" ,"HostSysName","HostPortSourceMAC",  "ModuleId" , "ModuleName", "ModuleMAC" , "ModuleSerialNumber"  }            
            dst_val : dest endpoint parameters-> dict (see options)
            ---
            
            options help :   
                {
                    <src_type OR dst_type>  : 
                    {
                        <src_val OR dst_val> : <val>
                    }
                    
                }
            options :
                {
                    "HostName " : { 
                        "name" :  source endpoint Hostname -> str -> default:None
                    }
                    "HostPortId" : {
                        "chassisId" : source endpoint Chassis ID -> str -> default:None
                        "chassisIdSubtype" : source endpoint Chassis ID subtype -> str -> default:None
                        "portId" : source endpoint Chassis ID Port Id -> str -> default:None
                        "portIdSubtype" : source endpoint Port ID subtype -> str -> default:None
                    }
                    "HostSysName" : {
                        "sysName" :  source endpoint Host System Name -> str -> default:None
                        "portId" : source endpoint Chassis ID Port Id -> str -> default:None
                        "portIdSubtype" : source endpoint Port ID subtype -> str -> default:None
                    } 
                    "HostPortSourceMAC" : {
                        "portSourceMAC" : source endpoint Port MAC address -> str -> default:None
                    }
                    "ModuleId"  : {
                        "moduleId" : source endpoint Module ID -> str -> default:None
                        "moduleClientIfAid" : source endpoint Module Client Interface ID -> str -> default:None
                    }
                   "ModuleName" : {
                        "moduleName" : source endpoint Module Name -> str -> default:None
                       "moduleClientIfAid" : source endpoint Module Client Interface ID -> str -> default:None
                   }
                    "ModuleMAC" : {
                        "moduleMAC" :  source endpoint Module MAC address -> str -> default:None
                        "moduleClientIfAid" : source endpoint Module Client Interface ID -> str -> default:None
                    }
                    "ModuleSerialNumber" : {
                        "moduleSerialNumber" : source endpoint Module Serial Number -> str -> default:None
                        "moduleClientIfAid" : source endpoint Module Client Interface ID -> str -> default:None
                    }
                }

        **Example :**
        
        **[ 1 ] :**
            `conns['xr'].xr_create_link(object = 'network-connection', name= 'HUB1', src_type = 'ModuleSerialNumber' ,src_val = { 'moduleSerialNumber' = '000000009', 'moduleClientIfAid = 'XR-T2'}, dst_type = "ModuleSerialNumber",{ 'moduleSerialNumber' = '00000000C', 'moduleClientIfAid' = 'XR-T1'},token = token)`
        
        **[ 2 ] :**
            `conns['xr'].xr_create_link(object = 'network-connection', name= 'HUB1', src_type = 'ModuleName' ,src_val = { 'moduleName' = 'Juniper1', 'moduleClientIfAid = 'XR-T2'}, dst_type = "ModuleSerialNumber",{ 'moduleSerialNumber' = '00000000C', 'moduleClientIfAid' = 'XR-T1'},token = token)`
        ----------------------
        """
        connId = self.connId
        # plgd = PLGDRestLib('10.220.74.133','/auth/realms/xr-cm/protocol/openid-connect/token')
        # token = plgd.plgd_get_token()
        try:
            sut = kwargs.get('sut', None)
            cmd = 'xr_create_link' 
            interface = 'RESTCONF' #InterfaceType.NETCONF.value 
            operation_method = 'restconf_post'
            driver_method = 'restconf_get_xr'
            driver_method_args_dict = {"token" : kwargs.get('token', None),
                                        "object" :  kwargs.get('object', None),
                                        "name" :  kwargs.get('name', None),
                                        "label" :  kwargs.get('label', None),
                                        "src_type": kwargs.get('src_type', None),
                                        "src_val" : kwargs.get('src_val', None),
                                        "dst_type" : kwargs.get('dst_type', None),
                                        "dst_val" : kwargs.get('dst_val', None)} # netconf_delete(sut = 'LocalNode', object = 'xcon', name = 'myxcon')
            # print(driver_method_args_dict)
            self._command_logger( connId,'xr_create_link' , driver_method_args_dict)
            return self._execute_cmd(sut = sut, cmd = cmd, interface = interface, operation_method = operation_method, 
                        driver_method = driver_method, driver_method_args_dict = driver_method_args_dict)
        except Exception as e:
            # logger.error(e)
            keys = [k for k, v in connsdb.items() if connId in v]
            plogger.error_log(handle =keys[0],msg = e )
            return False
    
    def xr_delete_link(self,**kwargs):
        """
        ----------------------
            xr_delete_link(object = 'network-connection', name= <name of connection>, token = <token string>)
        
        Method to DELETE the Network Connection by a Name

        **Example :** 

            conns['xr'].xr_delete_link(object = 'network-connection', name= 'HUB1', token = token)
        ----------------------
        """  
        connId = self.connId
        # plgd = PLGDRestLib('10.220.74.133','/auth/realms/xr-cm/protocol/openid-connect/token')
        # token = plgd.plgd_get_token()
        try:
            sut = kwargs.get('sut', None)
            cmd = 'restconf_delete' 
            interface = 'RESTCONF' #InterfaceType.NETCONF.value 
            operation_method = 'restconf_delete'
            driver_method = 'restconf_get_xr'
            driver_method_args_dict = {"token" : kwargs.get('token', None),
                                        "object" :  kwargs.get('object', None),
                                        "name" :  kwargs.get('name', None),
                                        "id":  kwargs.get('id', None)
                                        } # netconf_delete(sut = 'LocalNode', object = 'xcon', name = 'myxcon')
            # print(driver_method_args_dict)
            self._command_logger( connId,'xr_delete_link' , driver_method_args_dict)
            return self._execute_cmd(sut= sut, cmd=cmd, interface=interface, operation_method=operation_method, 
                        driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)
        except Exception as e:
            # logger.error(e)
            keys = [k for k, v in connsdb.items() if connId in v]
            plogger.error_log(handle =keys[0],msg = e )
            return False
            
    def netconf_get(self, **kwargs):
        """
        ----------------------
            netconf_get(object = <object name>, name = <parameter name>)
        
        Method to GET the values/config of any object (e.g. xcon , ethernet, TOM, ODU etc) through NETCONF

            Parameters:
            : object      -> string (e.g. 'xcon')
            : name        -> string (e.g. 'ALL')

        **Example :** 

            conns['netconf1'].netconf_get(object = 'xcon', name = 'ALL')\n
            conns['netconf1'].netconf_get(object = 'xcon', name = '1-6-T1,OTU4')\n
        ----------------------
        """  

        try:
            connId = self.connId
            cmd = 'netconf_get' 
            interface = 'NETCONF' #InterfaceType.NETCONF.value 
            operation_method = 'netconf_get'
            driver_method = 'netconf_get'
            driver_method_args_dict = { kwargs.get('object', None) : kwargs.get('name', None) } # netconf_delete(sut = 'LocalNode', object = 'xcon', name = 'myxcon')
            # print(driver_method_args_dict)
            self._command_logger( connId,'netconf_get' , driver_method_args_dict)
            return self._execute_cmd(sut= "LocalNode", cmd=cmd, interface=interface, operation_method=operation_method, 
                        driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)
        except Exception as e:
            # logger.error(e)
            keys = [k for k, v in connsdb.items() if connId in v]
            plogger.error_log(handle =keys[0],msg = e )
            return False
            
    def netconf_delete(self,**kwargs):
        """
        ----------------------
            netconf_delete(object = <object name>, name = <parameter name>)
        
        Method to DELETE the any object (e.g. xcon , ethernet, TOM, ODU etc) through NETCONF

            Parameters:
            : object      -> string (e.g. 'xcon')
            : name        -> string (e.g. 'myxcon-1')

        **Example :** 

            conns['netconf1'].netconf_delete(object = 'super-channel', name = 'SCH41'))
        ----------------------
        """  

        try:
            connId = self.connId
            cmd = 'netconf_delete' 
            interface = 'NETCONF' #InterfaceType.NETCONF.value 
            operation_method = 'netconf_delete'
            driver_method = 'netconf_delete'
            driver_method_args_dict = { kwargs.get('object', None) : kwargs.get('name', None) } # netconf_delete(sut = 'LocalNode', object = 'xcon', name = 'myxcon')
            self._command_logger( connId,'netconf_delete' , driver_method_args_dict)
            return self._execute_cmd(sut= "LocalNode", cmd=cmd, interface=interface, operation_method=operation_method, 
                        driver_method=driver_method, driver_method_args_dict=driver_method_args_dict)
        except Exception as e:
            # logger.error(e)
            keys = [k for k, v in connsdb.items() if connId in v]
            plogger.error_log(handle =keys[0],msg = e )
            return False        



    def _connect_ui_part(self, **kwargs):
    
        connId = self.connId
        use_rexui = True
        #use_rexui = False     
        try:
            #gCLI1 = rexui.App.notebookRoot()
            gCLI1 = rexui.gCLI1

        except:
            use_rexui = False
        
        if use_rexui:
            
            #self.frame3 = ttk.Frame(self.notebook, width=150, height=250)
            #self.frame3.pack(fill='both', expand=True)
            #self.notebook.add(self.frame3, text='Conn1')
           
            self.frame = ttk.Frame(gCLI1, width=150, height=250)
            self.rootn = self.frame
            self.frame.pack(fill='both', expand=True)
            gCLI1.add(self.frame, text=str(self.handle))

            self.Tn = tkinter.Text(
                self.frame, height=18, width=100, bg="black", fg="white"
            )
            
            self.Tn.pack()

            self.scroll_bar = tkinter.Scrollbar(self.frame)
            self.scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
            self.scroll_bar.config(command=self.Tn.yview)
            self.Tn.config(yscrollcommand=self.scroll_bar.set)
            
            self.frame1 = tkinter.Frame(self.frame)
            self.frame1.pack(side=tkinter.TOP)

            self.entry = tkinter.Entry(self.frame1, width=60)
            self.entry.pack(side=tkinter.RIGHT)
            self.entry.bind('<Return>',self._sndButton)
            
        else:
            rootn = "root" + str(connId)
            self.rootn = tkinter.Tk()
            # cstr = "vsh connection #" + str(connId)
            cstr = "vsh connection #" + str(self.handle)
            self.rootn.title(cstr)
            Tn = "T" + str(connId)
            # 1/17 - was 96 for a bit
            self.Tn = tkinter.Text(
                self.rootn, height=10, width=100, bg="black", fg="white"
            )

            # new
            # self.scroll?!!!
            scroll_bar = tkinter.Scrollbar(self.rootn)
            #!!! self.rootn , tkinter
            scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
            scroll_bar.config(command=self.Tn.yview)
            self.Tn.config(yscrollcommand=scroll_bar.set)

            #  command = nada
            # should be self.frame1???
            self.frame1 = tkinter.Frame(self.rootn)
            self.frame1.pack(side=tkinter.TOP)

            self.entry = tkinter.Entry(self.frame1, width=60)
            self.entry.pack(side=tkinter.LEFT)

            self.sendButton = tkinter.Button(
                self.frame1, height=2, width=6, text="Send", command=self._sndButton
            )
            self.sendButton.pack(side=tkinter.RIGHT)
            # new end

            self.Tn.pack(side=tkinter.LEFT)
            

    def connect(self, ip, port, username, password, **kwargs):
    
        #print("--bb--")
        # print("in connect...turned off keep - alive, logging messes up using ipython, is it needed???")
        connId = self.connId
        if self.debug:
            print("connecting to",self.handle)
        # connection ID not needed with "self" !!!
        # c1 = conection ID 1,2, ...
        # conn = 0,1,2
        #   1 = new connection
        #   0 = send / rcv command
        #   2 = disconnect
        # cmd = command to send with \n
        # logger id
        # not working!
        
    ############### copy paste _connect_ui_part ( not working to call)
        #_connect_ui_part(self, **kwargs)
    
        connId = self.connId
        use_rexui = True
        #use_rexui = False     
        try:
            #gCLI1 = rexui.App.notebookRoot()
            gCLI1 = rexui.gCLI1

        except:
            use_rexui = False
        
        if use_rexui:
            pQueue = pixi.PIXIQueue()
            pQueue.put({
                "command": "create_window",
                "data": {
                    "handle": self.handle,
                    "vsh": self
                }
            })
            #self.frame3 = ttk.Frame(self.notebook, width=150, height=250)
            #self.frame3.pack(fill='both', expand=True)
            #self.notebook.add(self.frame3, text='Conn1')
            """
            self.frame = ttk.Frame(gCLI1, width=150, height=250)
            self.rootn = self.frame
            self.frame.pack(fill='both', expand=True)
            gCLI1.add(self.frame, text=str(self.handle))
            self.Tn = tkinter.Text(
                self.frame, height=18, width=100, bg="black", fg="white"
            )
            
            self.Tn.pack()
            self.scroll_bar = tkinter.Scrollbar(self.frame)
            self.scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
            self.scroll_bar.config(command=self.Tn.yview)
            self.Tn.config(yscrollcommand=self.scroll_bar.set)
            
            self.frame1 = tkinter.Frame(self.frame)
            self.frame1.pack(side=tkinter.TOP)

            self.entry = tkinter.Entry(self.frame1, width=60)
            self.entry.pack(side=tkinter.RIGHT)
            self.entry.bind('<Return>',self._sndButton)
            """
            
        else:
            rootn = "root" + str(connId)
            self.rootn = tkinter.Tk()
            # cstr = "vsh connection #" + str(connId)
            cstr = "vsh connection #" + str(self.handle)
            self.rootn.title(cstr)
            Tn = "T" + str(connId)
            # 1/17 - was 96 for a bit
            self.Tn = tkinter.Text(
                self.rootn, height=10, width=100, bg="black", fg="white"
            )

            # new
            # self.scroll?!!!
            scroll_bar = tkinter.Scrollbar(self.rootn)
            #!!! self.rootn , tkinter
            scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
            scroll_bar.config(command=self.Tn.yview)
            self.Tn.config(yscrollcommand=scroll_bar.set)

            #  command = nada
            # should be self.frame1???
            self.frame1 = tkinter.Frame(self.rootn)
            self.frame1.pack(side=tkinter.TOP)

            self.entry = tkinter.Entry(self.frame1, width=60)
            self.entry.pack(side=tkinter.LEFT)

            self.sendButton = tkinter.Button(
                self.frame1, height=2, width=6, text="Send", command=self._sndButton
            )
            self.sendButton.pack(side=tkinter.RIGHT)
            # new end

            self.Tn.pack(side=tkinter.LEFT)
    ###############
        
        #print("--cc--")
        

        # later check if connected already and return error and disconnect first suggestion
        if _sim("get") == False:
            self.ssh[connId] = paramiko.SSHClient()
            #
            self.ssh[connId].set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh[connId].load_system_host_keys()

        # https://stackoverflow.com/questions/7439563/how-to-ssh-to-localhost-without-password
        if 0:
            # missing key param above
            passwd = getpass()
            # ssh.connect(hostname="localhost",port = "22",username="username",password="xxyyzz")
            self.ssh.connect(
                hostname="localhost", port="22", username="username", password=passwd
            )
        else:
            if _sim("get") == False:
                # self.ssh[connId].connect(hostname="localhost",port = "22")
                self.ssh[connId].connect(
                    hostname=ip, port=port, username=username, password=password
                )
            #print("...23 22")
        if _sim("get") == False:
            #print("Turned off keep alive - needed?  Logging / printing too messy!!!")
            self.ssh[connId]._transport.set_keepalive(60)
            # print("Timeout set short = .1 - because of upper level looping")
            # self.ssh[connId].settimeout(.1)
            # !!!
            # https://www.semicolonworld.com/question/60047/how-to-interact-with-paramiko-39-s-interactive-shell-session
            self.chan[connId] = self.ssh[connId].get_transport().open_session()
            print(f"Channel id will be {self.chan[connId]}")
            print(f"Connection id will be {connId}")
            self.chan[connId].get_pty(width=110)
            self.chan[connId].invoke_shell()
        return 1

    def _sndButton(self,unused):
        cmd = self.entry.get()
        cmdn = cmd + "\n"
        print("sending: ", cmd)
        rslt = self.sendRcv(cmdn, sendOnly=True)
        #print(rslt)
        self.entry.delete(0, "end")
        return 1

    def sendRcv(self, cmd, **kwargs):
        # import ipdb; ipdb.set_trace()
        """
        ----------------------
            sendRcv("command to send to NE (CLI /SSH)")
        
        Method to send the CLI command to the NE 

            Parameters ( see example below)
               handle
               command to send ( without termination)
            Parameters, optional
              sendOnly=False(default)  or True
              rcvOnly=False(default)  or True
              timeout=20(default) - seconds
              fromUI=False(detault) or True
              runAsStep False default
              prompt=(has defaults), override for commands like password prompt, etc.
        **Example :**
            `conns['cli1'].sendRcv('show xcon\n')`
        ----------------------
        """
 
        # psuedo code notes for cli ssh
        # if rcv only, rcv buffer, display in ui, and return data
        # if sending a new command with rcv
        #   - before sending, clear out the rcv buffer and display on UI.
        #   - send command ( can make sure echoed in resp by default)
        #   - rcv, display, return buffer
        # import ipdb; ipdb.set_trace()
        connId = self.connId
        timeouti = int(kwargs.get("timeout", 20))
        sendOnlyi = kwargs.get("sendOnly", False)
        rcvOnlyi = kwargs.get("rcvOnly", False)
        # used for code other than ssh CLI
        execCmd = kwargs.get("execCmd", False)
        # does nothing now
        fromUIi = kwargs.get("fromUI", False)
        
        runAsStep = kwargs.get("runAsStep", False)
        resultFailsStep = kwargs.get("resultFailsStep", "fail-str-not-set")
        cmdType = kwargs.get("type", False)
        prompti = kwargs.get("prompt", False)
        buffer = b""

        pQueue = pixi.PIXIQueue()
        # print(f"First command will be comming here :::::::: {cmd}")
        # print(f"Pqueue will be :::::::::: {pQueue}")
        # print(f"rcvOnlyi will be come here first ::::: {rcvOnlyi}")
        
        if _sim("get") == False:
            print("Getting Sim 1")
            print(f"-------------> RcvOnly will be : {rcvOnlyi}")
            if self.ssh == {}:
                print("Please connect first")
                return "0"
        print("Going down to _sim")
        if (_sim("get") == True):
            print("Getting Sim 2")
            if rcvOnlyi is False:
                keys = [k for k, v in connsdb.items() if connId in v]
                strin = "Simulate "+keys[0]+" send: -" + cmd.strip() + "-"
                #print("del this key[0]",keys[0])
                plogger.debug_log(handle = keys[0],msg = strin )
                print(strin)
            
                pQueue.put({"command": "add_to_window", "data": {"handle": self.handle, "text": strin}})
                #self.Tn.insert(tkinter.END, strin)
                #self.Tn.see("end")
                #self.rootn.update()
                return "1"
            else:
                return "1"
        # print(f"Comming to execCmd - {execCmd}")
        if execCmd == True:
            # elif:
            # if 'ssh[connId]' in globals():
            # print("*** chan[connId]",chan[connId],"***")
            if _sim("get") == False:
                stdin, stdout, stderr = self.ssh[connId].exec_command(cmd)
                keys = [k for k, v in connsdb.items() if connId in v]
                plogger.debug_log(handle = keys[0],msg = stdout )
                for line in stdout:
                    # print(line)
                    #self.Tn.insert(tkinter.END, line)
                    pQueue.put({"command": "add_to_window", "data": {"handle": self.handle, "text": line}})
                return stdout
            else:
                return ""
        # else leaving connection open

        #encode1 = buffer.decode("utf-8") 
        #encode = encode1.encode("ascii", "ignore")  
        #bufStr = encode.decode()
        
        #bufStr = buffer.decode("ascii")
        # print("Comming here atleast")
        bufStr = buffer.decode("utf-8")
        del buffer

        # print("Deleting Buffer")
        Tn = "T" + str(connId)
        # print(Tn)
        keys = [k for k, v in connsdb.items() if connId in v]
        # print(keys)
        plogger.debug_log(handle = keys[0],msg = bufStr )
        print("debug set")
        # print(self.handle)
        # print(bufStr)
        #self.Tn.insert(tkinter.END, bufStr)
        #self.Tn.see("end")
        pQueue.put({"command": "add_to_window", "data": {"handle": self.handle, "text": bufStr}})
        # print("Queue Successfuly")
        # 5/9
        #try:
        #   #self.rootn.update()
        #except:
        #   print("error around rootn")
        del bufStr
        # print("Second Buffer Deletion")

#########################

######### replaced code 
# clear buffer and update UI before sending command
# ( should be done in background)
#  for normal send / rcv case.
        if False:
            # send first
            if rcvOnlyi == False:
                buffer = b""
                resp = b""
                reads = 0
                #
                if self.chan[connId].recv_stderr_ready():
                    data = self.chan[connId].recv_stderr(1024)
                    print("err", data)
                    datal = len(data)
                    dcountMax = 400
                    # could save "event" output to a second buffer like with TL1 !!!
                    if datal > 1023:
                        #print(
                        #    "Clear Buffer: this may break later, note dcount etc, arbitrary"
                        #)
                        dcount = 0
                        while data and (dcount < dcountMax):
                            if self.chan[connId].recv_stderr_ready():
                                data = self.chan[connId].recv_stderr(1024)
                                print("err", data)
                                # temp test!!!
                                # self.root.update()
                                datal = len(data)
                                # print("-CB",end="")
                                if datal > 1023:
                                    dcount += 1
                                else:
                                    break
                            else:
                                break
                        # print error if hit max!!!
                        print("dcount = ", dcount)
                        if dcount == dcountMax:
                            print(
                                "dcount = dcountMax, did not fully clear buffer, not sending!"
                            )
                            return "0"
                    del data
                #
                if self.chan[connId].recv_ready():
                    data = self.chan[connId].recv(1024)
                    datal = len(data)
                    dcountMax = 400
                    # could save "event" output to a second buffer like with TL1 !!!
                    if datal > 1023:
                        #print(
                        #    "Clear Buffer: this may break later, note dcount etc, arbitrary"
                        #)
                        dcount = 0
                        while data and (dcount < dcountMax):
                            if self.chan[connId].recv_ready():
                                data = self.chan[connId].recv(1024)
                                # temp test!!!
                                # self.root.update()
                                datal = len(data)
                                # print("-CB",end="")
                                if datal > 1023:
                                    dcount += 1
                                else:
                                    break
                            else:
                                break
                        # print error if hit max!!!
                        print("dcount = ", dcount)
                        if dcount == dcountMax:
                            print(
                                "dcount = dcountMax, did not fully clear buffer, not sending!"
                            )
                            return "0"
                    del data
###################

        # send first
        # print("1")
        # print(cmd)
        if rcvOnlyi == False:

            # print("2")
            # clear out buffer and display, call self once ,not sure how to do...
            print("sending connId -"+cmd+"-")
            self.chan[connId].send(cmd)
            # print("after sendid")
            
        if sendOnlyi == True:
            # handled above.
            noop = 1
            #print("not returning early on sendOnly...")
            #return "1"

        ##print("rcv == True")
        success = 0
        buffer = b""
        resp = b""
        reads = 0

        # 20 secs
        # timestart, timemax
        bufferPrev = "notSet"
        tnow = time.time()
        tmax = time.time() + int(timeouti)
        #maxReads = int(timeouti * 100)
        # reads < maxReads:
        timedOut = False
        tstart = tnow
        if sendOnlyi == True:
            tmax = time.time() + 1
        while True:
            if (tnow <= tmax):
                noop = 1
            else:
                timedOut = True
                #print("sendRcv timed out")
                break
            # careful on sleep time ganularity
            #try:
            #    rootn = "root" + str(connId)
            #    self.rootn.update()
            #except Exception as e:
            #    noop = 1
            #    print("error rootn update", end="")
            reads += 1
            if reads % 10 == 0:
                if sendOnlyi == False:
                    time.sleep(0.05)
                else:
                    time.sleep(0.01)
                ##print("reads w/sleep 0.1 = ", reads)
            #if reads == maxReads:
            #    hitMaxReads = "yes"

            if self.chan[connId].recv_ready():
                resp = self.chan[connId].recv(1024)
                # print(resp)
                buffer += resp
                # prompt !!! make it settable ???
                if sendOnlyi == False:
                    if prompti is not False:
                        prompti.encode('utf_8') in resp
                        success = 1
                        break
                    elif (
                        resp.endswith(b"$ ")
                        or resp.endswith(b"# ")
                        or resp.endswith(b"> ")
                        or resp.endswith(b">")
                        or resp.endswith(b"[y/n] ")
                    ):
                        # !!!
                        #print("success")
                        success = 1
                        break
                else:
                    if buffer == bufferPrev:
                        break
                    bufferPrev == buffer
            tnow = time.time()
        del resp
        deltaT = tnow-tstart
        if deltaT > 19:
            print("sendRcv time: ",tnow-tstart, "secs.")

        # local variable and e ( not working !!!)
        if "e" in locals():
            print("exception:", str(e))
        #print("reads ", reads)
        if success == 0:
            if timedOut:
                if (sendOnlyi == False) and (timeouti > 0):
                    # !!!
                    #print("timeouti",timeouti)
                    print("sendRcv timed out..")
                    noop = 1
            bufStr = "0"
        else:
            # out.decode("ascii")
            # buffer.decode("utf-8")
            # self.bufStr[connId] = buffer.decode("ascii")
            noop = 1
            
        #encode1 = buffer.decode("utf-8") 
        #encode = encode1.encode("ascii", "ignore")  
        #bufStr = encode.decode()
        
        #bufStr = buffer.decode("ascii")
        bufStr = buffer.decode("utf-8")
        del buffer

        # self.logger.info(self.bufStr[connId])
        ##print("blen", len(bufStr))
        # self.bufStr[connId] = "\n".join(self.bufStr[connId].splitlines())

        # 1/17
        # bufStr = "\n".join(bufStr.splitlines())

        # lbufStr = self.bufStr[connId]
        ##print("alen", len(bufStr))
        Tn = "T" + str(connId)
        # for line in bufStr.splitlines():
        #    self.Tn.insert(tkinter.END,bufStr)
        # del line
        keys = [k for k, v in connsdb.items() if connId in v]
        plogger.debug_log(handle = keys[0],msg = bufStr )
        #self.Tn.insert(tkinter.END, bufStr)
        #self.Tn.see("end")
        pQueue.put({"command": "add_to_window", "data": {"handle": self.handle, "text": bufStr}})
        # 5/9
        #try:
        #   self.rootn.update()
        #except:
        #   print("error around rootn")
           
        # print("clearing buffer string")
        # del self.bufStr[connId]
        # self.bufStr[connId] = ""

        if runAsStep == "True":
            if resultFailsStep in bufStr:
                print("Result is -", bufStr, "-.  returning fail == 0")
                return 0

        return bufStr

    def _innerPause(self):
      # 
      global _pause
      print("paused@@@@")
      sec = 1
      # has to hit an object with root tk widget (rexui,vsh), so, not using 
      while True:
         #if sec % 1 == 0:
         #print(".",sec)
         # ms!
         #time.sleep(.1)
         #title = f'halt on fail %',sec
         #self.root.title(title)
         sec += 1
         # 10
         # no longer loading results!
         if sec > 999999999999:
            break
         count = 1
         print('.', end = '')
         # 5/24
         #print('paused:', count, flush=True)
         count += 1
         time.sleep(0.2)
         self.rootn.update()
         # 5/24
         #sys.stdout.flush()
         #%debug
         
         # rrFailed = False
         # try:
            #rexui.rexRoot.update()
            #self.root.update()
            #rexRoot = self.root
            # print("rexui.rexRoot.update passed")
         # except:
            # rrFailed = True
            # print("rexui.rexRoot.update failed")
            
         if abort("get"):
            break
         if _pause == False:
            print('Resuming testing...')
            break
         self.rootn.update()
         #root.update()
         #time.sleep(1)
      return 1
      
# 5/13, indented and added self, but issues now with rex.
def pause(getSet):
   # 
   global _pause
   # getSet == "get":
   if getSet == "get":
      return _pause
   elif getSet == "softSet":
      #print("pause softSet")
      _pause = True
      return True
   elif getSet == "set":
      _pause = True
      print("pause set")
         
      try:
         # or self or something?
         noop = 1
         #conns['cli1']._innerPause()
      except Exception as msg:  
         print("      --- p error begin ---")
         print(msg)
         print("      --- p error end ---")
         failed_test = True
      except AssertionError as msg:  
         print("      --- p error begin ---")
         print(msg)
         print("      --- p error end ---")
      #_pause = True
      return True
   elif getSet == "clear":
      _pause = False
      return False
   else:
      print("Invalid getSet data passed to vsh.pause")
      return 0
   return 1
   
def sleep(secs):
   tnow = time.time()
   tstart = time.time()
   while tnow < tstart + secs:
      time.sleep(.2)
      tnow = time.time()

      
def _sim(getSet):
   # 
   global _simMode
   if getSet == "get":
      return _simMode
   elif getSet == "set":
      _simMode = True
   elif getSet == "clear":
      _simMode = False
   else:
      print("Invalid getSet data passed to vsh.sim")
      return 0
   return 1
   
def sim(getSet):
   return _sim(getSet)
   
def vabort(getSet):
   # 
   global _aborti
   
   if getSet == "get":
      return _aborti
   elif getSet == "set":
      _aborti = True
   elif getSet == "clear":
      _aborti = False
   else:
      print("Invalid getSet data passed to vsh.abort -",getSet,"-")
      return 0
      
   #rex.log("in vsh abort getSet " + getSet + str(_aborti))
   return 1

def disconnect(handle):
    """
    ----------------------
        disconnect("<handle name>")
    
    Method to close a session by its handle name. The handles are created by create_handle function 

        Parameter:
        session handle name -> str        
        This is the session handle created by **create_handle()** method
    **Example :**
        `disconnect('cli1')  # closes a session with handle name 'cli1'
                 disconnect('netconf1')  # closes a session with handle name 'netconf1'
                 disconnect('all')  # closes ALL sessions which are active`
    ----------------------
    """
    global connsdb
    global conns

    pQueue = pixi.PIXIQueue()
    if handle == 'all':
        for id in conns:
            try:
                if connsdb[id][0] in conns[id].chan:
                    conns[id].chan[connsdb[id][0]].close()
                if connsdb[id][0] in conns[id].ssh:
                    if type(conns[id].ssh[connsdb[id][0]]).__name__ == 'SSHClient':
                        conns[id].ssh[connsdb[id][0]].close()
                    elif type(conns[id].ssh[connsdb[id][0]]).__name__ == 'Manager':
                        conns[id].ssh[connsdb[id][0]].close_session()
                    elif type(conns[id].ssh[connsdb[id][0]]).__name__ == 'Session':
                        conns[id].ssh[connsdb[id][0]].close()
            except:
                noop = 1
            try:    
                rootn = "root" + str(connsdb[id][0])
                pQueue.put({"command": "destroy_window", "data": {"handle": id}})
                #conns[id].rootn.destroy()
            except:
                noop = 1
        connsdb.clear()
        conns.clear()
    else:
        try:
           rootn = "root" + str(connsdb[handle][0])
           pQueue.put({"command": "destroy_window", "data": {"handle": handle}})
           #conns[handle].rootn.destroy()
        except:
           noop = 1

        try:
            if type(conns[handle].ssh[connsdb[handle][0]]).__name__ == 'SSHClient':
                if connsdb[handle][0] in conns[handle].chan:
                    conns[handle].chan[connsdb[handle][0]].close()
                if connsdb[handle][0] in conns[handle].ssh:
                    conns[handle].ssh[connsdb[handle][0]].close()
            if type(conns[handle].ssh[connsdb[handle][0]]).__name__ == 'Manager':
                conns[handle].ssh[connsdb[handle][0]].close_session()
            if type(conns[handle].ssh[connsdb[handle][0]]).__name__ == 'Session':
                conns[handle].ssh[connsdb[handle][0]].close()
        except:
            noop = 1
        try:
            connsdb.pop(handle)
            conns.pop(handle)
        except:
            noop = 1        

def _plot_table(filename = None):
    df = pd.read_csv(filename)
    df["DateTime"] = pd.to_datetime(df["DateTime"])
    print()
    pm_min = df['pm-value-min'].values
    pm_max = df['pm-value-max'].values
    pm_val = df['pm-value'].values
    timeX = df['DateTime'].values
    # figplt = go.Figure()
    # figplt.add_trace(go.Scatter(x=timeX, y=pm_min,mode='lines',name='trend',line=dict(color="#f54242")))
    # figplt.add_trace(go.Scatter(x=timeX, y=pm_max,mode='markers',name='Data',line=dict(color="#4287f5")))
    # figplt.add_trace(go.Scatter(x=timeX, y=pm_val,mode='markers',name='Data',line=dict(color="#089c1e")))
    # config = {'displaylogo': False,'showSendToCloud' : False,'scrollZoom' : True,'modeBarButtonsToRemove' : ['pan2d','select2d','lasso2d','resetScale2d']}
    # figplt.update_layout(
    #     title_text="Plot Data - "+ filename,
    #     showlegend=True,
    # )
    # figplt.write_html('graphs\\'+filename+'.html', auto_open=False,config=config)
    url = "file://graphs/"+filename+".html"
    webbrowser.open(url,new=2)
    return 1

def create_handle(handle):
    """
    ----------------------
        create_handle("<handle name>")
    
    Method to create a unique handle for a NE

        Parameters:
        Session handle name -> str

    **Example :**
        `create_handle('cli1')`
    ----------------------
    """    
    if handle not in conns:
        conns[handle] = []
        connsdb[handle] = []
        handlestr1 = ''.join(random.choices(string.ascii_letters+string.digits,k=5))
        handlestr2 = ''.join(random.choices(string.ascii_letters+string.digits,k=5))
        conns[handle].append (handlestr1)
        conns[handle].append (handlestr2)
        connsdb[handle].append (handlestr1)
        connsdb[handle].append (handlestr2)
    else:
        print("handle ",handle," already exists!")
        return None

    conns[handle] = Vsh(conns[handle][0], conns[handle][1], handle)
    plogger.pixie_logger(logtype = "vsh", logger_name = handle)
    print(f"In vsh.py file {conns[handle]}")
    return conns[handle]

# !!!
_pause = False
_aborti = False
print("imported vsh")
_simMode = True
_simMode = False
conns = {}
connsdb = {}