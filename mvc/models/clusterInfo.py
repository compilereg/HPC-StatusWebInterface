import json

class ClusterInfo:
    
    
    def ListAllPartitions(self,RespData):
        
            PartitionsLine = RespData.split(',')
            RespDataDict = {
                "code": 200,
                "Partitions": [
                    SinglePartition for SinglePartition in PartitionsLine
                    ]
            }
            cmdResponse=json.dumps(RespDataDict)
            
            return cmdResponse