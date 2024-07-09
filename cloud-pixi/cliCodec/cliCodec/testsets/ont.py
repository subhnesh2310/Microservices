import telnetlib
import time
from cliCodec.libs import plogger

class ONT(object):
    def __init__(self, logger_handle, ipaddress, ont_portConf="DUAL_PORT", ont_mode="TERM", tsRate=None,
                 chassis=None, slot=None, port=None,  port_type=None):
        self.logger_handle = logger_handle
        ont_mgmt_port = 5001
        self.ipaddress = ipaddress
        self.chassis = str(chassis)
        self.slot = str(slot)
        self.port = str(port)
        self.port_Conf = ont_portConf
        self.device_Mode = ont_mode
        self.tsRate = tsRate
        self.port_type = port_type
        try:
            mgmttn = telnetlib.Telnet(self.ipaddress, ont_mgmt_port)
            # mgmttn.set_debuglevel(10)
            msg = "Session to TestSet [ IP-Address {} and Port {} ] has been established".format(self.ipaddress, ont_mgmt_port)
            print (msg)
            plogger.debug_log(handle = logger_handle ,msg = msg )
            
        except Exception as e:
            exp_msg = "FAILED : Please check IP connectivity to chassis " + str(e)
            print (exp_msg)
            plogger.error_log(handle = logger_handle ,msg = exp_msg )
        tsport = self._getWorkingPort(logger_handle ,tnObj=mgmttn)
        self.telnet_working_port = tsport
        mgmttn.close()
        try:
            self.tn = telnetlib.Telnet(self.ipaddress, int(tsport))
            # self.tn.set_debuglevel(30)
            # Wait for the system to be up for remote commands
            msg = "Telnet session to TestSet IPAddress {} and Working Port {} has been established".format(self.ipaddress, tsport)
            print (msg)
            plogger.debug_log(handle = logger_handle ,msg = msg )
        
        except Exception as e:
            exp_msg = "FAILED : TestSet {} at {} is not reachable after reboot:{}".format(self.ipaddress, tsport, e)
            print (exp_msg)
            plogger.error_log(handle = logger_handle ,msg = exp_msg )
    
    def help():
        """
            --------------------

            Method to find the module help doc

            <a href="https://infinera.sharepoint.com/:f:/s/service-so/techops/EggTl_d9kGhLp8qNPWs2YYwBHD789gvKyODvhwGTJaXWMQ?e=97l7kr">ONT Test Set Documents Folder</a>

            --------------------
        """
        # os.path.join(testDir, testListFile)
        noop=1

    def _getWorkingPort(self, logger_handle ,tnObj):
        try:
            workingport = None
            # time.sleep(10)
            # Turn on the prompt
            tnObj.write(b'\r\n*PROMPT ON\r\n')
            tnObj.write(b':PRTM:LIST?\r\n')
            time.sleep(10)
            output = tnObj.read_very_eager()
            output = output.decode("utf-8")
            output = output.replace('>', '').replace('\n', '').strip()
            ports = output.split(",")
            for pt in ports:
                try: 
                    mychassis = pt.split(":")[0].split('/')[1]
                    myslot = pt.split(":")[0].split('/')[2]
                    myport = pt.split(":")[0].split('/')[3]
                except ValueError:
                    exp_msg = "FAILED : Exeception in getting port,Please check for number of clients logged into the testset"
                    print(exp_msg)
                    plogger.error_log(handle = logger_handle ,msg = exp_msg )
                    break
                if mychassis == self.chassis and myslot == self.slot and myport == self.port:
                    workingport = pt.split(":")[1]
                    break
                else:
                    msg = "chassis : {} , slot : {} ,port : {}".format(mychassis,myslot,myport)
                    plogger.debug_log(handle = logger_handle ,msg = msg )
            return workingport
        except Exception as e:
            exp_msg = "FAILED : Exeception in getting respons from testset " + str(e)
            print(exp_msg)
            plogger.debug_log(handle = logger_handle ,msg = exp_msg )

    def sendCommand(self, logger_handle,cmd, waittime=2):
        plogger.debug_log(handle = logger_handle ,msg = "send command :  {}".format(cmd) )
        self.tn.write((cmd + "\n").encode('ascii'))
        time.sleep(waittime)
        output = self.tn.read_very_eager().decode('ascii')
        plogger.debug_log(handle = logger_handle ,msg = "received output :  {}".format(output) )
        return output


    def configureTestset(self, logger_handle , rate, FrameSize=256, mapping=None):
        self.tn.write(b"*PROMPT ON\n")
        self.tn.read_until(b">",timeout = 10)
        self.tn.write(b"\n")

        output = self.sendCommand(logger_handle, ":INST:CAT?")
        # if self.tslogger: self.tsprint('Output of INST:CAT? is %s' % output)
        if not 'New-Application' in output:
            # Load the Application
            self.sendCommand(logger_handle,":INST:LOAD \"New-Application\"", waittime=10)
            self.sendCommand(logger_handle,"*OPC?")

        result = 'SUCCESS ,Successfully set the configuration to Rate= {}'.format(rate)
        plogger.debug_log(handle = logger_handle ,msg = result )
        # Rate mapping Dict
        rate_mapper = {
            "100GBE": "PHYS_PCSL_MAC",
            "OTU4": "PHYS_OTL4_OTN"
        }

        if rate == "100GBE" and self.tsRate == "100GBE_SR4FEC":
            rate = self.tsRate
            print("Testset rate taken from Yml file..: ")
            # print(rate)
        stacVal = rate_mapper[rate]
        
        self.sendCommand(logger_handle,':ABOR;*WAI', waittime=2)

        # Applying configuration parameters from Environment file
        print ("*** Applying configuration parameters read from input.yaml file ***")
        self.sendCommand(logger_handle,':INST:CONF:EDIT:OPEN ON', waittime=5)
        self.sendCommand(logger_handle,':INST:CONF:EDIT:PORT:CONF ' + str(self.port_Conf), waittime=2)
        self.sendCommand(logger_handle,':INST:CONF:EDIT:DEV:MODE ' + str(self.device_Mode))

        config_type = self.sendCommand(logger_handle,':INST:CONF:EDIT:LAY:STAC?')

        output = self.sendCommand(logger_handle,':INST:CONF:EDIT:LAY:STAC %s' % stacVal, waittime=2)
        if stacVal not in output:
            config_result = "FinalResult:FAILED"

        # Applying configuration
        print ("*** Applying configuration ***")
        if config_type == stacVal:
            output = self.sendCommand(logger_handle , ':INST:CONF:EDIT:APPL ON', waittime=5)
        else:
            output = self.sendCommand(logger_handle , ':INST:CONF:EDIT:APPL ON', waittime=60)

        # Configuring Payload Rate
        print ("*** Configuring Payload Rate ***")
        result_msg = self.configPayloadRate(logger_handle, rate)
        plogger.debug_log(handle = logger_handle ,msg = result_msg )
        # print(result_msg)
        if "FAILED" in result_msg:
            print ( result_msg)
            return result_msg

        # Enabling Service Disruption
        result_msg = self.__enableServiceDisruption(logger_handle)
        plogger.debug_log(handle = logger_handle ,msg = result_msg )
        # print(result_msg)
        if "FAILED" in result_msg:
            print ( result_msg)
            return result_msg

        # Configuring GBE related config
        print ("*** Configuring GBE related config ***")
        if "MAC" in stacVal:
            result_msg = self.__configureGbeParams(logger_handle,FrameSize)
            plogger.debug_log(handle = logger_handle ,msg = result_msg )
            # print(result_msg)
            if "FAILED" in result_msg:
                print ( result_msg)
                return result_msg

        self.clear_alarms_errors(logger_handle)

        # Enabling laser state
        print ("*** Turning ON the Laser ***")
        self.sendCommand(logger_handle,'OUTP:TEL:PHYS:LINE:OPT:STAT ON', waittime=5)

        #
        # if self.port_type and self.port_type != "None" and self.port_type != "none":
        #     self.sendCommand(logger_handle,":OUTP:TEL:PHYS:LINE:TYPE %s" % self.port_type)

        # Starting measurement
        print ("*** Starting the Test Measurement ***")
        self.sendCommand(logger_handle,':INIT:IMM:ALL;*WAI', waittime=4)

        # Refreshing alarms
        print ("*** Refreshing the alarms ***")
        self.sendCommand(logger_handle,":ABOR;*WAI;:INIT:IMM:ALL;*WAI", waittime=2)
        plogger.debug_log(handle = logger_handle ,msg = result)
        # print(result)
        # return result
        return True

    def configPayloadRate(self,logger_handle,rate):
        print("*** Configuring payload rate ***")
        plogger.debug_log(handle = logger_handle ,msg = "************ Configuring payload rate *******************" )
        rate = str(rate)
        config_type = self.sendCommand(logger_handle,':INST:CONF:EDIT:LAY:STAC?')
        if "_" in rate:
            rate_type = rate.split("_")
            msg = "layers in list: {}".format(rate_type)
            plogger.debug_log(handle = logger_handle,msg = msg)
            trate = rate_type[0]
            gmp_rate = rate_type[-1]
        else:
            trate = rate
            gmp_rate = None

        trate_map = {"OTU1":"OTU1","OTU1E":"OTU2_LAN_1105","OTU2":"OTU2_107","OTU2E":"OTU2_LAN_1110",
                     "OTU1F":"OTU2_FC_1127","OTU2F":"OTU2_FC_1132","OTU4":"OTU4","OTU3":"OTU3","OTU3E1":"OTU3_E1",
                     "OTU3E2":"OTU3_E2",

                     "OC3":"OC3","OC12":"OC12","OC48":"OC48","OC192":"OC192","STM1":"OC3","STM4":"OC12",
                     "STM16":"OC48","STM64":"OC192",
                     
                     "40GBE":"ETH_40G","100GBE":"ETH_100G","10GBE":"BASE10G_LAN","1GBE":"BASE1000",
                     "10GFC":"FC10G","400GBE":"ETH_400G"}

        gmp_map = {"OC3": "STM1_STS3", "STM1": "STM1_STS3", "OC12": "STM4_STS12", "STM4": "STM4_STS12"}

        cm_tx = ':SOUR:DATA:TEL:PHYS:LINE:RATE %s'%trate_map[trate]
        self.sendCommand(logger_handle,cm_tx, waittime=5)

        cm_rx = ':SENS:DATA:TEL:PHYS:LINE:RATE %s'%trate_map[trate]
        self.sendCommand(logger_handle,cm_rx, waittime=5)

        if "ODU" in config_type and "ODUMC" not in config_type:
            mux_typel1 = rate_type[1]
            if "ODU_ODU" in config_type:
                mux_typel2 = rate_type[2]
            else:
                mux_typel2 = None
        else:
            mux_typel1= None
            mux_typel2 = None

        if mux_typel1 :
            mux_tx = ':SOUR:DATA:TEL:OTN:OTU:MUX:TYPE %s' % mux_typel1
            self.sendCommand(logger_handle,mux_tx, waittime=5)
            mux_rx = ':SENS:DATA:TEL:OTN:OTU:MUX:TYPE %s' % mux_typel1
            self.sendCommand(logger_handle,mux_rx, waittime=5)
        if mux_typel2:
            mux_tx = ':SOUR:DATA:TEL:OTN:ODU:MUX:TYPE %s' % mux_typel2
            self.sendCommand(logger_handle,mux_tx, waittime=5)
            mux_rx = ':SENS:DATA:TEL:OTN:ODU:MUX:TYPE %s' % mux_typel2
            self.sendCommand(logger_handle,mux_rx, waittime=5)
        if gmp_rate in gmp_map:
            gmp_tx = ':SOUR:DATA:TEL:OTN:ODU:SEL:GMP:CLI:TYPE %s' % gmp_map[gmp_rate]
            self.sendCommand(logger_handle,gmp_tx, waittime=5)
            gmp_rx = ':SENS:DATA:TEL:OTN:ODU:SEL:GMP:CLI:TYPE %s' % gmp_map[gmp_rate]
            self.sendCommand(logger_handle,gmp_rx, waittime=5)

        result_msg="Payload rate and mux type configured successfully"
        return result_msg

    def __enableServiceDisruption(self,logger_handle):

        # print("************Enabling Service disruption *******************")
        config_type = self.sendCommand(logger_handle,':INST:CONF:EDIT:LAY:STAC?')
        layer_stack = (self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")).split('\n')[0].split('>')[-1]
        # msg = "Layer Stack :' {} '".format(layer_stack)
        # plogger.debug_log(handle = logger_handle ,msg = msg)
        layer_type = layer_stack.split("_")
        # msg = "layers in list: {}".format(layer_type)
        # plogger.debug_log(handle = logger_handle ,msg = msg)
        result_msg = "Service disruption enabled on all layer "
        if "ODU" in config_type and "ODUMC" not in config_type:
            if "ODU_ODU" in config_type or "ODU3_ODU" in config_type:
                for i in range(len(layer_type)):
                    if layer_type[i] == "ODU" or layer_type[i] == "ODU3" :
                        layer_type[i] = "ODUL1"
                        if layer_type[i+1] == "ODU":
                            layer_type[i+1] = "ODUL2"
                            break
            else:
                for i in range(len(layer_type)):
                    if layer_type[i] == "ODU" or layer_type[i] == "ODU3" :
                        layer_type[i] = "ODUL1"
                        break

        #print("layers in list:%s" % (layer_type))
        
        command_map = {"SON":"SON","SDH":"SDH","OTN":"OTN:OTU","ODUMC":"OTN:ODUM","ODUL1":"OTN:ODU","ODUL2":"OTN:ODUL2"}

        if "PCSL" in config_type:
            self.sendCommand(logger_handle,":SENS:DATA:TEL:PCS:SDIS:EVAL:STAT ON")
            self.sendCommand(logger_handle,":SENS:DATA:TEL:MAC:SDIS:EVAL:STAT ON")
        if "PCS400G" in config_type:
            self.sendCommand(logger_handle,":SENS:DATA:TEL:MAC:SDIS:EVAL:STAT ON")

        for layer in layer_type:
            if layer in ["PHYS","PCS","PCSL","PCS1G","PCS400G","MAC","GFP","OTL4","OTL3","SR4FEC","FC2","KR4FEC"]:
                pass
            else:
                if layer not in command_map:
                    result_msg = "FinalResult:FAILED :Servie disruption enable failed "
                    return result_msg
                self.sendCommand(logger_handle,":SENS:DATA:TEL:%s:SDIS:MODE ON" %command_map[layer] )

        return result_msg
    
    def __configureGbeParams(self,logger_handle,FrameSize):
        print( "*** Configuring 100GBE traffic ***")
        plogger.debug_log(handle = logger_handle ,msg = "************ Configuring 100GBE traffic *******************")
        stacVal = self.sendCommand(logger_handle,':INST:CONF:EDIT:LAY:STAC?')
        result_msg = 'Successfully configured GBE traffic parameters'

        ##Seting frame size for GBE traffic
        if FrameSize :
            result = self.configGbeFrameSize(logger_handle,FrameSize)

        #### Start traffic in case of MAC
        if "PCS" in stacVal:

            self.sendCommand(logger_handle,':SOUR:DATA:TEL:MAC:TRAF:STAT ON', waittime=4)
            self.sendCommand(logger_handle,':SOUR:DATA:TEL:MAC:TRAF:SCAL SCALED', waittime=3)
            self.sendCommand(logger_handle,':SOUR:DATA:TEL:MAC:TRAF:BAND:USER:PERC 1.0000000e+02', waittime=3)
            self.sendCommand(logger_handle,':SENS:DATA:TEL:MAC:PAYL:QOS:EVAL:NFTF OFF', waittime=4)
        return result_msg

    def release(self, logger_handle,slot=None, port=None):
        try:
            print("*** ONT - release in progress ***")
            plogger.debug_log(handle = logger_handle,msg = "************ ont - release in progress *******************")
            self.sendCommand(logger_handle,":INST:DEL \"New-Application\"", waittime=10)
            self.sendCommand(logger_handle,"*OPC?")
            self.tn.close()
            self.tn = None
            print("*** ont - release completed ***")
            plogger.debug_log(handle =logger_handle,msg = "************ ont - release completed *******************")
            return 'FinalResult:SUCCESS'
        except Exception as e:
            exp_msg = "Exception in release test set - {}".format(e)
            plogger.error_log(handle =logger_handle,msg = exp_msg)
            return 'FinalResult:FAILED'


    def releaseOnly(self, logger_handle,slot=None, port=None):
        try:
            print("*** ONT - release in progress ***")
            plogger.debug_log(handle = logger_handle,msg = "************ ont - release in progress *******************")
            self.tn.close()
            self.tn = None
            print("*** ont - release completed ***")
            plogger.debug_log(handle =logger_handle,msg = "************ ont - release completed *******************")
            return 'FinalResult:SUCCESS'
        except Exception as e:
            exp_msg = "Exception in release test set - {}".format(e)
            plogger.error_log(handle =logger_handle,msg = exp_msg)
            return 'FinalResult:FAILED'

    def configGbeFrameSize(self,logger_handle,FrameSize):
        print("*** Configuring GBE traffic frame size ***")
        plogger.debug_log(handle = logger_handle ,msg = "************ Configuring GBE traffic frame size *******************")

        result_msg = 'SUCCESS : Successfully configured frame size to %s\n' %FrameSize
        config_type = self.sendCommand(logger_handle,':INST:CONF:EDIT:LAY:STAC?')
        FrameSize = int(FrameSize)
        value = self.sendCommand(logger_handle,":SOUR:DATA:TEL:MAC:TRAF:SEL:FRAM:OVER?")
        if "PCSL" in config_type or "PCS400G" in config_type:
            if FrameSize > 2000 and value == "OFF":
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:MAC:TRAF:SEL:FRAM:OVER ON")
            elif FrameSize <= 2000 and value == "ON":
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:MAC:TRAF:SEL:FRAM:OVER OFF")

            self.sendCommand(logger_handle,":SOUR:DATA:TEL:MAC:TRAF:SEL:FRAM:SIZE:MODE FIX")
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:MAC:TRAF:SEL:FRAM:SIZE %s" % (FrameSize))

        #elif "PHYS_PCS_MAC" in config_type:
        else:
            if FrameSize > 1518 and value == "OFF":
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:MAC:TRAF:SEL:FRAM:OVER ON")
            elif FrameSize <= 1518 and value == "ON":
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:MAC:TRAF:SEL:FRAM:OVER OFF")

            self.sendCommand(logger_handle,":SOUR:DATA:TEL:MAC:TRAF:SEL:FRAM:SIZE:MODE FIX")
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:MAC:TRAF:SEL:FRAM:SIZE %s" % (FrameSize))
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:MAC:TRAF:EDIT:OK")

        msg = "Frame Size Configured Successfully to : {}".format(FrameSize)
        plogger.debug_log(handle =logger_handle,msg = msg)
        return result_msg
        
        
    def clear_alarms_errors(self,logger_handle):
        try:
            success_result_msg = "SUCCESS"
            fail_result_msg = 'FAILED'
            final_result_flag = 1

            print("*** Clear all alarms and errors ***")
            plogger.debug_log(handle =logger_handle,msg = "************ clear all alarms and errors *******************")
            layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")
            if layer_val is not None:
                alarm = "CLEAR_ALL"
                error = "CLEAR_ALL"
                layer_stack = layer_val.split("_")
                for lay in layer_stack:
                    if "\n>" in lay:
                        lay = lay.replace("\n>","")
                    if 'OTL' in lay:
                        lay = lay[:-1]
                    if lay != "MAC":
                        res1 = self.clearAlarm(logger_handle,Alarm=alarm, Layer=lay)
                    else:
                        res1 = success_result_msg
                    if lay != "PHYS":
                        res2 = self.clearError(logger_handle,Error=error, Layer=lay, lane="None")
                    else:
                        res2 = success_result_msg
                    if success_result_msg in res1 and success_result_msg in res2:
                        final_result_flag = final_result_flag * 1
                    else:
                        final_result_flag = final_result_flag * 0
                if final_result_flag == 1:
                    return success_result_msg
                else:
                    return fail_result_msg

            else:
                return fail_result_msg + " Failed to get the clear_alarms_errors"
        except Exception as e:
            result_msg = 'FAILED ' + str(e)
            plogger.error_log(handle =logger_handle,msg = result_msg)
            return result_msg

    def insertAlarm(self,logger_handle, Alarm,Layer,Duration=0,Mode="CONT",ActAlarmFrame=0,InactiveAlarmFrame=0,CH=None):
        alarm = Alarm.upper()
        dur = int(Duration)
        mode = Mode
        channel = str(CH)
        layer = Layer.upper()
        ActAlarmFrame = int(ActAlarmFrame)
        InactiveAlarmFrame = int(InactiveAlarmFrame)

        result_msg = "SUCCESS, Alarm :%s inserted successfully on layer:%s" % (alarm, layer)

        layer_map = {
            "PHYS": self.__insertAlarmPhys,
            "PCS": self.__insertAlarmPcs,
            "MAC":self.__insertAlarmMac,
            "OTL": self.__insertAlarmOtl,
            "OTN": self.__insertAlarmOtn
        }

        result = layer_map[layer](logger_handle,alarm,dur,mode,ActAlarmFrame,InactiveAlarmFrame,channel)
        if "FAILED" in result:
            return result

        return result_msg

    def insertError(self,logger_handle, Error, Layer, Mode, Duration, Rate, ActErrorFrame=0, InactErrorFrame=0,extraParam=None,lane=None, CH=None):
        error = Error.upper()
        rate = str(Rate)
        dur = int(Duration)
        mode = Mode.upper()
        channel = str(CH)
        layer = Layer.upper()
        ActErrorFrame = int(ActErrorFrame)
        InactErrorFrame = int(InactErrorFrame)

        result_msg = "SUCCESS: Error type = {} inserted successfully on layer:{}".format(error, layer)

        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")

        layer_map = {
            "PHYS": self.__insertErrorPhys,
            "OTL": self.__insertErrorOtl,
            "OTN": self.__insertErrorOtn,
            "PCS": self.__insertErrorPcs,
            "MAC": self.__insertErrorMac
        }
        result = layer_map[layer](logger_handle,error, rate, dur, mode, ActErrorFrame, InactErrorFrame, lane, channel)
        if "FAILED" in result:
            return result

        return result_msg


    def getLayerAlarms(self,logger_handle, Layer):
        layer = Layer.upper()

        layer_map = {
            "PHYS": self.__getAlarmPhys,
            "OTL": self.__getAlarmOtl,
            "OTN": self.__getAlarmOtn,
            "PCS": self.__getAlarmPcs,
            "MAC": self.__getAlarmMac
        }
        result = layer_map[layer](logger_handle)
        result_msg = result
        if "FAILED" in result['status']:
            plogger.info_log(handle =logger_handle,msg = "****** FAILED: Error while retreiving Alarms at the {} Layer ******".format(layer))
        else:
            plogger.info_log(handle =logger_handle,msg = "****** SUCCESS : Retreived alarms at {} Layer ******".format(layer))
        plogger.info_log(handle =logger_handle,msg = result_msg)
        return result_msg


    def clearAlarm(self, logger_handle,Alarm, Layer, CH=None):
        alarm = Alarm.upper()
        channel = str(CH)
        layer = Layer.upper()

        result_msg = "SUCCESS, Alarm :%s cleared successfully on layer:%s" % (alarm, layer)

        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")

        layer_map = {
            "PHYS": self.__clearAlarmPhys,
            "MAC": self.__clearAlarmMac,
            "PCSL": self.__clearAlarmPcs,
            "OTL": self.__clearAlarmOtl,
            "OTN": self.__clearAlarmOtn
        }

        if Alarm == "CLEAR_ALL":
            result = layer_map[layer](logger_handle,alarm, channel)
            return result

        if (layer not in layer_val and layer != "ODUL2") and (layer not in layer_val and layer != "ODUL1"):
            result_msg = "FAILED :Provided layer is not part of configured Testset "
            return result_msg

        elif layer not in layer_map:
            result_msg = "FAILED :Provided layer is not supported"
            return result_msg

        else:
            result = layer_map[layer](logger_handle,alarm, channel)
            if "FAILED" in result:
                return result

        return result_msg

    def __clearAlarmPhys(self, logger_handle,alarm, CH):

        msg = "************ Clearing Alarm on PHYS Layer *******************"
        plogger.info_log(handle =logger_handle,msg = msg)
        layer = "PHYS"
        layer_cmd = "PHYS:LINE"
        result_msg = "SUCCESS"
        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")
        alarm_list = self.__getAlarmList( alarm, layer)

        # if alarm in alarm_list:
        #     if "PCS400G" in layer_val:
        #         if self.ontmodel == "ONT_804":
        #             layer_cmd = "PHYS:MULT:PHY"
        # else:
        #     result_msg = "FAILED :Provided alarm is not part of PHYS layer"
        #     return result_msg

        result = self.__clearAlarm(logger_handle,alarm, layer_cmd)
        if "FAILED" in result:
            return result

        return result_msg

    def __clearAlarmMac(self, logger_handle,alarm, CH):

        msg = "************ Clearing Alarm on MAC Layer *******************"
        plogger.info_log(handle =logger_handle,msg = msg)


        layer = "MAC"
        layer_cmd = "MAC"
        result_msg = "SUCCESS"
        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")

        alarm_list = self.__getAlarmList(alarm, layer)

        if alarm not in alarm_list:
            result_msg = "FAILED :Provided alarm is not part of MAC layer"
            return result_msg

        status = self.sendCommand(logger_handle,":SOUR:DATA:TEL:%s:TRAF:STAT?" % layer_cmd, waittime=2)

        if status == "ON":
            result_msg = "FAILED :Alarm is not inserted or already cleared "
            return result_msg
        else:
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:%s:TRAF:STAT ON" % layer_cmd, waittime=2)

        return result_msg

    def __clearAlarmPcs(self, logger_handle,alarm, CH):

        msg = "************ Clearing Alarm on PCS Layer *******************"
        plogger.info_log(handle =logger_handle,msg = msg)
        layer = "PCS"
        layer_cmd = "PCS"
        result_msg = "SUCCESS"
        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")

        alarm_list = self.__getAlarmList(alarm, layer)

        if alarm not in alarm_list :
            result_msg = "FAILED :Provided alarm is not part of PCS layer"
            return result_msg

        if alarm == "LOA":
            result = self.setPcsSkewOnAllLanes(logger_handle,value=0)
            if "FAILED" in result:
                return result
            return result_msg

        elif alarm == "LOLM" :

            if "PCSL" in layer_val:
                # 100G case
                if "FEC" in layer_val:
                    layer_cmd = "FEC:LANE"
                else:
                    layer_cmd = "PCS:LANE"
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:%s:ALAR:INS OFF" % layer_cmd, waittime=2)
                return result_msg

            if "PCS400G" in layer_val:
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:%s:ALAR:INS OFF" % layer_cmd, waittime=2)
                return result_msg

        elif alarm == "LOAMPS":
            if "PCS400G" in layer_val:
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:%s:ALAR:INS OFF" % layer_cmd, waittime=2)
                return result_msg
            else:
                result_msg = "FAILED :Provided alarm is not part of PCS layer"
                return result_msg

        else:
            if alarm in ["LOC_FAULT", "REM_FAULT"]:
                layer_cmd = "PCS:RS"

            if "PCSL" in layer_val and alarm in ["LOBL", "LOAML","CLEAR_ALL"]:
                layer_cmd = "PCS:LANE"

            if "PCS400G" in layer_val:
                if alarm in ["LOC_DSER", "REM_DSER", "HSER"]:
                    layer_cmd = "PCS:FEC"

            result = self.__clearAlarm(logger_handle,alarm, layer_cmd)
            if "FAILED" in result:
                return result

        return result_msg

    def __clearAlarmOtl(self, logger_handle,alarm, CH):

        msg = "************ Clearing Alarm on OTL4 Layer *******************"
        plogger.info_log(handle =logger_handle,msg = msg)
        layer = "OTL"
        layer_cmd = "OTL"
        result_msg = "SUCCESS"
        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")
        alarm_list = self.__getAlarmList( alarm, layer)

        result = self.__clearAlarm(logger_handle,alarm, layer_cmd)
        if "FAILED" in result:
            return result

        return result_msg

    def __clearAlarmOtn(self, logger_handle,alarm, CH):

        msg = "************ Clearing Alarm on OTL4 Layer *******************"
        plogger.info_log(handle =logger_handle,msg = msg)
        layer = "OTN"
        layer_cmd = "OTN:OTU"
        result_msg = "SUCCESS"
        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")
        alarm_list = self.__getAlarmList( alarm, layer)

        result = self.__clearAlarm(logger_handle,alarm, layer_cmd)
        if "FAILED" in result:
            return result

        return result_msg
    
    def __getAlarmList(self, alarm, layer):

        alarm = alarm
        layer = layer

        phys_alarm = ["LOS"]

        pcs_alarm = ["LOBL", "LOAML", "HIBER", "LOC_FAULT", "REM_FAULT", "LOAMPS", "LOC_DSER",
                     "REM_DSER", "HSER", "LOA", "LOLM"]

        otl_alarm = ["LOFOTL", "OOFOTL"]

        otn_alarm = ["OTU_AIS", "LOF", "OOF", "LOM", "OOM", "SM_IAE", "SM_TIM", "SM_BDI", "SM_BIAE", "ODU_AIS",
                     "ODU_OCI", "ODU_LCK", "PM_TIM", "PM_BDI", "SIGNAL_FAIL_FW", "SIGNAL_DEG_FW", "SIGNAL_FAIL_BW",
                     "SIGNAL_DEG_BW", "CSF", "LOMFI", "OOMFI"]

        otn_tcm_alarm = []
        for i in range(1, 7):
            for alm in ["LTC", "IAE", "TIM", "BDI", "BIAE"]:
                otn_tcm_alarm.append(f"TCM{str(i)}_{alm}")
        otn_alarm = otn_alarm + otn_tcm_alarm

        fec_alarm = ["LOAMPS"]

        mac_alarm = ["IFS"]

        check_alarm_map = {
            "PHYS": phys_alarm,
            "PCS": pcs_alarm,
            "OTL": otl_alarm,
            "OTN": otn_alarm,
            "FEC": fec_alarm,
            "MAC": mac_alarm
        }

        check_alarm_map[layer].append("CLEAR_ALL")
        return check_alarm_map[layer]
        
        
    def __clearAlarm(self, logger_handle,alarm, cmd):

        msg = "************ Clearing  Alarm *******************"
        plogger.info_log(handle =logger_handle,msg = msg)
        alarm = alarm
        layer_cmd = cmd
        result_msg = "SUCCESS"

        if alarm == "CLEAR_ALL":
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:%s:ALAR:INS OFF" % layer_cmd, waittime=2)
            return result_msg

        status = self.sendCommand(logger_handle,":SOUR:DATA:TEL:%s:ALAR:INS?" % layer_cmd, waittime=2)

        if status == "OFF":
            result_msg = "FAILED :Alarm is not inserted or already cleared "
            return result_msg
        else:
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:%s:ALAR:INS OFF" % layer_cmd, waittime=2)

        return result_msg
    
    
    def clearError(self, logger_handle,Error, Layer, lane, CH=None):
        error = Error.upper()
        channel = str(CH)
        layer = Layer.upper()

        result_msg = "SUCCESS, Error :%s cleared successfully on layer:%s" % (error, layer)

        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")

        layer_map = {
            "PHYS": self.__clearErrorPhys,
            "MAC": self.__clearErrorMac,
            "PCSL": self.__clearErrorPcs,
            "OTL": self.__clearErrorOtl,
            "OTN": self.__clearErrorOtn
        }

        if Error == "CLEAR_ALL":
            result = layer_map[layer](logger_handle,error, lane, channel)
            return result

        if (layer not in layer_val and layer != "ODUL2") and (layer not in layer_val and layer != "ODUL1"):
            result_msg = "FAILED :Provided layer is not part of configured Testset "
            return result_msg

        elif layer not in layer_map:
            result_msg = "FAILED :Provided layer is not supported"
            return result_msg

        else:
            result = layer_map[layer](logger_handle,error, lane, channel)
            if "FAILED" in result:
                return result

        return result_msg

    def setPcsSkewOnAllLanes(self,logger_handle,value):
        msg = "************ Configuring PCS virtual lane Skew *******************"
        plogger.info_log(handle =logger_handle,msg = msg)
        stacVal = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")
        value = value
        defaultValue = 0
        result_msg = "SUCCESS : Successfully configured PCS Skew to all virtual lanes with value: %s"%(value)

        if "PCSL" in stacVal:
            if str(value):
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:PCS:VL:SKEW:BLOC %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                                 "%s,%s,%s,%s,%s,%s,%s,%s,%s"%(value,defaultValue,defaultValue,defaultValue,defaultValue,
                                                               defaultValue,defaultValue,defaultValue,defaultValue,
                                                               defaultValue,defaultValue,defaultValue,defaultValue,
                                                               defaultValue,defaultValue,defaultValue,defaultValue,defaultValue,
                                                               defaultValue,defaultValue), waittime=10)

            else :
                result_msg = "FAILED : No value provided to set PCS virtual lane Skew"
                return result_msg

        elif "PCS400G" in stacVal:
            if str(value):
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:PCS:LANE:SKEW:BLOC %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                                 "%s,%s,%s,%s,%s" % (
                                 value, defaultValue, defaultValue, defaultValue, defaultValue, defaultValue,
                                 defaultValue, defaultValue, defaultValue,
                                 defaultValue, defaultValue, defaultValue, defaultValue, defaultValue, defaultValue,
                                 defaultValue), waittime=10)

            else:
                result_msg = "FAILED : No value provided to set PCS virtual lane Skew"
                return result_msg

        else:
            result_msg = "FAILED : Please check Testset layer configuration for GBE config"
            return result_msg

        return result_msg
    
    def __clearErrorPhys(self, error, lane, CH):
        result_msg = "FAILED : currently clear error on PHYS layer is not supported by ONT"
        return result_msg
    
    def __clearErrorPcs(self, logger_handle,error, lane, CH):

        msg = "************ Clearing Error on PCS Layer *******************"
        plogger.info_log(handle =logger_handle,msg = msg)
        layer = "PCS"
        layer_cmd = "PCS"
        result_msg = "SUCCESS"
        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")

        if "PCSL" in layer_val:
            layer_cmd = "PCS:LANE"
        error_list = self.__getErrorList(error, layer)

        if error not in error_list:
            result_msg = "FAILED :Provided error is not part of PCS layer"
            return result_msg

        else:
            if error in ['ITB']:
                layer_cmd = "PCS:B257"

            if error in ['FEC_CORR', 'FEC_UNCORR', 'FEC_BURST', 'FEC_USER', 'FEC_STST']:
                layer_cmd = "PCS:FEC"

            if error in ['USER_AM_SEQ']:
                layer_cmd = "PCS:AM"

            if error in ['LEF']:
                layer_cmd = "PCS:RS"

            result = self.__clearError(logger_handle,error,lane, layer_cmd)
            if "FAILED" in result:
                return result

        return result_msg

    def __clearErrorOtl(self, logger_handle,error, lane, CH):

        msg = "************ Clearing Error on OTL Layer *******************"
        plogger.info_log(handle =logger_handle,msg = msg)
        layer = "OTL"
        layer_cmd = "OTL"
        result_msg = "SUCCESS"
        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")

        error_list = self.__getErrorList(error, layer)

        if error not in error_list:
            result_msg = "FAILED :Provided error is not part of OTL layer"
            return result_msg

        else:
            result = self.__clearError(logger_handle,error,lane, layer_cmd)
            if "FAILED" in result:
                return result

        return result_msg

    def __clearErrorOtn(self, logger_handle,error, lane, CH):

        msg = "************ Clearing Error on OTN Layer *******************"
        plogger.info_log(handle =logger_handle,msg = msg)
        layer = "OTN"
        layer_cmd = "OTN:OTU"
        result_msg = "SUCCESS"
        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")

        error_list = self.__getErrorList(error, layer)

        if error not in error_list:
            result_msg = "FAILED :Provided error is not part of OTN layer"
            return result_msg

        else:
            result = self.__clearError(logger_handle,error,lane, layer_cmd)
            if "FAILED" in result:
                return result

        return result_msg

    def __clearErrorMac(self, logger_handle,error, lane, CH):

        msg = "************ Clearing Error on MAC Layer *******************"
        plogger.info_log(handle =logger_handle,msg = msg)
        layer = "MAC"
        layer_cmd = "MAC"
        result_msg = "SUCCESS"
        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")

        error_list = self.__getErrorList(error, layer)

        if error not in error_list:
            result_msg = "FAILED :Provided error is not part of MAC layer"
            return result_msg

        else:

            result = self.__clearError(logger_handle,error,lane, layer_cmd)
            if "FAILED" in result:
                return result

        return result_msg

    def __clearError(self, logger_handle,error, lane, cmd):

        msg = "************ Clearing  Error *******************"
        plogger.info_log(handle =logger_handle,msg = msg)
        error = error
        layer_cmd = cmd
        result_msg = "SUCCESS"

        if error == "CLEAR_ALL":
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:%s:ERR:INS OFF" % layer_cmd, waittime=2)
            return result_msg

        if "PCS" in cmd or "OTL" in cmd:
            if lane:
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:%s:ERR:RANG SING"%layer_cmd,waittime=3)
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:%s:ERR:SING %s"%(layer_cmd,lane), waittime=3)
            else:
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:%s:ERR:RANG ALL" % layer_cmd, waittime=3)

        status = self.sendCommand(logger_handle,":SOUR:DATA:TEL:%s:ERR:INS?" % layer_cmd, waittime=2)

        if status == "OFF":
            result_msg = "FAILED :Error is not inserted or already cleared "
            return result_msg
        else:
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:%s:ERR:INS OFF" % layer_cmd, waittime=2)

        return result_msg

    def __getErrorList(self, error, layer):

        error = error
        layer = layer

        phys_error = ['BIT_ERROR']
        pcs_error = ['SYNC_HEADER_INV', 'IAM', 'BIP8', 'ITB', 'FEC_CORR', 'FEC_UNCORR', 'USER_AM_SEQ', 'BLOC_TYPE_INV']
        otl_error = ['FAS', 'MFAS', 'USER_MFAS', 'LLM', 'USER_LLM']
        otn_error = ['RAND', 'FAS', 'MFAS', 'SM_BIP', 'SM_BEI', 'FEC_CORR', 'FEC_UNCORR', 'FEC_MAX', 'FEC_ADV', 'PM_BIP', 'PM_BEI', 'OMFI']
        otn_tcm_error = []
        for i in range(1, 7):
            for err in ["BIP", "BEI"]:
                otn_tcm_error.append(f"TCM{str(i)}_{err}")
        otn_error = otn_error + otn_tcm_error
        fec_error = ['FEC_CORR', 'FEC_UNCORR']
        mac_error = ['RUNT', 'OV', 'FCS', 'SFD', 'JABB', 'FLOS', 'DUPL', 'MIS', 'SWAP']

        check_error_map = {
            "PHYS": phys_error,
            "PCS": pcs_error,
            "OTL": otl_error,
            "OTN": otn_error,
            "FEC": fec_error,
            "MAC": mac_error
        }

        check_error_map[layer].append("CLEAR_ALL")
        return check_error_map[layer]

    def __getAlarmsMap(self, layer):
        layer = layer

        phys_alrm = {"32" : "Frequency Out of Range alarm" }
        otl_alrm = {"1": "LOPL",
                    "2": "LOFOTL",
                    "4": "OOFOTL",
                    "8": "LOR",
                    "16": "OOR",
                    "32": "OOLLM",
                    "64": "OOMFAS",
                    "128": "LOL",
                    "256": "OOL",
                    "512": "LOA"
        }
        otn_alrm = {"1": "LOPL",
                    "2": "LOF",
                    "4": "OOF",
                    "8": "OTU-AIS",
                    "16": "LOM",
                    "32": "OOM",
                    "64": "ODU-AIS",
                    "128": "ODU-OCI",
                    "256": "ODU-LCK",
                    "512": "SM-BDI",
                    "1024": "SM-IAE",
                    "2048": "SM-BIAE",
                    "4096": "SM-TIM",
                    "8192": "PM-BDI",
                    "16384": "PM-TIM",
                    "32768": "FTFL-FSF",
                    "65536": "FTFL-BSF",
                    "131072": "FTFL-FSD",
                    "262144": "FTFL-BSD",
                    "524288": "Payload Type Mismatch",
                    "1048576": "Client Loss",
                    "2097152": "Client Signal Fail",
                    "4194304": "LOMFI",
                    "8388608": "OOMFI",
                    "16777216": "MSI"
        }
        otn_tcm1_alrm = {"1": "TCM1-BDI",
                        "2": "TCM1-BIAE",
                        "4": "TCM1-TIM",
                        "8": "TCM1-IAE",
                        "16": "TCM1-LTC",
                        "32": "TCM2-BDI",
                        "64": "TCM2-BIAE",
                        "128": "TCM2-TIM",
                        "256": "TCM2-IAE",
                        "512": "TCM2-LTC",
                        "1024": "TCM3-BDI",
                        "2048": "TCM3-BIAE",
                        "4096": "TCM3-TIM",
                        "8192": "TCM3-IAE",
                        "16384": "TCM3-LTC",
                        "32768": "TCM4-BDI",
                        "65536": "TCM4-BIAE",
                        "131072": "TCM4-TIM",
                        "262144": "TCM4-IAE",
                        "524288": "TCM4-LTC",
                        "1048576": "TCM5-BDI",
                        "2097152": "TCM5-BIAE",
                        "4194304": "TCM5-TIM",
                        "8388608": "TCM5-IAE",
                        "16777216": "TCM5-LTC",
                        "33554432": "TCM6-BDI",
                        "67108864": "TCM6-BIAE",
                        "134217728": "TCM6-TIM",
                        "268435456": "TCM6-IAE",
                        "536870912": "TCM6-LTC"
        }
        otn_tcm2_alrm = {"1": "TCM1-AIS",
                        "2": "TCM1-OCI",
                        "4": "TCM1-LCK",
                        "32": "TCM2-AIS",
                        "64": "TCM2-OCI",
                        "128": "TCM2-LCK",
                        "1024": "TCM3-AIS",
                        "2048": "TCM3-OCI",
                        "4096": "TCM3-LCK",
                        "32768": "TCM4-AIS",
                        "65535": "TCM4-OCI",
                        "131072": "TCM4-LCK",
                        "1048576": "TCM5-AIS",
                        "2097152": "TCM5-OCI",
                        "4194304": "TCM5-LCK",
                        "33554432": "TCM6-AIS",
                        "67108864": "TCM6-OCI",
                        "134217728": "TCM6-LCK",
        }
        pcs_alrm = {"Lane": {"0": "RESERVED",
                             "1": "LOPL",
                             "2": "LOBL",
                             "4": "LOA",
                             "8": "LOAML",
                             "16": "VL SWAP",
                             "32": "VOMS"},
                    "Reconciliation": {"0": "RESERVED",
                                       "1": "Local fault",
                                       "2": "Remote fault",
                                       "4": "Minimum interpacket gap violation",
                                       "8": "Link down"}
                    }
        mac_alrm = {"1" : "LOPL"}

        check_alarm_object_map = {
            "PHYS": phys_alrm,
            "OTL": otl_alrm,
            "OTN": otn_alrm,
            "OTNTCM1": otn_tcm1_alrm,
            "OTNTCM2": otn_tcm2_alrm,
            "PCS": pcs_alrm,
            "MAC": mac_alrm
        }
        return check_alarm_object_map[layer]  
    
    def stop_measurement(self,logger_handle):

        print("*** Stop the Measurement ***")
        plogger.debug_log(handle = logger_handle ,msg = "************ Stop the Measurement *******************")
        self.sendCommand(logger_handle,":ABOR",waittime=3)

        result_msg = "ONT measurement stopped"
        return result_msg
        
    def start_measurement(self,logger_handle):
        print("*** Start the Measurement ***")
        plogger.debug_log(handle = logger_handle ,msg = "************ Start the Measurement *******************")
        # Starting measurement
        self.sendCommand(logger_handle,':INIT:IMM:ALL;*WAI', waittime=4)

        # Refreshing alarms
        self.sendCommand(logger_handle,":ABOR;*WAI;:INIT:IMM:ALL;*WAI", waittime=2)
        result_msg = "ONT measurement started"
        return result_msg
    
    def check_traffic_status(self,logger_handle,expctAlmErr = False):
        msg = "*** Checking the ovearall traffic status ***"
        print(msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)     
        mapAlmErr = self.sendCommand(logger_handle,":INST:STAT:SUM:CST?",waittime=3)
        if mapAlmErr.strip().split(",")[1] > 0 and expctAlmErr == False:
            plogger.error_log(handle = logger_handle ,msg = "FAILED ,  Atleast one layer has an alarm/error !")
            result_msg = "FAILED"
        elif mapAlmErr.strip().split(",")[1] > 0 and expctAlmErr == True:
            plogger.info_log(handle = logger_handle ,msg = "SUCCESS ,  Atleast one layer has an alarm/error!")
            result_msg = "SUCCESS"
        return result_msg


    def check_traffic_current(self, logger_handle,expctAlmErr=False):

        msg = "********* Checking specific current traffic status***********"
        print("*** Checking the ovearall traffic status ***")
        plogger.debug_log(handle = logger_handle ,msg = msg)   
        layer_map = {
            "PHYS": self.__checkTrafficPhys,
            "OTL": self.__checkTrafficOtl,
            "OTN": self.__checkTrafficOtn,
            "PCSL": self.__checkTrafficPcsl,
            "MAC": self.__checkTrafficGbeMac
        }
        self.clearTraffic = True
        layer_stacks = (self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")).split('\n')[0].split('>')[-1].split("_")

        plogger.debug_log(handle = logger_handle ,msg = "Layer Stacks :'%s'" % layer_stacks)

        self.sendCommand(logger_handle,":ABOR;*WAI;:INIT:IMM:ALL;*WAI;", waittime=5)
        result="SUCCESS"
        result_msg="SUCCESS, Check traffic Current is successful"

        result_dict = {} 
        for layer in layer_stacks:
            if 'OTL' in layer:
                layer = layer[:-1]
            result_dict[layer] = ''
            if layer not in layer_map:
                result = "FAILED"
                result_msg = "FAILED , This Testset config is Not supported"
                return result_msg
            else:
                result = layer_map[layer](logger_handle,expctAlmErr)
                plogger.info_log(handle = logger_handle ,msg = result)

            if "SUCCESS" in result:
                pass
            else:
                plogger.error_log(handle = logger_handle ,msg = "Layer {} has alarms or errors !".format(layer))
                # break
            result_dict[layer] = result
        if "FAILED" in result_dict.values():
            result_msg = "FAILED"
        else:
            result_msg = "SUCCESS"
        return result_msg

    def __checkTrafficPhys(self,logger_handle,expctAlmErr):

        msg = "*** Checking traffic on PHYSICAL LAYER ***"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)
        commands = [":PHYS:LINE:CST:ALAR?"]
        for cmd in commands:
            layer = cmd.split(":")[1]
            layer_obj = "physical"
            result_msg = self.__check_traffic(logger_handle,cmd,layer,layer_obj,expctAlmErr)
        return result_msg

    def __checkTrafficOtl(self,logger_handle,expctAlmErr):
        msg = "*** Checking traffic on OTL LAYER ***"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)
        commands = [":OTL:SUM:CST:ALAR?", ":OTL:SUM:CST:ERR?"]
        for cmd in commands:
            layer = cmd.split(":")[1]
            layer_obj = ""
            result_msg = self.__check_traffic(logger_handle,cmd,layer,layer_obj,expctAlmErr)
        return result_msg

    def __checkTrafficOtn(self,logger_handle,expctAlmErr):
        msg = "*** Checking traffic on OTN LAYER ***"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)
        commands = [":OTN:OTU:CST:ALAR?", ":OTN:OTU:CST:ERR?"]
        for cmd in commands:
            layer = cmd.split(":")[1]
            layer_obj = ""
            result_msg = self.__check_traffic(logger_handle,cmd,layer,layer_obj,expctAlmErr)
        return result_msg

    def __checkTrafficPcsl(self,logger_handle,expctAlmErr):
        msg = "*** Checking traffic on PCSL LAYER ***"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)
        commands = [":PCS:CST:SUM?"]
        for cmd in commands:
            layer = cmd.split(":")[1]
            layer_obj = ""
            result_msg = self.__check_traffic(logger_handle,cmd,layer,layer_obj,expctAlmErr)
        return result_msg

    def __checkTrafficGbeMac(self,logger_handle,expctAlmErr):
        try:
            msg = "*** Checking traffic on MAC layer ***"
            print (msg)
            plogger.debug_log(handle = logger_handle ,msg = msg)
            layer_config = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")
            output = self.sendCommand(logger_handle,":MAC:BAND:UTIL?",waittime=3)
            value = float(output.split(',')[-1].split('\n')[0])
            if value > 0:
                if "PCSL" in layer_config:
                    commands = [":MAC:PAYL:CST:ERR:QOS?", ":MAC:PAYL:CST:ALAR:QOS?", ":MAC:CST:ALAR?", ":MAC:CST:ERR?"]
                else:
                    commands=[":MAC:PAYL:CST:ALAR:BERT?", ":MAC:PAYL:CST:ERR:BERT?", ":MAC:PAYL:CST:ERR:QOS?",
                              ":MAC:PAYL:CST:ALAR:QOS?",":MAC:CST:ALAR?", ":MAC:CST:ERR?"]

                for cmd in commands:
                    layer = cmd.split(":")[1]
                    layer_obj = cmd.split(":")[-1].split("?")[-2]
                    result_msg = self.__check_traffic(logger_handle,cmd,layer,layer_obj,expctAlmErr)
            else:
                result_msg = "FAILED - Bandwidth utilization is zero" 
                return result_msg
            return result_msg
        except:
            result_msg = "FAILED - Exception caught and traffic check terminated abnormally "
            return result_msg

    def __check_traffic(self,logger_handle,command, layer,layer_obj,expctAlmErr):
        try:
            result = self.sendCommand(logger_handle,command,waittime=2)
            if "\n>" in result:
                result = result.replace("\n>","")
            if int(result.strip().split(",")[1]) > 0 and expctAlmErr == False:
                plogger.error_log(handle = logger_handle ,msg = "ERROR  -  {} - {} layer has alarms!".format(layer,layer_obj))
                result_msg = "FAILED"
            elif int(result.strip().split(",")[1]) > 0 and expctAlmErr == True:
                plogger.info_log(handle = logger_handle ,msg = "CLEAR  -  {} - {} layer has alarms /errors (may be expected) !".format(layer,layer_obj))
                result_msg = "SUCCESS"
            elif int(result.strip().split(",")[1]) == 0:
                plogger.info_log(handle = logger_handle ,msg = "CLEAR  -  No alarms on the {} - {} layer!".format(layer,layer_obj))
                result_msg = "SUCCESS"
            else: 
                result_msg = "FAILED"
        except Exception as e:
            excp_msg = "ERROR OCCURED - while fetching the alarms/errors status- " + str(e)
            print (excp_msg)
            plogger.error_log(handle = logger_handle ,msg = excp_msg)
            result_msg = "FAILED"
        return result_msg

    def __insertAlarmPhys(self,logger_handle,alarm,duration,mode,ActAlarmFrame,InactiveAlarmFrame,CH):

        msg = "************ Inserting Alarm on PHYS Layer *******************"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)
        alarm = alarm
        dur = duration
        mode = mode

        layer = "PHYS"
        layer_cmd = "PHYS:LINE"
        result_msg = "SUCCESS"
        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")

        alarm_list = self.__getAlarmList(alarm,layer)

        if alarm in alarm_list:
            if "PCS400G" in layer_val:
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:PHYS:ALL:PHY:ALAR:INS 0,1,ON")
                layer_cmd = "PHYS:MULT:PHY"
        else:
            result_msg = "FAILED : Provided alarm is not part of PHYS layer"
            return result_msg

        if mode == "CONT":
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:INS ON".format(layer_cmd),waittime=2)
            plogger.debug_log(handle = logger_handle ,msg = " LOS insertion STARTED [PHYS Layer] from the Testset")
            if dur != 0:
                time.sleep(dur)
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:INS OFF".format(layer_cmd), waittime=2)
                plogger.debug_log(handle = logger_handle ,msg = " LOS insertion STOPPED [PHYS Layer] from the Testset")
        else:
            result_msg = "FAILED : Only Mode as 'CONT' is supported for PHYS layer"
            return result_msg

        return result_msg

    def __insertAlarmPcs(self,logger_handle, alarm, duration, mode,ActAlarmFrame,InactiveAlarmFrame,CH):

        msg = "************ Inserting Alarm on PCS Layer *******************"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)

        dur = duration
        layer = "PCS"
        layer_cmd = "PCS"
        result_msg = "SUCCESS"
        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")

        alarm_list = self.__getAlarmList(alarm, layer)

        if alarm not in alarm_list :
            result_msg = "FAILED : Provided alarm is not part of PCS layer"
            return result_msg

        if alarm == "LOA":
            result = self.setPcsSkewOnAllLanes(logger_handle,value=2000)
            if dur != 0:
                time.sleep(dur)
                result = self.setPcsSkewOnAllLanes(logger_handle,value=0)
            if "FAILED" in result:
                return result

        elif alarm == "LOLM":

            if "PCSL" in layer_val:
                # 100G case
                if "FEC" in layer_val:
                    alarm = "LOAMPS"
                    layer_cmd = "FEC:LANE"
                else:
                    layer_cmd = "PCS:LANE"
                    alarm = "LOAML"
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:TYPE {}".format(layer_cmd, alarm), waittime=5)
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:INS ON" .format(layer_cmd), waittime=2)
                plogger.debug_log(handle = logger_handle ,msg = "{} insertion STARTED [PCS Layer] from the Testset".format(alarm))
                if dur != 0:
                    time.sleep(dur)
                    self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:INS OFF".format(layer_cmd), waittime=2)
                    plogger.debug_log(handle = logger_handle ,msg = "{} insertion STOPPED [PCS Layer]  from the Testset".format(alarm))
                return result_msg

            if "PCS400G" in layer_val:
                alarm = "LOAMPS"
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:INS ON".format(layer_cmd), waittime=2)
                if dur != 0:
                    time.sleep(dur)
                    self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:INS OFF".format(layer_cmd), waittime=2)
                return result_msg

        elif "PCS400G" in layer_val and alarm == "LOAMPS":
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:INS ON".format(layer_cmd), waittime=2)
            if dur != 0:
                time.sleep(dur)
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:INS OFF".format(layer_cmd), waittime=2)
            return result_msg

        else:
            if alarm in ["LOC_FAULT", "REM_FAULT"]:
                layer_cmd = "PCS:RS"

            if "PCSL" in layer_val and alarm in ["LOBL","LOAML","HIBER"]:
                if alarm in ["LOBL", "LOAML"]:
                    layer_cmd = "PCS:LANE"
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:TYPE {}".format(layer_cmd, alarm), waittime=5)
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:INS ON".format(layer_cmd), waittime=2)
                if dur != 0:
                    time.sleep(dur)
                    self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:INS OFF".format(layer_cmd), waittime=2)
                return result_msg

            if "PCS400G" in layer_val:
                if alarm in ["LOC_DSER", "REM_DSER", "HSER"]:
                    layer_cmd = "PCS:FEC"

            result = self.__insertAlarm(logger_handle,alarm,duration,mode,ActAlarmFrame,InactiveAlarmFrame,layer_cmd)
            if "FAILED" in result:
                return result

        return result_msg

    def __insertAlarmOtl(self,logger_handle,alarm,duration,mode,ActAlarmFrame,InactiveAlarmFrame,CH):

        msg = "************ Inserting Alarm on OTL Layer *******************"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)
        alarm = alarm
        dur = duration
        mode = mode

        layer = "OTL"
        layer_cmd = "OTL"
        result_msg = "SUCCESS"
        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")

        alarm_list = self.__getAlarmList(alarm,layer)

        if alarm not in alarm_list:
            result_msg = "FAILED : Provided alarm is not part of OTL layer"
            return result_msg

        if mode == "CONT":
            result_msg = self.__insertAlarm(logger_handle,alarm,duration,mode,ActAlarmFrame,InactiveAlarmFrame,layer_cmd)
        else:
            result_msg = "FAILED : Only Mode as 'CONT' is supported for OTL layer"

        return result_msg

    def __insertAlarmOtn(self,logger_handle,alarm,duration,mode,ActAlarmFrame,InactiveAlarmFrame,CH):

        msg = "************ Inserting Alarm on OTN Layer *******************"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)
        alarm = alarm
        dur = duration
        mode = mode

        layer = "OTN"
        layer_cmd = "OTN:OTU"
        result_msg = "SUCCESS"
        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")

        alarm_list = self.__getAlarmList(alarm,layer)

        if alarm not in alarm_list:
            result_msg = "FAILED : Provided alarm is not part of OTN layer"
            return result_msg

        if mode == "CONT":
            result_msg = self.__insertAlarm(logger_handle,alarm,duration,mode,ActAlarmFrame,InactiveAlarmFrame,layer_cmd)
        else:
            result_msg = "FAILED : Only Mode as 'CONT' is supported for OTN layer"

        return result_msg

    def __insertAlarm(self,logger_handle,alarm, duration, mode,ActAlarmFrame,InactiveAlarmFrame,cmd):

        msg = "************ Selecting Mode and inserting Alarm *******************"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)
        dur = duration
        alarm = alarm
        mode = mode
        layer_cmd = cmd

        result_msg = "SUCCESS"

        self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:TYPE {}".format(layer_cmd, alarm), waittime=5)
        if mode == "CONT":
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:MODE {}".format(layer_cmd, mode), waittime=5)

            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:INS ON".format(layer_cmd), waittime=2)
            if dur != 0:
                time.sleep(dur)
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:INS OFF".format(layer_cmd), waittime=2)

        elif mode == "BURST_ONCE":
            if ActAlarmFrame == 0:
                result_msg = "FAILED :  Invalid values for 'ActAlarmFrame' parameter for BURST_ONCE mode"
                return result_msg

            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:MODE {}".format(layer_cmd, mode), waittime=5)
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:BURS:ACTI {}".format(layer_cmd, ActAlarmFrame), waittime=2)
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:INS ON".format(layer_cmd), waittime=2)
            if dur != 0:
                time.sleep(dur)
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:INS OFF".format(layer_cmd), waittime=2)

        elif mode == "BURST_CONT":
            if ActAlarmFrame == 0 or InactiveAlarmFrame == 0:
                result_msg = "FAILED : Invalid values for 'ActAlarmFrame and InactiveAlarmFrame' parameters for BURST_CONT mode"
                return result_msg

            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:MODE {}".format(layer_cmd, mode), waittime=5)
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:BURS:ACTI {}".format(layer_cmd, ActAlarmFrame), waittime=2)
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:BURS:INAC {}".format(layer_cmd, InactiveAlarmFrame), waittime=2)

            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:INS ON".format(layer_cmd), waittime=2)
            if dur != 0:
                time.sleep(dur)
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ALAR:INS OFF".format(layer_cmd), waittime=2)

        return result_msg

    def __insertAlarmMac(self,logger_handle, alarm, duration, mode, ActAlarmFrame, InactiveAlarmFrame,CH):

        msg = "************ Inserting Alarm on MAC Layer *******************"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)
        dur = duration
        layer = "MAC"
        layer_cmd = "MAC"
        result_msg = "SUCCESS"
        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")

        alarm_list = self.__getAlarmList(alarm, layer)

        if alarm not in alarm_list:
            result_msg = "FAILED :Provided alarm is not part of MAC layer"
            return result_msg

        else:
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:TRAF:STAT OFF".format(layer_cmd), waittime=2)
            if dur != 0:
                time.sleep(dur)
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:TRAF:STAT ON".format(layer_cmd), waittime=2)

        return result_msg


    def __insertErrorPhys(self, logger_handle,error, rate, duration, mode, ActErrorFrame, InactErrorFrame,lane, CH):
        msg = "************ Inserting Error on PHY Layer *******************"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)

        dur = duration
        layer = "PHYS"
        layer_cmd = "PHYS:PAYL"
        result_msg = "SUCCESS"
        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")

        error_list = self.__getErrorList(error, layer)

        if error not in error_list:
            result_msg = "FAILED :Provided error is not part of PHY layer"
            return result_msg

        else:
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:INS ON".format(layer_cmd), waittime=2)

        return result_msg

    def __insertErrorPcs(self, logger_handle,error, rate, duration, mode, ActErrorFrame, InactErrorFrame, lane, CH):

        msg = "************ Inserting Error on PCS Layer *******************"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)

        dur = duration
        layer = "PCS"
        layer_cmd = "PCS"
        result_msg = "SUCCESS"
        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")
        if "PCSL" in layer_val:
            layer_cmd = "PCS:LANE"
        error_list = self.__getErrorList(error, layer)

        if error not in error_list:
            result_msg = "FAILED :Provided error is not part of PCS layer"
            return result_msg

        else:
            if error in ['FEC_CORR', 'FEC_UNCORR', 'FEC_BURST', 'FEC_USER', 'FEC_STST']:
                layer_cmd = "PCS:FEC"

            if error in ['USER_AM_SEQ']:
                layer_cmd = "PCS:AM"

            if error in ['LEF']:
                layer_cmd = "PCS:RS"

            result = self.__insertError(logger_handle,error,rate, duration, mode, ActErrorFrame, InactErrorFrame, lane, layer_cmd)
            if "FAILED" in result:
                return result

        return result_msg

    def __insertErrorOtl(self, logger_handle,error, rate, duration, mode, ActErrorFrame, InactErrorFrame, lane, CH):

        msg = "************ Inserting Error on OTL Layer *******************"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)

        dur = duration
        layer = "OTL"
        layer_cmd = "OTL"
        result_msg = "SUCCESS"
        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")
        error_list = self.__getErrorList(error, layer)

        if error not in error_list:
            result_msg = "FAILED :Provided error is not part of OTL layer"
            return result_msg

        else:
            result = self.__insertError(logger_handle,error,rate, duration, mode, ActErrorFrame, InactErrorFrame, lane, layer_cmd)
            if "FAILED" in result:
                return result

        return result_msg

    def __insertErrorOtn(self, logger_handle,error, rate, duration, mode, ActErrorFrame, InactErrorFrame, lane, CH):

        msg = "************ Inserting Error on OTN Layer *******************"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)

        dur = duration
        layer = "OTN"
        layer_cmd = "OTN:OTU"
        result_msg = "SUCCESS"
        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")
        error_list = self.__getErrorList(error, layer)

        if error not in error_list:
            result_msg = "FAILED :Provided error is not part of OTN layer"
            return result_msg

        else:
            result = self.__insertError(logger_handle,error,rate, duration, mode, ActErrorFrame, InactErrorFrame, lane, layer_cmd)
            if "FAILED" in result:
                return result

        return result_msg

    def __insertError(self, logger_handle, error, rate, duration, mode, ActErrorFrame, InactErrorFrame, lane, cmd):

        msg = "************ Selecting Mode and inserting Error *******************"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)

        error = error
        rate = rate
        dur = duration
        mode = mode
        layer_cmd = cmd

        result_msg = "SUCCESS"

        self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:TYPE {}".format(layer_cmd, error), waittime=5)
        if mode == "CONT":
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:MODE {}".format(layer_cmd, mode), waittime=5)
            if lane:
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:RANG SING".format(lane),waittime=3)
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:SING {}".format(lane),waittime=3)
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:INS ON".format(layer_cmd), waittime=2)
            if dur != 0:
                time.sleep(dur)
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:INS OFF".format(layer_cmd), waittime=2)


        elif mode == "RATE":
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:MODE {}".format(layer_cmd, mode), waittime=5)
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:RATE {}".format(layer_cmd, rate), waittime=5)
            if lane:
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:RANG SING".format(lane),waittime=3)
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:SING {}".format(lane),waittime=3)
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:INS ON".format(layer_cmd), waittime=2)
            if dur != 0:
                time.sleep(dur)
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:INS OFF".format(layer_cmd), waittime=2)

        elif mode == "ONCE":
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:MODE {}".format(layer_cmd, mode), waittime=5)
            if lane:
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:RANG SING".format(lane),waittime=3)
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:SING {}".format(lane),waittime=3)
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:INS ON".format(layer_cmd), waittime=2)

        elif mode == "BURST_ONCE":
            if ActErrorFrame == 0:
                result_msg = "FAILED : Invalid value for 'ActErrorFrame' parameter for BURST_ONCE mode"
                return result_msg

            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:MODE {}".format(layer_cmd, mode), waittime=5)
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:BURS:ACTI {}".format(layer_cmd, ActErrorFrame), waittime=2)
            if lane:
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:RANG SING".format(lane),waittime=3)
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:SING {}".format(lane),waittime=3)
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:INS ON".format(layer_cmd), waittime=2)

        elif mode == "BURST_CONT":
            if ActErrorFrame == 0 or InactErrorFrame == 0:
                result_msg = "FAILED : Invalid values for 'ActErrorFrame and InactErrorFrame' parameters for BURST_CONT mode"
                return result_msg

            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:MODE {}".format(layer_cmd, mode), waittime=5)
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:BURS:ACTI {}".format(layer_cmd, ActErrorFrame), waittime=2)
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:BURS:INAC {}".format(layer_cmd, InactErrorFrame), waittime=2)
            if lane:
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:RANG SING".format(lane),waittime=3)
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:SING {}".format(lane),waittime=3)

            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:INS ON".format(layer_cmd), waittime=2)
            if dur != 0:
                time.sleep(dur)
                self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:ERR:INS OFF" .format(layer_cmd), waittime=2)

        return result_msg

    def __insertErrorMac(self, logger_handle,error, rate, duration, mode, ActErrorFrame, InactErrorFrame,lane, CH):

        msg = "************ Inserting Error on MAC Layer *******************"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)

        dur = duration
        layer = "MAC"
        layer_cmd = "MAC"
        result_msg = "SUCCESS"
        layer_val = self.sendCommand(logger_handle,":INST:CONF:EDIT:LAY:STAC?")

        error_list = self.__getErrorList(error, layer)

        if error not in error_list:
            result_msg = "FAILED :Provided error is not part of MAC layer"
            return result_msg

        if error in ['FLOS', 'DUPL', 'MIS', 'SWAP']:
            layer_cmd = "MAC:PAYL"
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:TFR:ERR:TYPE {}".format(layer_cmd, error), waittime=5)
            self.sendCommand(logger_handle,":SOUR:DATA:TEL:{}:TFR:ERR:INS ON".format(layer_cmd), waittime=2)

        else:

            result = self.__insertError(logger_handle,error, rate, duration, mode, ActErrorFrame, InactErrorFrame,lane, layer_cmd)
            if "FAILED" in result:
                return result

        return result_msg

    def __getAlarmPhys(self,logger_handle) -> list:
        msg = "************ Retreiving Alarm on PHYS Layer *******************"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)
        layer = "PHYS"
        layer_cmd = "PHYS:LINE"
        result_msg = {"status": "SUCCESS",
                      "alarms": []}
        try:
            alarm_list = self.__getAlarmsMap(layer)
            alarm_data = self.sendCommand(logger_handle,":{}:CST:ALAR?".format(layer_cmd), waittime=2)
            alarm_data = alarm_data .replace('\n>','')
            phys_alarms = []
            for key in alarm_list.keys():
                if (int(key) & int(alarm_data.split(',')[1])):
                    phys_alarms.append(alarm_list[key])
            result_msg['alarms'] = phys_alarms
        except Exception as e:
            result_msg["status"] = "FAILED"
            plogger.error_log(handle = logger_handle,msg = e )
        return result_msg

    def __getAlarmOtl(self,logger_handle) -> list:
        msg = "************ Retreiving Alarm on OTL Layer *******************"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)
        layer = "OTL"
        layer_cmd = "OTL:SUM"
        result_msg = {"status": "SUCCESS",
                      "alarms": []}
        try:
            alarm_list = self.__getAlarmsMap(layer)
            alarm_data = self.sendCommand(logger_handle,":{}:CST:ALAR?".format(layer_cmd), waittime=2)
            alarm_data = alarm_data .replace('\n>','')
            otl_alarms = []
            for key in alarm_list.keys():
                if (int(key) & int(alarm_data.split(',')[1])):
                    otl_alarms.append(alarm_list[key])
            result_msg['alarms'] = otl_alarms
        except Exception as e:
            result_msg["status"] = "FAILED"
            plogger.error_log(handle = logger_handle,msg = e )
        return result_msg

    def __getAlarmOtn(self,logger_handle) -> list:
        msg = "************ Retreiving Alarm on OTN Layer *******************"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)
        layer = "OTN"
        layer_cmd = "OTN:OTU"
        result_msg = {"status": "SUCCESS",
                      "alarms": []}
        sublayer_map = [("OTN", ":OTN:OTU:CST:ALAR?"),
                        ("OTNTCM1", ":OTN:OTU:CST:ALAR:TCM?"),
                        ("OTNTCM2", ":OTN:OTU:CST:ALAR:TCM2?")]
        try:
            otn_alarms = []
            for sublayer, sublayer_cmd in sublayer_map:
                alarm_list = self.__getAlarmsMap(layer)
                alarm_data = self.sendCommand(logger_handle, sublayer_cmd, waittime=2)
                alarm_data = alarm_data .replace('\n>','')
                for key in alarm_list.keys():
                    if (int(key) & int(alarm_data.split(',')[1])):
                        otn_alarms.append(alarm_list[key])
            result_msg['alarms'] = otn_alarms
        except Exception as e:
            result_msg["status"] = "FAILED"
            plogger.error_log(handle = logger_handle,msg = e )
        return result_msg

    def __getAlarmPcs(self,logger_handle) -> list:
        msg = "************ Retreiving Alarm on PCS Layer *******************"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)
        layer = "PCS"
        layer_cmd_lane = "PCS:LANE:SUM"
        layer_cmd_recons = "PCS:RS"
        result_msg = {"status": "SUCCESS",
                      "alarms": {}}
        alarm_map_rs = {"Local fault": "LOCF",
                       "Remote fault": "REMF",
                       "Link down": "LNKDWN"}
        try:
            alarm_list = self.__getAlarmsMap(layer)
            alarm_data_lane = self.sendCommand(logger_handle,":{}:CST:ALAR?".format(layer_cmd_lane), waittime=2)
            alarm_data_lane = alarm_data_lane .replace('\n>','')
            alarm_data_recons = self.sendCommand(logger_handle,":{}:CST:ALAR?".format(layer_cmd_recons), waittime=2)
            alarm_data_recons = alarm_data_recons .replace('\n>','')
            pcs_alarms_lane = []
            pcs_alarms_recons = []
            for key in alarm_list["Lane"].keys():
                if (int(key) & int(alarm_data_lane.split(',')[1])):
                    pcs_alarms_lane.append(alarm_list["Lane"][key])
            for key in alarm_list["Reconciliation"].keys():
                if (int(key) & int(alarm_data_recons.split(',')[1])):
                    pcs_alarms_recons.append(alarm_list["Reconciliation"][key])
            if len(pcs_alarms_lane) > 0 :   
                for alarm in pcs_alarms_lane:
                    alm_sec = self.sendCommand(logger_handle,":{}:ASEC:{}?".format(layer_cmd_lane,alarm), waittime=2)
                    alm_sec = alm_sec .replace('\n>','')
                    result_msg['alarms'][alarm] = int(alm_sec.split(',')[1])
            if len(pcs_alarms_recons) > 0 :
                for alarm in pcs_alarms_recons:
                    alm_sec = self.sendCommand(logger_handle,":{}:ASEC:{}?".format(layer_cmd_recons,alarm_map_rs[alarm]), waittime=2)
                    alm_sec = alm_sec .replace('\n>','')
                    result_msg['alarms'][alarm] = int(alm_sec.split(',')[1])
        except Exception as e:
            result_msg["status"] = "FAILED"
            plogger.error_log(handle = logger_handle,msg = e )
        # result_msg['alarms'] = pcs_alarms
        return result_msg

    def __getAlarmMac(self,logger_handle) -> list:
        msg = "************ Retreiving Alarm on MAC Layer *******************"
        print (msg)
        plogger.debug_log(handle = logger_handle ,msg = msg)
        layer = "MAC"
        layer_cmd = "MAC"
        result_msg = {"status": "SUCCESS",
                      "alarms": []}
        try:
            alarm_list = self.__getAlarmsMap(layer)
            alarm_data = self.sendCommand(logger_handle,":{}:CST:ALAR?".format(layer_cmd), waittime=2)
            alarm_data = alarm_data .replace('\n>','')
            mac_alarms = []
            for key in alarm_list.keys():
                if (int(key) & int(alarm_data.split(',')[1])):
                    mac_alarms.append(alarm_list[key])
            result_msg['alarms'] = mac_alarms
        except Exception as e:
            result_msg["status"] = "FAILED"
            plogger.error_log(handle = logger_handle,msg = e )
        return result_msg