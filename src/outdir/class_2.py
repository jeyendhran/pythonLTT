# sample function
def addition(a,b):
    '''
    addition(int,int) -> int
    returns addition of 2 numbers'
    '''
    return a+b

if __name__ == '__main__': # looks like main function
    c = addition(5,6)
    print("addtion of given numbers is",c)
    print("The doc string of the function addition is",addition.__doc__)


def listFunction(li,element):
    #li = [1,2,3,4]
    li.append(element) # global list will updated
    print("List inside function",li)

lis = [1,2,3,4]
listFunction(lis,5)
print("The new list is",lis)

def addstudent(name,age=3,area="Chennai"):
    print("Name is",name)
    print("Age is",age)

addstudent('Jeyendhran')
addstudent('Sathish',5)
addstudent('Deepan')


def add(a=10,b=20,c=30):
    print("a's value",a)
    print("b's value", b)
    print("c's value", c)
    return a+b-c

print(add(1,2,3))
print(add(b=2,c=3,a=1))
print(add(1,c=2,b=3))
print(add(a=1))


def varargs(*args):
    print(args)
    for i in args:
        print(i)

varargs('1','2','3')
varargs('a','b','c','d',{"name":"Jey",'age':23},1,2,3,4)

def varkargs(*args,**kwargs):
    print("key word arguments",kwargs)
    print('non keyword arguments',args)

varkargs(1,2,3,4,5,6,7,8,9,age=23,name="jeyendhran")


def multiply(a,b):
    return a*b

def subtract(a,b):
    return a-b

def operation(func,a,b):
    if callable(func):
        return func(a,b)
    else:
        return "Invalid function"

def double(a):
    return 2*a

print(operation(addition,2,3))
print(operation(subtract,2,3))
print(operation(multiply,2,3))
print(operation(lis,2,3))
def operationOne(func,a):
    return func(a)



# Lambda function

squa = lambda x,y:x*y
print("Square of 4 is",squa(4,13))
print(operationOne(lambda x:x*x,6))
print(operation(squa,6,2))
print(addition.__code__.co_nlocals,addition.__code__.co_argcount,addition.__code__.co_varnames)


def generate(url):
    return lambda website:url+website

ie = generate("http://")
cr = generate("https://")
print(ie("www.google.com"))
print(cr("www.google.com"))

# map and filter in list
def isEven(no):
    return no % 2 == 0

print(lis,list(map(double,lis)))
print(lis,list(filter(isEven,lis)))

lis1 = [1,2,3,4,5]
lis2 = [5,4,3,2,1]
print(list(map(lambda a,b:a*b, lis1, lis2)))

from functools import reduce
lis1 = [1,2,3,4,5]
lis2 = [5,4,3,2,1]
print(reduce(lambda a,b:a*b, lis1),reduce.__doc__)


name = 'sjeyandhran'
names = list(name)
print(names)
names.remove('a')
names.insert(4,'e')
name = str(names)
print(reduce(lambda a,b:a+b,names))
print(''.join(names))
print(list(zip(lis1,lis2)))
print(dict(zip(lis1,lis2)))

lis = {double(x) for x in lis1 if x%2==0} # comprehension with filter
print(lis)

ls = [1,2,3,4,5]
print([x*2 for x in [y+1 for y in ls]]) # nested comprehension

name = "jeyendhran sridHar"
print(name.lower(),name.upper(),name.capitalize(),name.title())

def checkCondition(ans):
    while True:
        if ans.upper().strip(' ') == "YES":
            print("OK thanks")
            break
        elif ans.upper().strip(' ') == "NO":
            print("Sorry for your inconvience")
            break
        else:
            ans = input(("Enter valid answer"))
            #checkCondition(ans)

#ans = input("Enter yes/no:")
#checkCondition(ans)

# age = input("Enter age")
# if age.isdigit():
#     age = int(age)
#     print("Entered age is",age,end='OK')
# else:
#     print("Invalid age")

print("hello","world",sep = ':',end = ',')
num = 5*2*34*12/4*4/23
print("\nThe value of a number is %.3f" %num)
fname,lname = 'jeyendhran','sridhar'
print(':%-20s:%20s' %(fname,lname))

name = 'j,e,y,e,n,d,h,r,a,n'
name =name.split(',')
print(name)
print(''.join(name))


def file_write(filename):
    f = open(filename,'w')
    f.write("Hai I am Jeyendhran.\n")
    f.write("I am a python developer.\n")
    f.close()

def file_read(filename):
    f = open(filename) # default mode is read
    print("f.read",f.read())
    f.seek(9,0) # to move cursor to start of file
    print("f.readline",f.readline())
    f.seek(0)
    print("f.readlines",f.readlines())

def file_writes(filename):
    f = open(filename,'a')
    f.write("\n")
    f.writelines(list(map(lambda x:str(x)+"|",[11,12,13]))) # to write a list/tuple/set/dict to a file
    f.close()

def file_reads(filename):
    f = open(filename)
    cnt = f.readlines()
    cnt = list(map(lambda x: x.strip(), cnt))
    print('cnt',cnt)
    cnt = list(map(lambda x: x.strip("|"), cnt))
    print('cnt', cnt)
    cnt = list(map(lambda x: x.split("|"), cnt))
    print(cnt)

files = 'python.txt'
#file_writes(files)
#file_reads(files)


# Programs to read and write dict object to a file
def file_write_dict(filename):
    f = open(filename,'w')
    dic = {'a':[1,2,3,11,12,13,14],'b':[4,5,6],'c':[7,8,9]}
    header = ','.join(dic.keys())
    f.write(header+'\n')
    print(list(header))
    f.close()

def file_read_dict(filename):
    f = open(filename)
    cnt = tuple(map(lambda x:x.strip(),f.readlines()))
    print('cnt',cnt)
    cnt = list(map(lambda x:x.split(','),cnt))
    print('cnt',cnt)
    cnt = dict(map(lambda x: (x[0],int(x[1])), cnt))
    print('cnt', cnt)
    #
    # cnt = list(map(lambda x:x.strip(),f.readlines()))
    # cnt = list(map(lambda x:x.strip(),cnt))
    #
    # import numpy as np
    # cnt_arr = np.array(cnt[1:])
    # cnt_list = list(cnt_arr.T)
    # cnt_list = list(map(lambda x:list(x),cnt_list))
    # print(dict(zip(cnt[0],cnt_list)))

filename = 'dict_out.csv'
file_write_dict(filename)
#file_read_dict(filename)
