import numpy as np

str = np.array(['1','b','c',1,2])
print(str,type(str))

arr3 = np.array([[15,12,-1,4],[-17,8,3,4],[4,5,-9,2]])
print(arr3)
print("Size of arr is",arr3.size,"and its shape is",arr3.shape)
print("Second row is",arr3[[0,1],2])

rangearr = np.arange(0,10)
print(rangearr)

rangearr = np.linspace(0,10,3)
print(rangearr,rangearr.size)

logspace = np.logspace(0,10,20)
print(logspace)

dia = np.diag([1,2,3,4]) #diagonal matrix
print("Diagonal matrix\n",dia)

print(np.zeros([5,2]),np.ones([3,4],dtype=int),np.zeros(5,dtype=np.int64))


x,y = np.mgrid[1:7,10:20]
print(x)
print(y)

#print("Random array of size(3,4)\n",np.random.rand(10,4,2))

arr = np.array([2,6,3,7,1,8])
print(np.sort(arr))
print(np.argsort(arr))
print(arr[np.argsort(arr)])

arr = np.arange(0,50,5)
print(arr)
arr = np.arange(0,50)
print(arr)
idx_arr = np.arange(0,50,5)
print(arr[idx_arr])
print(arr)

# arr = np.array(['d','c','b','a','e'])
# print(type(arr),arr.dtype,arr)
# print(arr.any())
# print(arr.all())
# print(type(arr),arr.dtype,arr)

n = np.arange(0,24)
print(n.reshape(3,4,2)) # reshapes the array dimension

arr = np.array([[3,2],[6,2],[4,5]])
print("tranpose of matrix",np.transpose(arr))
print("Another way to get tranpose of matrix",arr.T)

a = np.array([[2,-2,-4],[-1,3,4],[1,-2,-3]])
m = np.mat(a)
n = np.array([[1,2,3],[3,4,5],[6,7,8]])
print(a[0],m[0])
print("Array multiplication",a*a,)
print("Matrix multiplication",m*m,"and",m.dot(m))
print(np.eye(3,3))