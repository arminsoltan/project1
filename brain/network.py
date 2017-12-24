import datetime
import os
import menu
import url
import requests
import loginmenu
import datetime
#from .models import User
#########################################################################
def Log_in(session):
    os.system("clear")
    time = datetime.datetime.now()
    username = input("input your username: ").lower()
    password = input("input your password: ")
    info = dict(username=username,password=password)
    r = session.get(url.urls['log_in'],params=info)
    if ("you coudn't login" in str(r.content)):
        rec=input("your login has a problem. Do you want login again (y)")
        if (rec=="y"):
            Log_in(session)
        else:
            menu.init()
    input("your now login press any keys to show login menu ...")
    loginmenu.menu(session)
#########################################################################    
def Log_out(session):
    r = session.get(url.urls["log_out"])
    input("you log out press any keys to show main menu ...")
    menu.init()
#########################################################################
def Register(session):
    #print(url.urls['register'])
    os.system("clear")
    username = input("input your username: ").lower()
    password = input("input your password: ")
    if (len(username)==0 or len(password)==0):
        input("your username and password must be not empty presss any keys to register again ... ")
        Register(session)
    info = dict(username=username,password=password)
    r = session.get(url.urls['register'],params=info)
    if "invalid" in str(r.content):
        input("your registeration has a problem press any keys to show register again ...")
        
        Register(session)
    input("your registeration complete press any keys to show login menu ...")
    loginmenu.menu(session)
#########################################################################
def Dummy(session):
    print(datetime.datetime.now())
    r=session.get(url.urls["dummy"])
    print(r.content)
    if ("you are not login" in str(r.content)):
        input("you are not allowed to visit dummy page press any key to back to main menu ...")
        menu.init()
    input("press any key to back to login menu ...")
    loginmenu.menu(session)