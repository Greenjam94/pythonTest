import requests

from CommonStuff import common

x = requests.get(common.api_base()+'1/')

print(x.text)

###
#"""
#PS C:\Users\Greenjam94\Code\pythonTest> & C:/Users/Greenjam94/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Greenjam94/Code/pythonTest/MyProject/ThingOne/getAPI.py
#Traceback (most recent call last):
#  File "c:\Users\Greenjam94\Code\pythonTest\MyProject\ThingOne\getAPI.py", line 3, in <module>
#    from MyProject import common
#ModuleNotFoundError: No module named 'MyProject'
#"""
