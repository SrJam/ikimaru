#Imports
import requests
import json
from colorama import Fore, Back, Style
import os
from commands import listCommand, command
from helps import help
from welcome import welcome, animation
from getData import getGeo
from checkIp import check
from myip import myIp
from fullcontact import fullcontact
import time
import sys


def main():


   if sys.version_info<(3,0):
      sys.stderr.write("\nYou need python 3.0 or later to run this script\n")
      sys.stderr.write("Please update and make sure you use the command " + '\033[1m' + "python3 ikimaru.py" + '\033[0m' + "\n\n")
      sys.exit(0)

   try:

      os.system('clear')
      welcome()
      animation()

      userArgv = input('-> ')
      print(Style.RESET_ALL)

      usA1 = userArgv.split(" ")[0]
      split = (len(userArgv.split (" ")))
      if split >= 2:
         usA2 = userArgv.split (" ")[1]

      if (len(userArgv) > 1) and userArgv.startswith('-'):
         if userArgv == "--help" or userArgv == '-h':
               os.system('clear')
               welcome()
               help(userArgv)

         elif userArgv == '-b' or userArgv == '--banner':
            os.system('clear')            
            welcome()
         elif userArgv == '-c' or userArgv == '--commands':
            os.system('clear')            
            welcome()
            listCommand()

      elif userArgv == 'fullcontact' or userArgv == '-f':
         fullcontact()


      elif userArgv == 'localhost':
         ip = myIp()
         os.system('clear')
         welcome()
         userArgv = ip
         getGeo(userArgv)
         check(userArgv)


      else:
         if usA1 == str:
            sys.exit(0)

         else:  
            os.system('clear')
            welcome()
            print(Fore.CYAN + 'Wait a minute.....')
            getGeo(usA1)
            check(usA1)
            if (len(userArgv.split(" ")) > 1):
               usA1 = userArgv.split(" ")[0]
               usA2 = userArgv.split(" ")[1]
               command(usA2, usA1)

   except KeyboardInterrupt:
      os.system('clear')
      welcome()
      keyCenter = "The program was interrupted by the user's keyboard. I hope to see you soon :)\n".center(85)
      print(keyCenter)
main()
