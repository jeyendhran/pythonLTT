#regular exp
import re

patrn1 = re.compile('san$')
name = "Sudharsan"
if patrn1.search(name):
    print("It matched with san")
else:
    print("Not matched")

patrn2 = re.compile('(.+)([0-9]{3})')
target = 'dfssegds4576457dsgsdg4636sdgs'
match = patrn2.search(target)
if match:
    print("match.group(0)",match.group(0))
    print("match.group(1)", match.group(1))
    print("match.group(2)", match.group(2))
else:
    print("Not matched")

patrn3 = re.compile("(^[a-z0-9\W?]+)@([a-z]{3,5})\.([a-z]{,3}$)")
target = "jeyendhran.s@hcl.com"
match = patrn3.search(target)
if match:
    print("match.group(0)",match.group(0))
    print("match.group(1)", match.group(1))
    print("match.group(2)", match.group(2))
    print("match.group(3)", match.group(3))
else:
    print("Not matched")

patrn4 = re.compile("^(\+91|\+44)?[0-9]+$")      # match starts with either +91 or +44 nor both numbers of any length
target = "324325"
match = patrn4.search(target)
if match:
    print("It matched")
else:
    print("Not matched")

print(re.compile("\s+").findall('total 10, present 8, absent 2'))


patrn5 = re.compile("hello$",re.MULTILINE)
patrn6 = re.compile(".+",re.DOTALL)
target = "hello\nworld"
print(patrn5.search(target))
print(patrn6.search(target))

patrn7 = re.compile(r"\W+")
print(patrn7.split("This string is splitted based on, space and white spaces"))
print(patrn7.split("This string is splitted based on, space and white spaces",3))

patrn8 = re.compile("green|red|blue")
print(patrn8.sub("Color","blue pant and red shirt"))
print(patrn8.sub("Color","blue pant and red shirt",count=1))

f = open("dict_out.txt")
for l in f:     # buffered reading a file i.e for reading larger files efficiently
    print(l)


def iterate(iterable):
    it = iter(iterable)
    while True:
        try:
            item = next(it)
        except:
            break
        else:
            print(item)


# mylist = [1,2,3,4,5,6,7,8,9]
# iterate(mylist)
# mylistiter = iter(mylist)
# print(next(mylistiter))
# print(next(mylistiter))

# myset = {'a','b','c'}
# mysetiter = iter(myset)
# print(next(mysetiter))
# print(next(mysetiter))
#
# mystr = "jeyendhran"
# mystriter = iter(mystr)
# print(next(mystriter))
# print(next(mystriter))

class MyRepeater:
    def __init__(self,val):
        self.value = val
    def __iter__(self):
        print("Iterator func called")
        return MyRepeatorIterator(self)

class MyRepeatorIterator:
    def __init__(self,s):
        self.source = s
        self.val = iter(s.value)
    def __next__(self):
        return next(self.val)

r = iter(MyRepeater([1,2,3,4,5]))
print(next(r))
print(next(r))
print(next(r))

class MyRepeator1:
    def __init__(self,val):
        self.value = val
        self.max = len(val)
        self.idx = 0
    def __iter__(self):
        print("Iterator func called")
        return self
    def __next__(self):
        if self.idx >= self.max:
            raise StopIteration
        ret =  "next func called "+str(self.value[self.idx])
        self.idx += 1
        return ret

r = MyRepeator1([1,2,3,4,5])

for i in r:
    print("myrepeater1",i)


class Fibonacci:
    def __init__(self,range):
        self.no1 = 1
        self.no2 = 1
        self.range = range
        self.cnt = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.cnt >= self.range:
            raise StopIteration
        self.no1,self.no2,sum = self.no1+self.no2,self.no1,self.no2
        self.cnt +=1
        return sum


fib = Fibonacci(5)
for i in fib:
    print(i)

class QSequence:
    def __init__(self,s):
        self.s = s[:]
    def __iter__(self):
        return self
    def __next__(self):
        try:
            q = self.s[-self.s[-1]] + self.s[-self.s[-2]]
            self.s.append(q)
            return q
        except IndexError:
            raise StopIteration

qseq = QSequence([1,1])
for i in range(5):
    print(next(qseq))


def gen_func():     # Generator function
    print("Init")
    for i in range(20):
        yield i

print(gen_func())
g = gen_func()
print(next(g))
print(next(g))
print(next(g))

def recipeData():
    f = open("recipeData.csv")
    for l in f:
        yield l
    f.close()

data = recipeData()
print(next(data))
print(next(data))
print(next(data))

line = (l for l in open("recipeData.csv"))

l = (i.split(",") for i in line)
beercnts = {}
header = next(l) # store the header which is in first line of the file
beerdicts = (dict(zip(header,i)) for i in l)
beercnts = {}
#for beer in beerdicts:

while True:
    beer = next(beerdicts)
    if beer["Style"] not in beercnts:
        beercnts[beer["Style"]] = 1
    else:
        beercnts[beer["Style"]] += 1
    if beercnts[beer["Style"]] == 2:
        break
print(beercnts)
print("d",next(beerdicts))

lc = [n**2 for n in [1,2,3,4]]  # list compreension
ge = (n**2 for n in [1,2,3,4])  # generator exp
print(lc)
print(ge)
print(next(ge))
print(next(ge))
print(next(ge))
print(next(ge))

