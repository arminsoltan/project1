from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import datetime
from register.models import User_Password
from django.core.urlresolvers import resolve
#from register.models import User
#from .forms import NameForm
# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

def Register(request):
    
    current_url = request.get_full_path()
    content=current_url.split("/")
    if "username" in content:
        for i in range(len(content)):
            if (content[i]=="username"):
                username=content[i+1]
            if (content[i]=="password"):
                password=content[i+1]
        tmp=[]
        for i in User_Password.objects.all():
            tmp.append(i.username)
        if username not in tmp: 
            a=User_Password.objects.create(username=username,password=password)
            a.save()           
    #return HttpResponse(current_url)
    time=datetime.datetime.now()
    return HttpResponse(str(time))

def Log_In(request):
    current_url = request.get_full_path()
    content=current_url.split("/")
    f=True
    if "username" in content:
        for i in range(len(content)):
            if (content[i]=="username"):
                username=content[i+1]
            if (content[i]=="password"):
                password=content[i+1]
        tmp={}
        for i in User_Password.objects.all():
            tmp[i.username]=i.password
        if (username in tmp) and (tmp[username]==password):
            return HttpResponseRedirect('/login/')
    #if username not in tmp:
    return HttpResponse("you coudn't login")
def Log_Out(request):
    return HttpResponse("hello world2")
def index3(request):
    return HttpResponse("hello world3")
