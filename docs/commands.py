import requests
import sys
import json
from colorama import Fore, Back, Style
import os


def command(usA2, usA1):
   print("--------------------------------------------------------------------- \n")
   if usA2 == '--nmap' or usA2 == '-n':
      os.system(' cd modules && sh nmap.sh ')
      print(Fore.CYAN + '---------------------------------------------------------------------')
      print("If Nmap is slow to respond don't worry, sometimes it takes a while.")
      print('--------------------------------------------------------------------- \n \n')
      ip = usA1
      nmapcc = os.system('nmap ' + ip)
      print(nmapcc)
      sys.exit(0)

   else:
      print('Review the command after the IP, \nwrite python geo-recon.py --command or -c to see the avaliables commands')
   print("\n##################################### \n")


def listCommand():
      print(Fore.WHITE+'# Commands')

      print("--help or -h                         (Display this)")

      print("123.456.789.10 --nmap or -n          (Nmap standard use)")

      print("123.456.789.10                       (Standard use, infos about IP)")

      print("--commands or -c                     (Display avaliable commands)")

      print("localhost                            (Stardad use, infos about YOUR IP address)")

      print("localhost -n or --nmap               (Stardad use, infos about YOUR IP address with Nmap log)")

      print("fullcontact                          (Use this to have options for stalking over the phone, emails")
      print("                                     and names. Theoretically it works best with companies)")