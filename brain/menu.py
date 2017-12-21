import os
import network
def init():
    cmd=_show_menu()
    _run(cmd)

######################################
def _show_menu():
    os.system("clear")
    print("1.log in")
    print("2.log out")
    print("3.Register")
    print("4.Exit")
    cmd=input("Enter your number: ")
    if (_is_valid(cmd)):
        return cmd
    else:
        _show_menu()
    #_run(message)
######################################
def _run(message):
    if   message=="1":
        network.Log_in()
    elif message=="2":
        network.Log_out()
    elif message=="3":
        network.Register()
    elif message=="4":
        exit()
######################################
def _is_valid(message):
    if message in ["1","2","3","4"]:
        return True
    return False
