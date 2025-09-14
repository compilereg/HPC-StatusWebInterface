import json

class hostLoadAvgModel:
    def GetHostLoadAvg(self,RespData):
        
            
            LoadLine = RespData.split(',')
            RespDataDict = {
                "code": 200,
                "AvgLoad": {
                    "1Min": f"{LoadLine[0]}",
                    "5Min": f"{LoadLine[1]}",
                    "15Min": f"{LoadLine[2]}"
                }
            }
            cmdResponse=json.dumps(RespDataDict)
            
            return cmdResponse