#Elimination methods
M = 10

def func(a, b, c, x):
    return ((a * pow(x, 2)) + (b * x) + c)

#function to performOperation
def performOperation(arr, n):
    i = j = k = c = flag = m  = 0

    # Perform elementary
    for i in range(n):
        if(arr[i][i] == 0):
            c = 1
            while ((i + c) < n and not arr[i + c][i]):
                c += 1
            
            if i + c == n:
                flag = 1
                break
            
            j = i
            for k in range(n + 1):
                temp = arr[j][k]
                arr[j][k] = arr[j + c][k]
                arr[j + c][k] = temp
                
        for j in range(n):
            # Excluding all i == j
            if i != j:
                #Converting matrix to reduced row
                # echelon form (diagonal matrix)
                p = arr[j][i] / arr[i][i]
                    
                k = 0
                for k in range(n + 1):
                    arr[j][k] = arr[j][k] - (arr[i][k]) * p
            
    
    return flag

# print matrix
def printMatrix(arr, n):
    print("The final result of matrix : ")
    for i in range(n):
        print(*arr[i])
        
def printResult(arr, save, n, flag):
    if flag == 2:
        print("Infinite solusion Exist<br>")
    elif flag == 3:
        print("No solution Exist<br>")
    else:
        for i in range(n):
            print("result x", (i + 1), " is ", "{0:.3f}".format(arr[i][n] / arr[i][i]), sep="")
            save.append(arr[i][n] / arr[i][i])
            
def checkCondition(arr, n, flag):
    # flag == 2 for infinite solution
    # flag == 3 for No Solution
    flag = 3
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += arr[i][j]
        if sum == a[i][j]:
            flag = 2
    
    return flag

# linier equations
"""
    4a^2 + 2b + c = 9,68
    16a^2 + 4b + c = 10,96 
    36a^2 + 6b + c = 12,32 
    
    |4    2    1| |a| = 9,68 
    |16   4    1| |b| = 10,96
    |36   6    1| |c| = 12,32
"""
arr = [[4, 2, 1, 9.68], [16, 4, 1, 10.96], [36, 6, 1, 12.32]]
save = []

# order of matrix n
n = 3
flag = 0
flag = performOperation(arr, n)

if flag == 1:
    flag = checkCondition(arr, n, flag)

#printing final matrix
printMatrix(arr, n)
print()

# print result, if no solution can print "No Solution"
printResult(arr, save, n, flag)

# Print result of the problem
print()
dik = 2.1
print(f'The result of f({dik}) = ', func(save[0], save[1], save[2], dik), sep="")

# Print Error relatif
tempOfLinierInterpolation = 9.744
errorRelatif = abs((func(save[0], save[1], save[2], dik) - tempOfLinierInterpolation) / func(save[0], save[1], save[2], dik)) * 100
print("{0:.3f}".format(errorRelatif))