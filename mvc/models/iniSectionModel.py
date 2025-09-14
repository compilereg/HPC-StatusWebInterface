class iniSectionModel:
    sectionSettings = {}
    

    def emptySettings(self):
        self.sectionSettings.clear()
        
    def setValue(self,key,value):
        self.sectionSettings[key] = value

    def getValue(sel,key):
        return self.sectionSettings[key]

    
    
    
        