import datetime
import os
import menu
import url
import requests
#from .models import User

def Log_in():
    time=datetime.datetime.now()
    username=input("input your username: ")
    password=input("input your password: ")
    r = requests.get(url.urls['log_in'])
    if "you coudn't login" in str(r.content):
        input("press any keys to login again  ...")
        Log_in()
    else:
        input("press any keys to back to menu ...")
    # for i in User_Password.objects.all():
    #     r
    #r=requests.post(url.urls['register'],"kheili khari")
    print(str(r.content))
    print(r)
def Log_out():
    r = requests.get(url.urls['log_out'])
def Register():
    print(url.urls['register'])
    username=input("input your username: ")
    password=input("input your password: ")
    if (len(username)==0 or len(password)==0):
        input("your username and password must be not empty presss any keys to register again ... ")
        Register()
    r = requests.get(url.urls['register']+"username"+'/'+username+'/'+"password"+'/'+password+'/')
    input("Press any keys to back to menu...")
    menu.init()
