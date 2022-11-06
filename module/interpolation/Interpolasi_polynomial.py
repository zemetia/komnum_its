# Import library python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.interpolate as interpolate

# create tabel 
data_x = np.array([2, 4, 6, 8, 10], float)
data_y = np.array([9.68, 10.96, 12.32, 13.76, 15.28])
n = len(data_x)

# creating a tree table 
p = np.zeros([n, n + 1])

# input the desired value
value = float(input("Enter the point : "))

# cek data frame
data = pd.DataFrame({'x' : data_x, 'f(x)' : data_y})
#print(data)


# firss two column of the table are filled with x and y data points
for i in range(n):
    p[i, 0] = data_x[i]
    p[i, 1] = data_y[i]

for i in range(2, n + 1):
    for j in range(n + 1 - i):
        p[j, i] = (p[j + 1, i - 1] - p[j,  i - 1]) / (data_x[j + i - 1] - data_x[j])

# this suppress the sciencetific symbol (e) and return value in normal digits
np.set_printoptions(suppress=True)  

b = p[0][1:]
print("b = ", b)
print("x = ", data_x)

listt = [] # list where we will append the values of product terms

temp = 1

for i in range(len(data_x)):
    temp *= (value - data_x[i])
    listt.append(temp)
    
print("The list of product elements : ", listt)

# Creating a general function
func = b[0]
for k in range(1, len(b)):
    func += b[k] * listt[k - 1]
    
print("The value of polynomial: ", "{0:.3f}".format(func))