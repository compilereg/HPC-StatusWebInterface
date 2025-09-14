class settingsModel:
    serverSettings = {}
    

    def emptySettings(self):
        self.serverSettings.clear()
        
    def setVServerValue(self,key,value):
        self.serverSettings[key] = value

    def getServerValue(self,key):
        return self.serverSettings[key]
    
    def getServer(self):
        return self.serverSettings
    