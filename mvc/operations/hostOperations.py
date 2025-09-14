from mvc.controllers import settingsController as sc
from mvc.models import responseModel as rm
import paramiko

class HostOperations:
    
    #Return true if host is live, false otherwise. The @classmethod allows to call the class by its name
    @classmethod
    def getHostState(self,hostname):
        if hostname=="team1":
            return True
        else:
            return False
        
    @classmethod    
    def executeRemoteCommand(self,hostname,cmd):
        
        resp = rm.ResponseModel()
    
        systemSettings = sc.Settings()
        AuthKeyFile = systemSettings.getServerINIJString()['authkey']
        AuthUser= systemSettings.getServerINIJString()['authuser']
        
        sshClient = paramiko.SSHClient()
        sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            sshClient.connect(hostname, port=22, username=AuthUser, key_filename=AuthKeyFile)
            stdin, stdout, stderr = sshClient.exec_command(cmd)
            output = stdout.read().decode('utf-8')
            error = stderr.read().decode('utf-8')
        
            if output:
                ResCode=200
                ResString=output
            if error:
                print("Command Error:")
                print(error) 
            
        except paramiko.AuthenticationException:
            ResCode=401
            ResString = "Authentication failed. Check username and authentication key."
        except paramiko.SSHException as e:
            ResCode = 400
            ResString = f"SSH error: {e}"
        except Exception as e:
            ResCode = 408
            ResString = f"An unexpected error occurred: {e}"
        finally:
            sshClient.close()
         
         
        return  resp.buildResponse(ResString,ResCode)