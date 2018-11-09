from django.shortcuts import render
from django.template import Template,Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db import models
import datetime

# Create your views here.

class Person():
    def __init__(self,name,age):
        self.name, self.age = name, age
    def names(self):
        raise SilentError

class SilentError(AssertionError):
    silent_variable_failure = True

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
