#Library Initialization
import numpy as np
from numpy import linalg as LA

#Variables Initialization
# Input Matrix
A = np.array([
              [5, 4, 3, 4],
              [5, 4, 3, 4],
             [7, 6, 3, 2],
             [8, 3, 9, 10],
            ])

#Number of Principal Components

while True:
  try:
    k = int(input("Please enter the number of principal components needed: "))
    break
  except ValueError:
    print("Oops! Wrong Value Entered")

#Define the shape of matrix
dimensions = np.shape(A)
rows,columns = dimensions

print("Input Matrix: ",A)
print("Number of Principal Components: ", k)
print("Rows:", rows)
print("Columns:", columns)

while k > columns:
  try:
    raise TypeError('Bad entry')
  except Exception as e:
    e.add_note("Value of k is larger than excepted")
    raise

# Matrix Standardization Step
mean_A = np.mean(A, axis=0)
std_A = np.std(A, axis=0)
standard_A = (A - mean_A)/std_A

print("Mean of Matrix A is : ",mean_A)
print("SD of Matrix A is : ",std_A)
print("Standardized Matrix A is : ",standard_A)

# Identify the covariance matrix
Covariance_A = np.cov(standard_A, rowvar=False)

print("Covariance of Standardized Matrix is : ",Covariance_A)

#Identify eigen value & eigen vector of matrix

eigen_val , eigen_vec = LA.eig(Covariance_A)
#print(eigen_vec)
eigen_sum_work = np.sum(eigen_vec, axis=0)
#eigen_sorted = np.sort(eigen_sum,axis=0)

eigen_sum = eigen_sum_work.tolist()
eigen_sorted = eigen_sum_work.tolist()
eigen_sorted.sort(reverse = True)
print("Eigen Matrix is : ",eigen_vec)
print("Eigen Sum List is : ",eigen_sum)
print("Eigen Sorted Listed is : ",eigen_sorted)

#type(eigen_sorted)

# Retrieve Principal component list from the matrix
PCA_List = []
for i in range(k):
  for j in range(len(eigen_sorted)):
    if eigen_sum[j]==eigen_sorted[i]:
      #print(i,j)
      PCA_List.append(j)
      break

PCA_List

# Retrieve Principal component matrix

PCA_Matrix = []
for elem in A:
  row = []
  for i in PCA_List:
    row.append(elem[i])
  PCA_Matrix.append(row)

PCA_Matrix