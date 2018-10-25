
def getmatrix(elementList,matrixdimen):
    matrix = []
    row = matrixdimen[0]
    col = matrixdimen[1]
    start = 0
    end = col
    if row*col == len(elementList):
        for i in range(0,row):
            r1 = elementList[start:end]
            start += col
            end += col
            matrix.append(r1)
    else:
        return "Invalid input"

    return matrix


mylist = getmatrix([1,2,3,4,5,6,7,8,9,10,11,12],(3,4))
print(mylist)