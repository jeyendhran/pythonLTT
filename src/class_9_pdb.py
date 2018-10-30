#Pdb debugging
import pdb

# def myfunc(myint):
#     print("my Int value is",myint)
#     ret = 10/myint
#     print("Return int is",ret)
#     return ret

# function is called as a string to pdb.module
#print("pdb.run",pdb.run("myfunc(2)"))
#print("pdb.runeval",pdb.runeval("myfunc(2)"))
#pdb.runcall(myfunc,0)
# try:
#     myfunc(0)
# except:
#     import sys
#     tb = sys.exc_info()[2]
#     pdb.post_mortem(tb)

def f1(arg1):
    myvar = arg1 + 1
    print("f1 says",myvar)
    for i in range(10):
        print(i)
    myadd(arg1, myvar)
    return f2(myvar)

def f2(arg):
    var = arg + 1
    var = 2 * var - 17
    arg = 3 *(var + 12)
    myadd(arg,var)
    var = var + arg
    print("f2 says",var)
    return f3(var)

def f3(arg):
    var = arg + 1
    print("f3 says",var)
    return f4(var)

def f4(arg):
    var = arg + 1
    var = 2 * var - 17
    arg = 3 * (var + 12)
    var = myarith(var,arg)
    print("f4 says",var)
    return var

def myadd(x,y):
    print("x is ",x)
    print("Sum of",x,y,"is",x+y)

def myarith(x,y):
    x = 9/x + 1.8*y
    y = 4.5 *(x/9 + 2 * y)
    return x+y

pdb.run("f1(1)")
