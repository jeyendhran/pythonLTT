def intersection(a,b):
    '''To find intersection of 2 dicts'''
    res={}
    keysa = set(a.keys())
    keysb = set(b.keys())
    intersect = list(keysa.intersection(keysb))
    keys =[]
    values = []
    for i in intersect:
        keys.append(i)
        values.append(list([a[i],b[i]]))
    res = dict(zip(keys,values))
    return res

def union(a,b):
    '''To find union of 2 dicts'''
    res = {}
    keysa = set(a)
    keysb = set(b)
    union = list(keysa.union(keysb))
    keys = []
    values = []
    for i in union:
        keys.append(i)
        if i in a and i in b:   # the key is in 2 dict then make the values of 2 dicts as a list
            values.append(list([a[i], b[i]]))
        elif i in a:
            values.append(a[i])
        elif i in b:
            values.append(b[i])
    res = dict(zip(keys, values))
    return res

def subtract(a,b):
    '''To find subtraction of 2 dicts'''
    res = {}
    keysa = set(a)
    keysb = set(b)
    sub = list(keysa-keysb)
    keys = []
    values = []
    for i in sub:
        keys.append(i)
        if i in a:
            values.append(a[i])
    res = dict(zip(keys, values))
    return res

def issubsetdict(a,b):
    '''To find issubset of 2 dicts'''
    keysa = set(a)
    keysb = set(b)
    res = keysa.issubset(keysb)
    return res

def symmetricdiff(a,b):
    '''To find symmetric difference of 2 dicts'''
    keysa = set(a)
    keysb = set(b)
    symdif = keysa.symmetric_difference(keysb)
    keys = []
    values = []
    for i in symdif:
        keys.append(i)
        if i in a and i in b:   # the key is in 2 dict then make the values of 2 dicts as a list
            values.append(list([a[i], b[i]]))
        elif i in a:
            values.append(a[i])
        elif i in b:
            values.append(b[i])
    res = dict(zip(keys, values))
    return res


dict1 = {'a':1,'b':2,'c':3,'d':4}
dict2 = {'b':3,'d':5,'k':12,'h':4}
print("Intersection is",intersection(dict1,dict2))
print("Union is",union(dict1,dict2))
print("Subtraction is",subtract(dict1,dict2))
print("dict1 is subset of dict2?",issubsetdict(dict1,dict2))
print("Symmetric diff",symmetricdiff(dict1,dict2))
