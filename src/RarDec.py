import sys
import os
import site

def RarDec():
    try:
        arg = sys.argv[1]
        with RarFile(arg, 'r') as rar:
            rar.printdir()
            print('extracting in progress...')
            rar.extractall()
            print('Done!')
    except IndexError:
        print('\033[31m' + 'Error' + ': You must specify the file to extract')
    """try:
        arg = file
        with RarFile(arg, 'r') as rar:
            rar.printdir()
            print('extracting in progress...')
            rar.extractall()
            print('Done!')
    except IndexError:
        print('\033[31m' + 'Error' + ': You must specify the file to extract')"""

try: 
   from rarfile import RarFile
   RarDec()
except ImportError:
   print ("RarDec needs the rar file package, do you want to install it? (y/n)")
   res = input()
   if res == 'y':
       import pip
       cmd = "pip3 install rarfile"
       #print ("Requests package is missing\nPlease enter root password to install required package")
       os.system(cmd)
       #reload(site)
       print('Now you can unpack your rar file')
       """print('Enter the name of your file')
       file = input()
       RarDec(file)"""
   else:
       exit()
        


