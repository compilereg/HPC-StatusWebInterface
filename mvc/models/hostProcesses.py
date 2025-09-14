import json

class hostProcesses:
    def GetHostProcessCount(self,RespData):
        
            
            LoadLine = RespData.split(',')
            RespDataDict = {
                "code": 200,
                "Process": {
                    "Count": f"{LoadLine[0]}",
                }
            }
            cmdResponse=json.dumps(RespDataDict)
            
            return cmdResponse