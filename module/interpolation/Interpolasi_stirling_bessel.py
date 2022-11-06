import numpy as np

# factorial
def fact(n):
    temp = 1
    for i in range(2, n + 1):
        temp *= i
    return temp

# calculate formula stirling and bessel's
def calculate_formula(u, n):
    if n == 0:
        return 1
    
    temp = u
    up = int(n / 2 + 1)
    mid = int(n / 2)
    for i in range(1, up):
        temp *= (u - i)
    
    for i in range(1, mid):
        temp *= (u + i)
        
    return temp

# Driver code
n = 5
data_x = [2, 4, 6, 8, 10]
data_y = [[0 for i in range(n)] for j in range(n)]
data_y[0][0] = 9.68
data_y[1][0] = 10.96
data_y[2][0] = 12.32
data_y[3][0] = 13.76
data_y[4][0] = 15.28

# calculate table
for i in range(1, n):
    for j in range(n - i):
        data_y[j][i] = np.round(data_y[j + 1][i - 1] - data_y[j][i - 1], 4)

# Display a table
for i in range(n):
    print(data_x[i], end='\t')
    for j in range(n - i):
        print(data_y[j][i], '\t', end=" ")
    print("") 

# input the desired value
value = float(input("Enter the point : "))

# initializing sum
up = int(n / 2 + 1)
mid = int(n / 2)
sum = (data_y[up][0] + data_y[mid][0]) / 2

# k for origin
k = (int(n / 2) if n & 1 else int(n / 2 - 1))

u = (value - data_x[k]) / (data_x[1] - data_x[0])

for i in range(1, n):
    if n & 1:
        sum += ((u - 0.5) * (calculate_formula(u, i - 1) * data_y[k][i]) / fact(i))
    else:
        sum += (calculate_formula(u, i) * (data_y[k][i] + data_y[k - 1][i]) / (2 * fact(i)))
        k -= 1

print("The value at", value, "is", round(sum, 3))