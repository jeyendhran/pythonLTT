def flattenList(mylist):
    '''To flattened multi dimensional list
    Returns flattended list'''
    flatList = []
    for i in mylist:
        if type(i) is list:
            flatList.extend(flattenList(i))
        else:
            flatList.append(i)
    return flatList

def findIndex(mylist,element):
    idx = []
    try:
        idx.append(mylist.index(element))
    except:
        for i in mylist:
            if type(i) is list:
                idex = findIndex(i, element)
                if idex == []:
                    pass
                else:
                    idx.append(mylist.index(i))
                    idx.append(idex)
    return idx

mylist = [[1,2],3,[4,[5,[6]]],7,[8]]
print("Flattened list is",flattenList(mylist))
print("Index of 5 is",findIndex(mylist,5))



