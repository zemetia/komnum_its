import numpy as np

# factorial
def fact(n):
    temp = 1
    for i in range(2, n + 1):
        temp *= i
    return temp

# calculate u mentioned in the formula
def calculate_formula(u, n):
    temp = u
    for i in range(1, n):
        temp *= (u - i)
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

# calculating the forward difference
for i in range(1, n):
    for j in range(n - i):
        data_y[j][i] = np.round(data_y[j + 1][i - 1] - data_y[j][i - 1], 4)
        
# Displaying the forward difference table
for i in range(n):
    print(data_x[i], end='\t')
    for j in range(n - i):
        print(data_y[i][j], end='\t')
    print("")
    
# input the desired value
value = float(input("Enter the point : "))

# initializing u and sum
sum = data_y[0][0]
u = (value - data_x[0]) / (data_x[1] - data_x[0])
for i in range(1, n):
    sum += (calculate_formula(u, i) * data_y[0][i]) / fact(i)
    
print("The value at", value, "is", round(sum, 3))