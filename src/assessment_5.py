def getTranspose(matrix):
    '''Function to get transpose of the matrix
    returns the transposed matrix'''
    trans_mat =[]
    col = len(matrix)
    row = len(matrix[0])
    for i in range(0,row):
        row_data=[]
        for j in range(0,col):
            row_data.append(matrix[j][i])
        trans_mat.append(row_data)
    return trans_mat

matrix = [[1,2,3],[4,5,6],[7,8,9]]
transpose_mat = getTranspose(matrix)
print("Tranpose of the martix is",transpose_mat)