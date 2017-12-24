import os
import network
import requests
def init():
    cmd=_show_menu()
    _run(cmd)

######################################
def _show_menu():
    os.system("clear")
    print("1.log in")
    print("2.Register")
    print("3.dummy page")
    print("4.Exit")
    cmd=input("Enter your number: ")
    if (_is_valid(cmd)):
        return cmd
    else:
        init()
    #_run(message)
######################################
def _run(message):
    session=requests.Session()
    if   message=="1":
        network.Log_in(session)
    elif message=="2":
        network.Register(session)
    elif message=="3":
        network.Dummy(session)
    elif message=="4":
        exit()
######################################
def _is_valid(message):
    if message in ["1","2","3","4"]:
        return True
    return False
