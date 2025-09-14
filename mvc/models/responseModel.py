import json
class ResponseModel:
    
    
    def buildResponse(self,msg,code):
        response={}
        response['data']=msg
        response['code']=code
        return json.dumps(response)