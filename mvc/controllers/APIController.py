from mvc.operations import hostOperations as ho
from mvc.models import responseModel as rm
import json


class APIController:
    
    @classmethod
    def getHostState(self,hostname):
        resp = rm.ResponseModel()
    
        HostName = f"{hostname}"
        HostState = ho.HostOperations.getHostState(HostName)
        if HostState == True:
            ResCode = 200
            HostState="Live"
        else:
            ResCode = 408
            HostState="Dead"
        
        return  resp.buildResponse(HostState,ResCode),ResCode
    
    
    @classmethod
    def getHostMemory(self,hostname):
        cmdResponse=ho.HostOperations.executeRemoteCommand(hostname,"free -h")        
        
        ResCode=json.loads(cmdResponse)['code']
        print(json.loads(cmdResponse)['data'])
        return  cmdResponse,ResCode


    @classmethod
    def getHostLoadAverage(self,hostname):
        cmdResponse=ho.HostOperations.executeRemoteCommand(hostname,"uptime")        
        
        ResCode=json.loads(cmdResponse)['code']
        print(json.loads(cmdResponse)['data'])
        return  cmdResponse,ResCode
    
    @classmethod
    def getHostProcesCount(self,hostname):
        cmdResponse=ho.HostOperations.executeRemoteCommand(hostname,"ps -ef|wc -l")        
        
        ResCode=json.loads(cmdResponse)['code']
        print(json.loads(cmdResponse)['data'])
        return  cmdResponse,ResCode
    
    
    @classmethod
    def getClusterParition(self,hostname):
        cmdResponse=ho.HostOperations.executeRemoteCommand(hostname,"sinfo -s")        
        
        ResCode=json.loads(cmdResponse)['code']
        print(json.loads(cmdResponse)['data'])
        return  cmdResponse,ResCode