import unittest


# def myerrorfun():
#     '''
#     >>> myerrorfun()
#     Traceback (most recent call last):
#     RuntimeError: my error
#     '''
#     raise RuntimeError("my error")

# def myclassfun(obj):
#     """
#     >>> myclassfun(MyClass("Jeyendhran",23)) #doctest: +ELLIPSIS
#     <sample_module.MyClass object at 0x...>
#     """
#     return obj

# def myfun(a,b):
#     """
#     >>> myfun(2,3)
#     6
#     >>> myfun('a',4)
#     'aaaa'
#     """
#     return a*b
#
# def myadd(a,b):
#     """
#     >>> myadd(4,5)
#     9
#     >>> myadd('a','b')
#     'ab'
#     """
#     return a+b

import doctest
if __name__ == '__main__':
    #doctest.testmod(verbose=True)
    doctest.testfile("doctest_sample.txt",verbose=True)

