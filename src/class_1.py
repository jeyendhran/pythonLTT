print("Hello World")
a = 1
b = 3.4576458474
z = "hai"
aa = a
print(aa,id(a),id(aa))
aa = aa+2
print(a,aa,id(a),id(aa))
""" This will check data type
of variables"""
if type(a) is int:
    print("a is int type")
if type(b) is float:
    print("b is float type")

if a>b:
    print("a",a,type(a))
else:
    print("b",b,type(b))


print("type of z is",type(z))

print("Hai\nHow r u")
print(r"Hai\nHow r u") # prints raw text
print("'Hai'",'"Hai"','''"How's that", he said''') # various ways to define a string


a,b = 10,5
print(id(a),id(b))
b,a = a,b
print(id(a),id(b))

print("************ Sequence data types************")
lis = [1,2,3,'6',"Hai",[2,3],("hai",7.4)]
print(lis,type(lis))
print("1st ele",lis[0],"and last ele",lis[-1])
lis[-2].append(6)
print(lis)
print(2 in lis,6 in lis)

tup = (2,3,4,'5',"hai",(3,4.5),[3,5])
print(tup,type(tup),id(tup))
print("1st ele",tup[0],"and last ele",tup[-1])

tup[-1].append(6) # able to change the value of a list in tuple
print("Tuple after updation",tup,id(tup))

# slicing operation
print(tup[1:-3])
print(tup[-3:]) # prints last 3 elements
print(tup[:3]) # prints first 3 elements
print(tup[(len(tup)//2)]) # prints middle element
print(tup[:]) # prints entire tuple

#Advanced slicing
alp = [0,1,2,3,4,5,6,7,8,9,10,11,12]
print(alp[0:12:2]) # start:end:step(optional default 1)
print(alp[10:0]) # returns empty list
print(alp[10:0:-1])
print(alp[0:10])
print(alp[0::2])
print("reverse the list",alp[::-1]) # reverse the list

print("-----------Deep and shallow copy in list--------------")
lis1 = lis
print(id(lis),id(lis1)) # creates shallow copy, change in one with affect another
lis2 = lis[:]
print(id(lis),id(lis2)) # creates deep copy, both are independent , changes in one will not reflect in another

print("-----------Deep and shallow copy not work in tuple-----------")
tup1 = tup
print(id(tup),id(tup1))
tup2 = tup[:]
print(id(tup),id(tup2))

#List operations
l1 = [1,2,3]+[4,5,6]
print(l1,id(l1))
l2 = l1*2
print(l2)
l1.append(7)
print("Appending at last index",l1)
l1.extend([8,9]) # extends needs iterator object as a param
print("List after extending",l1)
l1.extend((10,11)) # extends needs iterator object as a param
print("List after extending",l1)
l1.extend({2,3,4}) # extends needs iterator object as a param
print("List after extending",l1)
l1.insert(2,2.5)
print("Insert data at specified index and changes the index of the other elements",l1)
print(l1.index(2)) # returns 1st occurrence of the element
print(l1.index(2,3)) # returns the occurrence of the element from the specified index
print(l1.index(2,3,14)) # index(element,start,stop)
print(l1.count(2)) # returns no of occurrence of the element in the list
l1.remove(2) # removes 1st occurrence of the element
print(l1)
print(l1.pop()) # removes the last element of the list
print(l1)
print(l1.pop(10)) # removes the indexed element from the list
print(l1)
l1.reverse()
print(l1)
l1.sort()
print(l1)

tup = (9)
print(type(tup))
tup = 9,
print(type(tup))
tup = (9,)
print(type(tup))

print("********** Mapping data type *************")
dic = {"name": "Jeyendhran", 'age': 23,'location':["Chennai","Dharapuram"]}
print(dic,dic['name'],dic['age'])
print(dic.items(),dic.values(),dic.keys())
keys = list(dic.values())
print(type(keys),type(keys[0]),keys[0])
#dic.pop('age')
print('age' in dic.keys(),'name' in dic,'Jeyendhran' in dic.values())
print(dic)
for i in dic.keys():
    print(i)
for i in dic.values():
    print(i)
for i in dic.items():
    print(i)
for i,j in dic.items():
    print(i,"has the value",j)

print("*****Sets operation******")
l1 = [2,3,4,4,5,6,7,7,8]
print(l1)
set1 = set(l1)
print("set1",set1)
set2 = {2,3,4,5,6,7,8,9,10,11,12,13}
print("set2",set2)
print(set2.intersection(set1),set1.intersection(set2))
print(set1.union(set2),set2.union(set1))
print(set2.isdisjoint(set1),set1.issubset(set2))

print(list(range(10)),list(range(0,21,2)),list(enumerate(l1)))


a = [20,2,3,4,5]
b = a
c = [20,2,3,4,5]
print(a == b, a is b, b == c, b is c)

#time = int(input("Enter the hour"))
#print((time%12) if time > 12 else time,"AM" if time < 12 else "PM")

'''while True:
    wage = int(input("Enter your wage:"))
     print("High" if wage>2500 else ("Moderate" if wage>1500 else "Low")) '''

i = 0
while i<10:
    i = i + 1
    if i <= 4:
        continue
    print(i)
    if i == 6:
        break
else:
    print("Reached the end of list")

print("********* For loop **********")

for i in l1:
    print(i)

eleToFound = 2


# Program to find all occurences of a element
def getoccurence():
    print("Occurence")
    lis = [2,3,4,5,6,2,3,4,6,2,4,6]
    l = 0
    eleToFound = 2
    ind = []
    #Method 1
    while l < len(lis)-1:
        try:
            l = lis.index(eleToFound, l, len(lis) - 1)
            ind.append(l)
            l += 1
        except:
            break
    print("2 is occurenced in the indeces",ind)

#Method 2
def getoccurence1():
    l=0
    li = lis
    ind = []
    while len(ind) < lis.count(eleToFound):
        l = lis.index(eleToFound, l, len(li) - 1)
        ind.append(l)
        l += 1
    print("2 is occurenced in the indeces",ind)
    ind.reverse()
    print(ind)

    for i in ind:
        lis.pop(i)
    print(lis)

# Program to remove duplicates from the list
def getdup():
    setl = set(lis)
    new = []
    for i in lis:
        if i in setl:
            new.append(i)
            setl.remove(i)
    print(new)

# Program to get the keys using its values
def getkeys():
    dic = {"fruit":"orange","color":"orange","age":"23"}
    value = "orange"
    keys = []
    for (k,v) in dic.items():
        if v == value:
            keys.append(k)
    print(keys)