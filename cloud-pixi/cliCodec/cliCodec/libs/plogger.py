from loguru import logger
import os
import re
from datetime import datetime
import sys
from cliCodec.libs import pixi
import logging

# logger.remove()
def debug_log(handle = None,msg = None):
    logger_a = logger.bind(handle=handle)
    logger_a.debug(msg)

def error_log(handle = None,msg = None):
    logger_a = logger.bind(handle=handle)
    logger_a.exception(msg)

def info_log(handle = None,msg = None):
    logger_a = logger.bind(handle=handle)
    logger_a.info(msg)

def cleanTestTitle(_TEST_title_2):
    _TEST_title_2=re.sub('[<>*:"/\?|]', '_', _TEST_title_2)
    _TEST_title_2=re.sub(r"\s+", '_', _TEST_title_2)
    #print(_TEST_title_2)
    return(_TEST_title_2)
    
def main_log_dir():
    # was pixie_logs now pixi_logs
    mld = os.path.join(pixi.home(),"pixie_framework","pixi_logs")
    return mld
    
def main_log_dir_date():
    # 
    # see also pixi.todayLogDir
    # creates today's log dir and suite dir as needed
    #
    main_dir = main_log_dir()
    day_dir = datetime.today().strftime('%m-%d-%Y')
    
    fd_dir = os.path.join(main_dir,day_dir)
    if not os.path.exists(fd_dir):
       os.makedirs(fd_dir)
    return(fd_dir)
    
def suite_log_dir():
    # leaving same as main log dir
    fd_dir = pixi.todayLogDir("get")
    #suiteCleanDate = cleanTestTitle(suite_or_app)
    #suiteCleanDate = ""
    #suite_dir = os.path.join(fd_dir,suiteCleanDate)
    suite_dir = fd_dir
    if not os.path.exists(suite_dir):
       os.makedirs(suite_dir)
    return(suite_dir)

def sheet_rows_dir(_suitename):

    dir = pixi.todayLogDir("get")
    if not os.path.exists(dir):
       os.makedirs(dir)
       
    _suitename = cleanTestTitle(_suitename)
    dir2 = os.path.join(dir,_suitename)
    if not os.path.exists(dir2):
       os.makedirs(dir2)
       
    rowsDir = os.path.join(dir2,"rowsLogs")
    if not os.path.exists(rowsDir):
       os.makedirs(rowsDir)
    return(rowsDir)

    
def sheet_row_log_get(_suitename,_excelsheet,currentsheetrow,_TEST_title_2):
    if "no" in currentsheetrow:
       return ""
    sheet_and_ui_rows = currentsheetrow
    sheet_row = sheet_and_ui_rows.split("_")[0]
    try:
       ui_row = sheet_and_ui_rows.split("_")[1]
       uiRow = "uiRow-"+ui_row
    except:
       uiRow = ""
    new_sheet_and_ui_rows = "sheetRow-"+sheet_row+"_"+uiRow
    _suitename = cleanTestTitle(_suitename)
    sr_dir = sheet_rows_dir(_suitename)
    date = datetime.now().strftime('%Y-%m-%d_%H-%M')
    
    clean_title = cleanTestTitle(_TEST_title_2)
    row_log_file =os.path.join(sr_dir,_suitename+"_"+_excelsheet+"_"+new_sheet_and_ui_rows+"_"+clean_title+".txt")
    return(row_log_file)


def sheet_row_log(_suitename,_excelsheet,currentsheetrow,str,_TEST_title_2):
    # log a test sheet row
    #
    # new
    # change sheetrow to that + gui_row ( if needed - for multi sheet and multi element )
    #  - normally just "N"
    #  - if needed it is "N-M"
    # gui row is 0 based
    #
    _suitename = cleanTestTitle(_suitename)

    row_log_file = sheet_row_log_get(_suitename,_excelsheet,currentsheetrow,_TEST_title_2)
    if row_log_file != "":
       with open(row_log_file,"a+") as f:
          f.write(str+"\n")
    else:
       #info_log(handle = "pixi",msg = str)
       # already logged
       noop = 1
    
def pixie_logger(logtype= None, logger_name = None):
    # if a suite
    #  logtype = pixi
    #  logger_name = suite-name
    # return the log name
    #print("in pixie_logger")
    # current_directory = os.getcwd() + "\\pixie_logs"
    #current_directory = "pixie_logs"
    #current_directory = main_log_dir()
    #dir = datetime.today().strftime('%m-%d-%Y')
    dir = pixi.todayLogDir("get")
    #log_directory = os.path.join(current_directory,dir)
    if not os.path.exists(dir):
       os.makedirs(dir)
    current_suite = pixi.suite("get")
    print("current_suite: "+current_suite)
    #log_directory = suite_log_dir()
    date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')
    #new_var = log_directory+"\\" +logtype +"_"+logger_name+"_"+date+".log"
    new_var = logtype +"_"+logger_name+"_"+date+".log"
    #logger.remove(handler_id=None)
    new_var = os.path.join(dir,logger_name+"-"+ logtype+"-"+date+".log")
    #new_var = os.path.join(logger_name+"-"+ logtype+"-"+date+".log")
    #new_var = logger_name+"-"+ logtype+"-"+date+".log"
    logger.add(new_var, rotation="1 MB",filter=lambda record: record["extra"]["handle"] == logger_name,backtrace=True, diagnose=True)
    info_log(handle = "pixi",msg = "Log: "+new_var)
    print("Log: "+new_var)
    #logger.add(sys.stdout)
    logger_data = logging.getLogger(__name__)
    logger_data.setLevel(logging.DEBUG)
    return(new_var)
    

