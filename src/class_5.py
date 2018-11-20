# Database connectivity
import pymysql

# Open database connection
db = pymysql.connect("localhost","demo","demo","test")
# prepare a cursor
cursor = db.cursor()

#sqlquery = "SELECT VERSION()"
#cursor.execute(sqlquery)
# get the result of the executed command
# data = cursor.fetchone()
# print("DB version is",data)

#sqlquery = "INSERT INTO pets(name,owner,age) VALUES('%s','%s','%d')" %('puppy','Arnold',12)
#sqlquery = "INSERT INTO pets(name,owner,age) VALUES('buzy','John',10)"
# try:
#     # to execute a command
#     cursor.execute(sqlquery)
# except:
#     print("Rollback")
#     db.rollback()
# else:
#     db.commit()

# age = int(input("Enter the age of pet:"))
# # sqlquery = "SELECT * from pets where age <= 12"
# sqlquery = "SELECT * from pets where age >= %d" %(age
# try:
#     cursor.execute(sqlquery)
#     results = cursor.fetchall()
#     for result in results:
#         print("Each row is",result)
#         print("Name is",result[0],"Owner is",result[1],"and the age of dog is ",result[2])
# except:
#     print("Error in executing command")

# sqlquery = "UPDATE pets set age = 15 where owner = '%s'" %('Arnold')
# try:
#     cursor.execute(sqlquery)
# except:
#     print("Exception occur")
#     db.rollback()
# else:
#     db.commit()
# disconnect the database connection
db.close()


import sys

# for arg in sys.argv[1:]:    # read data from command variables
#     try:
#         f = open(arg)
#     except IOError:
#         print("File not found")
#     else:
#         print(f.read())
#         f.close()

class MyException(Exception): # User defined exception
    def __init__(self):
        return
    def __str__(self):
        return "Myexception occurred"

def createException():
    raise MyException

def divide(x,y):
    return x/y

try:
    print(divide(10,2))
    #print(divide(10,0))
    #createException()
except Exception as e:
    print("Exception",str(e))
    raise
finally:
    print("Ok I understand exception")

print("Outside exception")


class NewClass(object):
    def __new__(cls, *args, **kwargs):
        print("cls",cls)
        print("args", args)
        print("kargs", kwargs)
        instance = super(NewClass,cls).__new__(cls)
        return instance

    def __init__(self,a,b):
        print("Init called")
        self.a = a
        self.b = b

    def __getitem__(self, item):
        print("getitem called")
        return "The value of "+item+" is "+str(getattr(self,item))

    def __call__(self, *args, **kwargs):
        print("call called")

n = NewClass(10,20)
print(n,n['a'],n['b']) #
n()
n1 = NewClass(20,30)
print("Second obj",n1)

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        print("cls",cls)
        print("args", args)
        print("kargs", kwargs)
        if not hasattr(cls,'obj'):     # To create singleton object
            cls.obj = super(Singleton,cls).__new__(cls)
        return cls.obj

    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("Init called")

import copy
n = Singleton(10,20)
n1 = Singleton(15,30)
print("Instance",n)
print("Instance n1",n1)
print(n.a,n.b)
print(n1.a,n1.b)

n2 = copy.deepcopy(n1)  # then also it will not create new object same obj is referenced

def mymethod(self,a):
   print(a)


class Monostate:
    myvar = {"2":"3"}
    def __init__(self):
        self.a = 1
        #self.__dict__ = self.myvar

m = Monostate()
m1 = Monostate()
print(m.__dict__,m1.__dict__)
m.b = 10
m1.c = 20
m1.amethod=mymethod
print(m,'\n',m1)
print(m.__dict__,m1.__dict__)
#print(m.b,m1.b)
print(m.myvar,m1.myvar)

class MyMetaClass(type):
    def __call__(self, *args, **kwargs):
        return type.__call__(self,*args,*kwargs)

class str():
    def __init__(self,a,b):
        self.firstname = a
        self.lastname = b

name = str("Jeyendhran","Sridhar")
print("Full name is",name.firstname,name.lastname)


class Decorate:
    def __init__(self,func):
        self.f = func
    def __call__(self, *args, **kwargs):
        print("I am also added")
        self.f()

@Decorate
def mynormalfunc():
    print("Hai I am simple")
mynormalfunc()

def decoratorfunc(func):
    def innerfunc():
        print("+++++++++")
        func()
        print("*********")
    return innerfunc

#f = decoratorfunc(mynormalfunc)
#f()
