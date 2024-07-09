import os
import yaml
import queue
import concurrent.futures
from datetime import datetime
import pickle


def persist(set_get,varNamesList = None):

   # runnable header, tester
   if False:
      import pixi
      prods = [ "G31", "G42" ]
      ifs = ["ANY", "CLI", "REST"]
      myVars = [ prods , ifs ]
      pixi.persist("set",myVars)
      # ...restart shell...
      prods , ifs = pixi.persist("get")
      print(prods)
      print(ifs)
   # 
   pickle_file = os.path.join(home(),"pixie_framework","pixi_persist.pkl")
   if (set_get == "set"):
      handle = open(pickle_file, 'wb')
      #rslt = pickle.dump(varName, handle, protocol=pickle.HIGHEST_PROTOCOL)
      rslt = pickle.dump(varNamesList, handle, protocol=pickle.HIGHEST_PROTOCOL )
      handle.close
      return rslt
   elif (set_get == "get"):
      handle = open(pickle_file, 'rb')
      varName = pickle.load(handle)
      handle.close
      return(varName)
   else:
      print("Invalid value set_get to pixi.persist")
      return(False)


def home():
    pixi_home = os.getenv('PIXI_HOME')
    return(pixi_home)


def local_input():
    pixi_local_input = os.getenv('PIXI_LOCAL_INPUT')
    return(pixi_local_input)
    
def suite(getSet,name=""):
   global suiteName
   if getSet == "get":
      return(suiteName)
   else:
      suiteName = name
    
def flat_mode():
    os.environ['PIXI_FLAT_MODE'] = "yes"
    #os.environ['PIXI_FLAT_MODE'] = "no"
    pixi_flat_mode = os.getenv('PIXI_FLAT_MODE')
    # yes|no ( changing default)
    #print("PIXI_FLAT_MODE: "+os.environ['PIXI_FLAT_MODE'])
    return(pixi_flat_mode)
    
def todayLogDir(getSet):
#    import ipdb; ipdb.set_trace()
   global _mld_date
   if getSet == "get":
      return _mld_date
   elif getSet == "set":
      day_dir = datetime.today().strftime('%m-%d-%Y')
      main_dir = os.path.join(home(),"pixie_framework","pixie_logs",day_dir)
      if not os.path.exists(main_dir):
         os.makedirs(main_dir)
      _mld_date = main_dir
      return(main_dir)
   else:
      print("Error in pixi.mail_log_dir_date getSet: "+getSet)
      return "Error in pixi.mail_log_dir_date getSet: "+getSet
    

def ui():
#
# is really "gui"
#  returns:
#   tkinter, none, or jupyter
# 
#
    pixi_ui = "tkinter"
    try:
        pixi_ui = os.getenv('PIXI_UI')
    except:
        noop = 1
    return(pixi_ui)


def get_setupEnvironment(sut = None, option = None, local = False):
    # Use Input.yml set via PIXI_LOCAL_INPUT if set, otherwise use default pixi-provided copy
    pixi_home = home()
    env_path = local_input()
    if local:
        if not app_path:
            print("Error: Unable to load local Input.yml. app_path not set")
            return False
        input_path = os.path.join(pixi_home, app_path, "Input.yml")
    elif pixi_home and env_path:
        input_path = os.path.join(pixi_home, env_path)
    else:
        input_path = 'Input.yml'
    with open(input_path, 'r') as file:
        config_env = yaml.safe_load(file)
    return (config_env.get(sut, {}).get(option))

def generate_input_file(name, data):
    local_path = os.path.join(home(), app_path)
    input_data = {}
    if 'Input.yml' in os.listdir(local_path):
        with open(os.path.join(local_path, 'Input.yml')) as fh:
            input_data = yaml.safe_load(fh)
    with open(os.path.join(local_path, 'Input.yml'), 'w') as fh:
        input_data[name] = data
        yaml.dump(input_data, fh)
    print(f"Generated {name} login data in Input.yml located at {local_path}")

def suite(getSet,name="no-suite"):
   global _suite
   if getSet == "get":
      return(_suite)
   elif getSet == "set":
      _suite = name
      return(_suite)
   else:
      myErr = "pixi.suite invalid getSet:"+getSet
      print(myErr)
      return(myErr)

# suite or app path also set in rex.loadUserSuite
app_path = ""
todayLogDir("set")

class PIXIQueue():
    """
        Singleton Queue class. 
        Ensures that anybody that creates a PIXIQueue object receives the same instance 
        with the same Python queue.
    """
    def __new__(cls):
        # Check if base instance doesn't exist, create if not, or return singleton if it does
        if not hasattr(cls, 'instance'):
            cls.instance = super(PIXIQueue, cls).__new__(cls)
            # Create the python Queue only during initial creation
            cls.instance.queue = queue.Queue(maxsize=400)
        return cls.instance

    def __init__(self):
        pass

    def put(self, obj):
        self.queue.put(obj)

    def get(self):
        return self.queue.get()

    def empty(self):
        return self.queue.empty()

_MAX_WORKERS = 4

class PIXIPool():

    pool = None
    used_workers = None
    max_workers = None
    cancel = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PIXIPool, cls).__new__(cls)
            cls.instance.pool = concurrent.futures.ThreadPoolExecutor(max_workers=_MAX_WORKERS)
            cls.instance.used_workers = 0
            cls.instance.max_workers = _MAX_WORKERS
            cls.instance.futures = {}
            cls.instance.cancel = False
        return cls.instance

    def __init__(self):
        pass

    def submit(self, function, *args, **kwargs):
        if self.used_workers >= self.max_workers:
            raise RuntimeError(f"Error: PIXIPool max_workers reached: {self.max_workers}. Unable to allocate more.")
        self.futures[self.used_workers] = self.pool.submit(function, *args, **kwargs)
        self.used_workers += 1

    def shutdown(self, cancel=True):
        for k, v in self.futures.items():
            v.cancel()
        self.used_workers = 0
        self.cancel = True


## rex variables
# test
_numericalTestStatus = 0
_testStatus = "noStepsRunYet"
_stepsRun = 0

# row
_numericalRowStatus = 0
_rowStatus = "noStepsRunYet"
_rowStepsRun = 0

# state
_REX_STATE = "idle"


app_path = ""
runner_thread = None
thread_pool = None
_suite = "no-suite"