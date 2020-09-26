import requests
import sys
import json
from welcome import welcome
from colorama import Fore, Back, Style
import os

def check(userArgv):
    try:
        print ( "\n" + Fore.YELLOW + "[*] Running Reputation Check Against"+ " ", userArgv + "\n")

        url = 'https://api.abuseipdb.com/api/v2/check'

        querystring = {
            'ipAddress': userArgv,
            'maxAgeInDays': '90'
        }

        headers = {
            'Accept': 'application/json',
            'Key': '2afe2f2928cadb589963ff2c5e5e3d3a703e16ba4afdc621b0058ac2acd2f2747a870e4a5c962010 '
        }

        response = requests.request(method='GET', url=url, headers=headers, params=querystring)
        # Formatted output
        decodedResponse = json.loads(response.text)
        print ( Fore.WHITE + "Domain: " + json.dumps(decodedResponse ["data"]["domain"]))
        print ( "Hostname: " + json.dumps(decodedResponse ["data"]["hostnames"]))
        print ( "Usage Type: " + json.dumps(decodedResponse ["data"]["usageType"]))
        print ( "Confidence of Abuse: " + json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]))
        print ( "Number Times of Reported: " + json.dumps(decodedResponse ["data"]["totalReports"]))
        print ( "Last Reported: " + json.dumps(decodedResponse ["data"]["lastReportedAt"]))
        print ( "Whitelisted: " + json.dumps(decodedResponse ["data"]["isWhitelisted"]) + "\n")

        #This conditional statement outputs the status of the ip address based on abuse of confidence
        if json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) == "100":
            print ( Fore.YELLOW + "The IP Address " + userArgv + " Is Malicious and well known for SSH Bruteforce Attacks" + "\n")
        elif json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) == "0":
            print ( Fore.GREEN + "The IP Address " + userArgv + " Is Not Malicious" + "\n")
        elif json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) < "20":
            print ( "The IP Address " + userArgv + " Is Probably Not Malicious But Should Be Investigated Further")
        elif json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) > "20":
            print ( "The IP Address " + userArgv + " Is Probably Malicious And Should Be Investigated Further")
        else:
            print ( "[*] IP Reputation Look up Complete!!!" + "\n" )

        print ( Fore.GREEN + "[*] IP Reputation Look up Complete!!!" + "\n" )
    except KeyError:
        print(Fore.RESET)
        os.system('clear')
        welcome()
        print("There was an error with the entry, please review your response. \nUse -h or --help to see help.")

