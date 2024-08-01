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
        self.request = {"geteverything" : "geteverything"}
        self.headers = None
    
    def getCity(self, referer : str):
        
        headers = headersAnocris()
        
        self.headers = headers.get(referer)
        
        URL = "https://int43.anocris.com/rest/geteverything"
        
        # location given here
        t = int( time.time())
        
        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'_':t}
        
        # sending get request and saving the response as response object
        r = requests.get(url = URL, params = PARAMS, headers = self.headers)

        #for rest in r:
        #    print( rest)
        
        # extracting data in json format
        data = r.json()
        
        return data