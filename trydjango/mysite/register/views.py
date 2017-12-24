from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import datetime
from register.models import User_Password
from django.core.urlresolvers import resolve
#import request
##################################################################################################
def Register(request):
    request.session.modified = True
    info=request.GET.dict()
    username=info["username"]
    password=info["password"]
    tmp=[]
    for i in User_Password.objects.all():
        tmp.append(i.username)
    print(tmp)
    for i in info["username"]:
        if (ord(i)<ord("a") or ord(i)>ord("z")):
            return HttpResponse("invalid")
    if username not in tmp: 
        a=User_Password.objects.create(username=username,password=password)
        a.save()
        request.session["username"]=username
        request.session.save()           
        return HttpResponse("Registration complete")
    return HttpResponse("invalid")
###################################################################################################
def Log_In(request):
    r=request.get_full_path()
    info=request.GET.dict()
    tmp={}
    for i in User_Password.objects.all():
        tmp[i.username]=i.password
    if (info["username"] in tmp) and (tmp[info["username"]]==info["password"]):
        request.session.set_expiry(999)
        request.session["username"]=info["username"]
        request.session.save()
        request.session.modified = True
        print(dict(request.session))
        return HttpResponse("you are login")
    return HttpResponse("you coudn't login")
    # def login(request):
    #     if request.method != 'POST':
    #     raise Http404('Only POSTs are allowed')
    # try:
    #     m = Member.objects.get(username=request.POST['username'])
    #     if m.password == request.POST['password']:
    #         request.session['member_id'] = m.id
    #         return HttpResponseRedirect('/you-are-logged-in/')
    # except Member.DoesNotExist:
    #     return HttpResponse("Your username and password didn't match.")
#######################################################################################################
def Log_Out(request):
    request.session.modified = True
    # def logout(request):
    #     try:
    #     del request.session['member_id']
    # except KeyError:
    #     pass
    # return HttpResponse("You're logged out.")
    print(request.session["username"])
    del request.session["username"]
    return HttpResponse("you are logged out.")
#######################################################################################################
def Dummy(request):
    print(dict(request.session))
    if request.session.has_key("username"):   
        return HttpResponse("This is your Dummy page  "+ str(request.session["username"])+"  welcome")
    #print(request.session["username"])
    return HttpResponse("you are not login")
