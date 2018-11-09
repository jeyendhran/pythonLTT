from django.shortcuts import render
from django.template import Template,Context
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from django.db import models
from django.forms import ModelForm, Textarea
from Myapp.models import Publisher
import hashlib
import datetime
import os

# Create your views here.

class Person():
    def __init__(self,name,age):
        self.name, self.age = name, age
    def names(self):
        raise SilentError

class SilentError(AssertionError):
    silent_variable_failure = True

def checkLogin(func):
    def loginfun(request):
        if 'uname' in request.COOKIES and 'pwd' in request.COOKIES:
            return func(request)
        else:
            return redirect('/login')
        return func()
    return loginfun



#To get the name from URL and send the same as response
def say_hello(request,name):
    if name == "sathish":
        raise SyntaxError("Name is invalid")
        return HttpResponse(SyntaxError("Error"))
    else:
        return HttpResponse("Hai hello to "+name)

def say_hello_all(request):
    return HttpResponse("Hai hello to everyone")


def date_time(request):
    date = datetime.datetime.now()
    print(date)
    return render_to_response('current_datetime.html',{"now":date})
    #return HttpResponse(date)

def addhours(request,addTime):
    t = addTime.split(".")
    hrs = int(t[0])
    min = 0
    if len(t)>1:
        min = int(t[1])
    dt = datetime.datetime.now() + datetime.timedelta(hours=hrs,minutes=min)
    return HttpResponse(dt)


def getTemplate(request,content):
    t = Template("Name is {{person.name}} and the age is {{person.age}}<br>")
    t_array = []
    for n in content.split(","):
        name = n.split(":")
        p = Person(name[0],name[1])
        t_array.append(t.render(Context({"person":p})))
    return HttpResponse(t_array)

@checkLogin
def getForm(request):
    #return render_to_response('myform.html',{})
    return render(request,"myform.html")

@checkLogin
def searchtext(request):
    p = Publisher.objects.filter(name=request.POST['search'])
    if p:
        return render_to_response('myform.html',{'data':p.values()[0]})
        #return HttpResponse("The publisher info with searched name is "+str(p.values()[0]))
    else:
        return render_to_response('myform.html', {'data':"No data found"})
        #return HttpResponse("No data found for the publisher name '"+request.GET['search']+"'")

@checkLogin
def update(request):
    name = request.GET['name']
    address = request.GET['address']
    country = request.GET['country']
    state = request.GET['state']
    city = request.GET['city']
    p = Publisher.objects.get(name=name)
    if p:
        p.name = name
        p.address = address
        p.country = country
        p.state = state
        p.city = city
        p.save()
        return HttpResponse("Saved")

class MyForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ['name','address','city','state_province','country']
        widgets = {
            'name': Textarea(attrs={'cols': 10, 'rows': 10}),
        }
        labels = {
            'name': 'Writer',
        }

@checkLogin
def getMyform(request):
    form = MyForm()
    print(form)
    return render_to_response("mymodelform.html",{'form':form})
    #return HttpResponse(form)


def getcookie(request):
    return render(request,"mycookie.html")

def setcookie(request):
    message = 'Cookie saved'
    response = HttpResponse(message)
    print(request.session.test_cookie_worked())
    if request.session.test_cookie_worked(): #check if cookie is allowed or not
        if 'mycookie' not in request.COOKIES:  # to check if already a cookie is set with same key
            response.set_cookie('mycookie',request.GET['cookie'])
        else:
            response = HttpResponse("Cookie already exists")
    else:
        response = HttpResponse("Enable cookies first")
    return response


def login(request):
    return render(request,"login.html")


#To check if username and password from req is equal to login.txt file contents and set cookie if success
def validate_login(request):
    response = HttpResponse("Cookie setted")
    name = request.POST['username']
    pwd = request.POST['password']
    fp = open(os.path.abspath("Myapp/login.txt"))
            #"/home/cisco/mysite/Myapp/login.txt") #Other way to get file path
    cred = fp.read()
    cred = cred.split(":")
    if name == cred[0] and pwd == cred[1]:
        response = render(request, "myform.html")
        response.set_cookie("uname",name)
        response.set_cookie("pwd",pwd)
    else:
        response = HttpResponse("Invalid credentials")
    return response

def logout(request):
    response = HttpResponse()
    if 'uname' in request.COOKIES and 'pwd' in request.COOKIES:
        response = redirect('/login')
        response.set_cookie('uname',max_age=-1)
        response.set_cookie('pwd', max_age=-1)

    return response