a = [1,2,3,4,5,6,7,8]
for i in a:
    if i%2 == 0 and a.index(i)%2 != 0:
        for j in a:
            if a.index(j)%2 == 0 and j%2 != 0:
                temp = j
                j = i
                i = temp
                a[a.index(j)] = i
                a[a.index(i)] = j

# print(a)

import datetime

def getrandom(end):
    l = []
    d = int(datetime.datetime.now().microsecond)
    d = d%end
    return d

def getrandom1(start,end):
    l = []
    d = getrandom(end-start)
    d = d + start
    l.append(d)
    return l


#print(getrandom1(5,7))


def getkey(dic, keys=[], values=[]):
    for k,v in dic.items():
        keys.append(k)
        if type(v) is dict:
            getkey(v)
        else:
            values.append(v)
    return [keys, values]

dic = {'a':{'b':{'c':{'d':'e'}}}}
print(getkey(dic))



l = [7,7,4,56,2,76,2,7,4,7]
l.sort()
print("Largest element in list",l[-1],"and second largest element is",l[-2])
