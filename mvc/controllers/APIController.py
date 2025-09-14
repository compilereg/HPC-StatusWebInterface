from mvc.operations import hostOperations as ho
from mvc.models import responseModel as rm
from mvc.models import hostMemoryModel as hm
from mvc.models import hostLoadAvgModel as hla
import json



class APIController:
    
    @classmethod
    def getHostState(self,hostname):
        resp = rm.ResponseModel()

        HostState = ho.HostOperations.getHostState(hostname)
        if HostState == "Live":
            ResCode = 200
        else:
            ResCode = 408
        
        return  resp.buildResponse(HostState,ResCode),ResCode
    
    
    @classmethod
    def getHostMemory(self,hostname):
        cmdResponse=ho.HostOperations.executeRemoteCommand(hostname,"free -h|tr -s ' '| sed -e 's/ /,/g' -e '1d'")        
        
        ResCode=json.loads(cmdResponse)['code']
        if ResCode == 200:
            HostMemory=hm.HostMemoryModel()
            cmdResponse = HostMemory.GetHostMemory(json.loads(cmdResponse)['data'])
            
            
        return  cmdResponse,ResCode


    @classmethod
    def getHostLoadAverage(self,hostname):
        cmdResponse=ho.HostOperations.executeRemoteCommand(hostname,"cat /proc/loadavg | awk ' { print $1\",\"$2\",\"$3\",\"$4 } '")        
        
        ResCode=json.loads(cmdResponse)['code']
        if ResCode == 200:
            HostLoadAvg=hla.hostLoadAvgModel()
            cmdResponse = HostLoadAvg.GetHostLoadAvg(json.loads(cmdResponse)['data'])
        
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