import os
import network
import menu
############################################################
def menu(session):
    os.system("clear")
    print("1.log out")
    print("2.dummy page")
    cmd=input()
    if (_is_valid(cmd)):
        _run(cmd,session)
    else:
        input("your input is not correct press any keys to try again ... ")
        menu()
################################################################
def _is_valid(message):
    if (message in ["1","2","3"]):
        return True
    return False
##############################################################
def _run(message,session):
    if (message=="1"):
        network.Log_out(session)
    elif(message=="2"):
        network.Dummy(session)
