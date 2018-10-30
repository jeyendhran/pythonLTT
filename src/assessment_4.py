
def getmatrix(elementList,matrixdimen):
    '''To get the list as a matrix based on matrixdimension'''
    matrix = []
    row = matrixdimen[0]
    col = matrixdimen[1]
    start = 0
    end = col
    # if length of list is matched with matrixdimen then proceed
    if row*col == len(elementList):
        for i in range(0,row):
            # slicing each row based on column element count
            eachrow = elementList[start:end]
            # to get next row
            start += col
            end += col
            matrix.append(eachrow)
    else:
        return "Invalid input"

    return matrix


mylist = getmatrix([1,2,3,4,5,6,7,8,9],(3,3))
print(mylist)