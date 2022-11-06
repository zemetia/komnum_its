import numpy as np
import matplotlib.pyplot as plt

# factorial
def fact(n):
    temp = 1
    for i in range(2, n + 1):
        temp *= i
    return temp

# calculate coefficient of y
def calculate_formula(p, n):
    temp = p
    for i in range(1, n):
        if i & 1:
            temp *= (p - i)
        else:
            temp *= (p + i)
    return temp

# driver code 
n = 5
data_x = [2, 4, 6, 8, 10]
data_y = [[0 for i in range(n)] for j in range(n)]
data_y[0][0] = 9.68
data_y[1][0] = 10.96
data_y[2][0] = 12.32
data_y[3][0] = 13.76
data_y[4][0] = 15.28

# Generating gauss forward
for i in range(1, n):
    for j in range(n - 1):
        data_y[j][i] = np.round(data_y[j + 1][i - 1] - data_y[j][i - 1], 4)
        
# display the data
for i in range(n):
    print(data_x[i], end='\t')
    for j in range(n - i):
        print(data_y[i][j], end='\t')
    print("")
    
# input the desired value
value = float(input("Enter the point : "))

# Implementing formula gauss forward
sum = data_y[int(n / 2)][0]
p = (value - data_x[int(n / 2)]) / (data_x[1] - data_x[0])

for i in range(1, n):
    sum += (calculate_formula(p, i) * data_y[int((n - i) / 2)][i]) / fact(i)

print("The value at", value, "is", round(sum, 3))