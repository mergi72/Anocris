# importing the requests library
import requests
import time
import json
from headersAnocris import *

class postHTTPAnocris():
    
    def __init__(self) -> None:
        self.rest = None
        self.req = requests()
        self.headers = headersAnocris()
    
    def switchcity(self, cityID = int, formfk = str, postHeaders) -> None:
        return self.req.post(url = "https://int43.anocris.com/rest/" + self.switchcity.__name__ + "/" + cityID, 
                             data = formfk, headers = headersAnocris.post(referer = "city"))
    
    def collectproduction(self, product = str) -> None:
        pass
    
    def startproduction(self, production = str, interval = str) -> None:
        pass
     
    #https://int43.anocris.com/rest/switchcity/3837
    #https://int43.anocris.com/rest/geteverything
    # api-endpoint
    URL = "https://int43.anocris.com/rest/startproduction/corn/600"
    
    # location given here
    t = int( time.time())
    
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'_':t}

    post_city = {"overviewFormfk" : "9a3d5e22950a22ea3f6829f8f5889a6c236aa967f81011c4cd850c202b9fbd401de6853c0a6ae40ba8834888d235d88e0e37180404dee6fc343eb9decd7630ec"}

    get_corn = "https://int43.anocris.com/rest/collectproduction/corn"
    start_production_corm_600 = "https://int43.anocris.com/rest/startproduction/corn/600"
    
    post_corn = {"resourceProductionFormCornfk" : "3711e2c717314ad2e484dda6f686152e4b119cb184f8a563b22e524ec29cf6324568707a3cbe24ac6fb0f3a3119cbbfd8ac669c418bf45f0f7fba7988a1fea55"}

    post_limestone = {"resourceProductionFormLimestonefk" : "a126fc6a456be854b1f018a3d6a16a88b7e90ea1e541371d6a53ba69c052f335aafb3b896a8a3d26f14bbc0d03c819749ada5e59fe658ebce044265be4d0e65b"}

    post_obsisian = {"resourceProductionFormObsidianfk " : "78113a18ae9fd32fd59de1bfad463d91566f5910000f85efd39d78ec01d08da1e358e5b2f84c66f082ddc298af97e05543d8004fcacd9777424c299a9e49c741"}

    post_cacao = {"resourceProductionFormCacaofk" : "d59e913c4008baf47a4eb234f73ee629515b5abd4ed2b45a6acfe4c9db20888a68c05d2302ad020cff30f53cccb05610ea99e3b88562ddc278f5e3a693e6ab23"}

    # sending get request and saving the response as response object
    r = requests.post(url = URL, data = post_corn, headers = HEADERS_CITY)

    # extracting data in json format
    data = r.json()

    print()