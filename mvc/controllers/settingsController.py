from configparser import ConfigParser
from mvc.models import settingsModel as sm
import json
import threading
        
            
##########################Class reads in the settings from the INI file
### The class must be a singleton so that settings must be unique for all objects
### The singleton implemented from 
class Settings:
    _instance = None
    _lock = threading.Lock() # For thread-safety
    iniData = sm.settingsModel()
    conf = ""

    ##Overload the __init__ with __new__, we can add any variables to the new after cls, 
    def __new__(cls):
        if not cls._instance:
            with cls._lock: # Ensure only one thread creates the instance
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance.Data = 0 # Initialize instance-specific data
                    cls.iniData.emptySettings()
        return cls._instance


    def readINI(self):
        self.conf = ConfigParser()
        self.conf.read('settings.ini')  
        for option_name, value in self.conf.items("server"):
            self.iniData.setVServerValue(option_name, value)
            
    def getServerINI(self):
        resp = json.dumps(self.iniData.getServer())
        return resp       
    
    def getServerINIJString(self):
        resp = self.iniData.getServer()
        return resp