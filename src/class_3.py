import sys

sys.path.append(r'lib')

from sample_module import MyClass,MySubClass
from copy import deepcopy

me = MyClass("Jeyendhran",-7)
myfrnd = MyClass('Vishnu',25)
myclone = deepcopy(me)

print("My name is",me.getname(),'and my age is',me.getage(),"and I am from batch",MyClass.batch)
me.inc_age(50)
me.__class__.batch = 'Python LTT'  # way to update static variable
print("My name is",me.getname(),'and my age is',me.getage(),"after 50 years")
print("My clone's name is",myclone.getname(),'and his age will be same',myclone.getage(),"after 50 years")
print("My frnd's name is",myfrnd.getname(),'and his age is',myfrnd.getage(),"and he is also from batch",myfrnd.batch)
me.inc_noofClass()
me.inc_noofClass()
myfrnd.inc_noofClass()
print("No of classes attended by me",me.attendclass)
print("No of classes attended by myfrnd",myfrnd.attendclass)
print("No of classes attended by both",MyClass.total_classes)


mystudent = MySubClass("Balu",12,"basic topics")
print("\n\nMy student name is",mystudent.getname(),"and his age is",mystudent.age)
print("I teached the topic",mystudent.gettopic()+" to him")
print("The doc string of MyClass is",me.__doc__,"and 'me' is",me)

# while True:
#     try:
#         age = int(input("Enter your age"))
#         print("Your age is",age)
#         break
#     except ValueError:
#         print("Please enter valid age")


def readFile():
    f = open('dict_out.txt')
    print(int(f.read()))

try:
    readFile()
except FileNotFoundError:
    print("FileNotfounderror", sys.exc_info()[0])
#except ValueError:
#    print("ValueError", sys.exc_info()[0])
except Exception as e:
    print("Error is",sys.exc_info()[1])
    print(e.args,type(e),e)

try:
    raise Exception("MyException")
except Exception as e:
    print(e.args)