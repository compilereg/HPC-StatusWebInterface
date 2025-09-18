from mvc.controllers import settingsController as sc
from flask import Flask, request , session,  render_template , send_from_directory
from mvc.controllers import APIController as ac
import os
import json
############### The main file to start the flask server
CURDIR=os.getcwd()
app = Flask(__name__  , static_url_path= "") 
app.secret_key = 'D0ntEverL0gHereCauseAmHere'


@app.route('/')
def emptyRoot():
   return defaultRoute('index.html')


""" @app.route('/static')
def defaultIndex():
   return defaultRoute('index.html')

@app.route('/static/<filename>')
def defaultRoute(filename):
   return render_template(f"{filename}")
 """

@app.route('/static/<path:filename>')
def serve_report(filename):
    # You can add authorization checks here before serving the file
    # For example, check if the user is logged in or has permission
    return send_from_directory('static/', filename)
 
 
app.add_url_rule('/api/get/hoststate/<hostname>', view_func=ac.APIController.getHostState)
app.add_url_rule('/api/get/hostmem/<hostname>', view_func=ac.APIController.getHostMemory)
app.add_url_rule('/api/get/hostavgload/<hostname>', view_func=ac.APIController.getHostLoadAverage)

app.add_url_rule('/api/get/hostname/<hostname>', view_func=ac.APIController.getHostName)
app.add_url_rule('/api/get/hostprocesscount/<hostname>', view_func=ac.APIController.getHostProcesCount)
app.add_url_rule('/api/get/clusterpartitions/<hostname>', view_func=ac.APIController.getClusterParitions)
app.add_url_rule('/api/get/clusterpartition/<hostname>/<partitionname>', view_func=ac.APIController.getClusterParitionInfo)


if __name__ == '__main__':
    systemSettings = sc.Settings()
    print("Starting..")

    systemSettings.readINI()
    ServerSettings=json.loads(systemSettings.getServerINI())
    app.run(ServerSettings['listenip'],int(ServerSettings['listenport']),True)    
    
