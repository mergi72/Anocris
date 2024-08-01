from getHTTPAnocris import *
import json
from resourcesAnocris import *
from citiesAnocris import *

cities = citiesAnocris()
getHTTP = getHTTPAnocris()
#geteverything = getHTTP.getCity(referer = "city")

postHTTP = None

cityList = cities.getList("geteverything")

resources = resourcesAnocris()
 
for i in range(len(cityList)):
    cityName = cityList[i]["cityName"]
    print(cityName)

    print(cityList[i]["cityID"])

    print(cityList[i]["resourcesPending"])

d = cities.geteverything
            
print(d)