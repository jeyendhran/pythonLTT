from scipy.stats import pearsonr

print(pearsonr([1,2,3],[1,2,3.1])) # to get common pearson correlation coefficient

from numpy import array,mean,cov,linalg

A = array([[1,2],[3,4],[5,6]])
print(A)

M = mean(A,axis=0) # to get mean of the matrix
print(M)

C = A-M
print(C)

V = cov(C.T) # to get covarient of the matrix
print(V)


val, vec = linalg.eig(V) # to get eigen values and vectors
print(vec)
print(val)

P = vec.T.dot(C.T)
print(P)

# doing the same operation as above using predefined library
print("\nPCA method\n")
from sklearn.decomposition import PCA

A = array([[1,4],[3,2],[5,9]])

pca = PCA(2) # to get PCA instance
pca.fit(A)

print(pca.components_) # will print eigen vector
print(pca.explained_variance_) # will print eigen value

B = pca.transform(A)
print(B)