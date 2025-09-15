import json
import math

class ClusterInfo:
    
    def GetPartitionSummary(self,RespData):
        
        ##The sinfo returns AVAIL,NODES,NODES(A/I),TIMELIMIT,GRES,SOCKETS,CORES,MEMORY
        PartitionSummary = RespData.split(',')
        PState=PartitionSummary[0]
        PTotalNodes=int(PartitionSummary[1])
        PAllocatedodes=int(PartitionSummary[2].split("/")[0])
        PIdleNodes=int(PartitionSummary[2].split("/")[1])
        PTimelimit=PartitionSummary[3]
        PGresDevice=PartitionSummary[4]
        PSocketPerNode=int(PartitionSummary[5])
        PCoresPerNode=int(PartitionSummary[6])
        PMemPerNode=int(PartitionSummary[7])
        PTotalWorkingNodes =  PAllocatedodes + PIdleNodes 
        ###PTotalWorkingSockets total number of sockets in all working nodes (Allocaed + Idel)
        PTotalWorkingSockets= PTotalWorkingNodes * PSocketPerNode
        PTotalWorkingCores = PTotalWorkingNodes * PCoresPerNode
        PTotalWorkingMemory = math.floor((PTotalWorkingNodes * PMemPerNode) / 1024)
         
        RespDataDict = {
                "code": 200,
                "Data": {
                    "state": f"{PState}",
                    "time_limit": f"{PTimelimit}",
                    "total_nodes": f"{PTotalNodes}",
                    "total_allocated": f"{PAllocatedodes}",
                    "total_idle": f"{PIdleNodes}",
                    "gres_devices": f"{PGresDevice}",
                    "total_sockets": f"{PTotalWorkingSockets}",
                    "total_cores": f"{PTotalWorkingCores}",
                    "total_memory": f"{PTotalWorkingMemory}G"
                }
            }
        cmdResponse=json.dumps(RespDataDict)
            
        return cmdResponse
    
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