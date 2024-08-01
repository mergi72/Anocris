from getHTTPAnocris import *
import json
from resourcesAnocris import *
from citiesAnocris import *

city = citiesAnocris()
getHTTP = getHTTPAnocris()
geteverything = getHTTP.getCity(referer = "city")

postHTTP = None

cityList = geteverything["user"]["cityList"]

resources = resourcesAnocris()
 
for i in range(len(cityList)):
    cityName = cityList[i]["cityName"]
    print(cityName)

    for key, value in city.city.items():
        if value == geteverything["user"]["cityID"]:
            print(key)

    for res in resources.products:
        if geteverything["resources"][res.capitalize()]["pending"] == True:
            print(res.capitalize() + " " + "True")