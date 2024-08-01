from getHTTPAnocris import *

class citiesAnocris():
      
    def __init__(self) -> None:
        self.cities = None
        self.getHTTP = getHTTPAnocris()
        self.cities = None
        self.geteverything = None
        
    def getList(self, reqst: str) -> int:
        self.geteverything = self.getHTTP.get(reqst)
        return self.geteverything["user"]["cityList"]
    
    def get(self, name: str) -> int:
        return self.city[name]lllllll