import json

class HostMemoryModel:
    def GetHostMemory(self,RespData):
        
            RespDataLines = RespData.split('\n')
            MemLine = RespDataLines[0].split(',')
            SwapLine = RespDataLines[1].split(',')
            RespDataDict = {
                "code": 200,
                "Memory": {
                    "Total": f"{MemLine[1]}",
                    "Used": f"{MemLine[2]}",
                    "Free": f"{MemLine[6]}"
                },
                "Swap": {
                    "Total": f"{SwapLine[1]}",
                    "Used": f"{SwapLine[2]}",
                    "Free": f"{SwapLine[3]}"
                }
            }
            cmdResponse=json.dumps(RespDataDict)
            
            return cmdResponse