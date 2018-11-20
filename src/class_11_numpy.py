#Numpy module
import numpy as np

arr1 = np.array([11,-2,23.3,4,75],dtype=np.int64)
arr2 = np.array([-2,4,9,-30,4])
print(arr1,type(arr1),arr1.dtype)
if type(arr1) is np.ndarray:
    print("yes")
if arr1.dtype == np.int64:
    print("int 64 type")

arr3 = np.array([[15,12,-1,4],[-17,8,3,4],[4,5,-9,2]])
print(arr3)
print("Size of arr is",arr3.size,"and its shape is",arr3.shape)
print("Second row is",arr3[1])
print("First column is",arr3[:,0])
print(arr3[1][2],arr3[1,2])
print(arr3[0][0:2],arr3[0,0:2])

#normal array using range
rangearr = np.arange(0,10,2)
print(rangearr)

linearspacearr = np.linspace(1,20,40)
print(linearspacearr)

#logspace = np.logspace(0,10,20,)

# dia = np.diag([1,2,3,4]) #diagonal matrix
# print("Diagonal matrix",dia)
#
print(np.zeros(5),np.ones([3,4],dtype=int),np.zeros(5,dtype=np.int64))
#
# print(arr1*2)

x,y = np.mgrid[1:7,10:20]
print(x)
print(y)

print("Random array of size(3,4)",np.random.rand(3,4))

print(arr1,"\n",arr2,"\n")
print("Sorted array",np.sort(arr1))
print("Index of original array after sorting",np.argsort(arr1))
print("Another way of sorting",arr1[np.argsort(arr1)])
print("Sum of elements",arr1.sum())
print("Mean of elements",arr1.mean())
print("standard deviation of elements",arr1.std())
print("Max of elements",arr1.max())
print("Min of elements",arr1.min())
print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1/arr2)

myarr = np.arange(20,100)
index_arr = [3,6,20,70,4]
print(myarr[index_arr])
div_by_3 = myarr%3 == 0
print(myarr[div_by_3])
print(div_by_3.all())
print(div_by_3.any())
print(myarr[div_by_3.nonzero()])

print(np.arange(10,20).reshape(5,2)) # reshapes the array dimension

arr = np.array([[3,2],[6,4]])
#print(np.linalg.inv(arr)) # raise Exception because Singular matrix
arr = np.array([[3,2],[6,2]])
print("tranpose of matrix",np.transpose(arr))
print("Another way to get tranpose of matrix",arr.T)

print(np.eye(3))

a = np.array([[1,2],[3,4]])
m = np.mat(a)
print(a[0],m[0])
print("Array multiplication",a*a,)
print("Matrix multiplication",m*m,"and",m.dot(m))
print(a.T)
print(m.T)
#print(a.I) # ndarray has no such attribute to inverse
#m = np.matrix(a)
print(m.I) # inverse of matrix