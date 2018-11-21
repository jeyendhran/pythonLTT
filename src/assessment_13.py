def getNewName(name):
    name = list(name)

    name = [chr(97+(ord(x)-97+13)%26) if ord(x)>=97 else chr(65+(ord(x)-65+13)%26) for x in name]
    return  "".join(name)

print(getNewName("Jeyendhran"))

a = [0,1]
[a.append(a[i]+a[i+1]) for i in range(10-len(a))]
print(a)

