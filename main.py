from mvc.controllers import settingsController as sc
from flask import Flask, request , session
from mvc.controllers import APIController as ac
import json
############### The main file to start the flask server
app = Flask(__name__)
app.secret_key = 'D0ntEverL0gHereCauseAmHere'


@app.route('/')
def hello_world():
   return 'Hello API!.'

app.add_url_rule('/api/get/hoststate/<hostname>', view_func=ac.APIController.getHostState)
app.add_url_rule('/api/get/hostmem/<hostname>', view_func=ac.APIController.getHostMemory)
app.add_url_rule('/api/get/hostavgload/<hostname>', view_func=ac.APIController.getHostLoadAverage)
app.add_url_rule('/api/get/hostprocesscount/<hostname>', view_func=ac.APIController.getHostProcesCount)
app.add_url_rule('/api/get/clusterpartition/<hostname>', view_func=ac.APIController.getClusterParition)


if __name__ == '__main__':
    systemSettings = sc.Settings()
    print("Starting..")

    systemSettings.readINI()
    ServerSettings=json.loads(systemSettings.getServerINI())
    app.run(ServerSettings['listenip'],int(ServerSettings['listenport']),True)    
    
