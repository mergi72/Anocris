# importing the requests library
import requests
import time
import json

from headersAnocris import *

class getHTTPAnocris():
    
    def __init__(self):
    # (( "Litvínov", 3837), ( "Most", 5490),( "Ossegg", 5552))
    #https://int43.anocris.com/rest/switchcity/3837 
    #https://int43.anocris.com/rest/geteverything
    # api-endpoint
        self.request = {"geteverything" : "rest/geteverything", "switchcity" : "/rest/switchcity/"}
        self.headers = headersAnocris()
        self.URL = "https://int43.anocris.com/" #rest/geteverything"
        self.data = None
        
    def get(self, reqst : str) -> list:
                
        self.headers = self.headers.get( self.request[reqst])
              
        # time unix format
        t = int( time.time())
        
        # defining a params
        PARAMS = {'_':t}
        
        # sending get request and saving the response as response object
        r = requests.get(url = self.URL + self.request[reqst], params = PARAMS, headers = self.headers)
        
        # extracting data in json format
        self.data = r.json()
        
        return self.data