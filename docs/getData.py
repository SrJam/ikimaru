import requests
import sys
import json
from welcome import welcome
from colorama import Fore, Back, Style
import os

def getGeo(usA1):
    try:
        r = requests.get('http://ip-api.com/json/'+usA1)
        response = json.loads(r.text)

        #Iterate the data, filter & print ( data for specific fields
        print ( "\n" + Fore.YELLOW + "[*] Running Geo-location Check Against"+ " " + usA1 + "\n") 
        print ( Fore.WHITE + "Country: "+ response["country"])
        print ( "Region: " + response["regionName"])
        print ( "City: " + response["city"])
        print ( "Organization: "+response["org"])
        print ( "Longitude: ", response["lon"])
        print ( "Latitude: ", response["lat"])
        print ( "ISP: "+ response["isp"] + "\n") 
        print ( Fore.GREEN + "[*] Geo-IP Lookup Complete!!!" + "\n")

    except KeyError:
        print(Fore.RESET)
        os.system('clear')
        welcome()
        print("There was an error with the entry, please review your response\n")
