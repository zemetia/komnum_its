#Elimination methods
import numpy as np
M = 10

class gaussJordan:
    def __init__(self, arr, n, flag):
        self.save = []
        self.flag = flag
        self.performOperation(arr, n)
        
    def func(self, a, b, c, x):
        return ((a * pow(x, 2)) + (b * x) + c)

    #function to performOperation
    def performOperation(self, arr, n):
        i = j = k = c = 0
        print("p")
        # Perform elementary
        for i in range(n):
            if(arr[i][i] == 0):
                c = 1
                while ((i + c) < n and not arr[i + c][i]):
                    c += 1
                
                if i + c == n:
                    self.flag = 1
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
                
        return (self.checkCondition(arr, n) if self.flag == 1 else self.printMatrix(arr, n))

    # print matrix
    def printMatrix(self, arr, n):
        print("The final result of matrix : ")
        for i in range(n):
            print(*arr[i])
        self.printResult(arr, self.save, n)
            
    def printResult(self, arr, save, n):
        if self.flag == 2:
            print("Infinite solusion Exist<br>")
        elif self.flag == 3:
            print("No solution Exist<br>")
        else:
            for i in range(n):
                print("result x", (i + 1), " is ", "{0:.3f}".format(arr[i][n] / arr[i][i]), sep="")
                save.append(arr[i][n] / arr[i][i])
                
        self.printFinalMatrix(save)
                
    def checkCondition(self, arr, n):
        # flag == 2 for infinite solution
        # flag == 3 for No Solution
        self.flag = 3
        print("p")
        for i in range(n):
            sum = 0
            for j in range(n):
                sum += arr[i][j]
            if sum == a[i][j]:
                self.flag = 2
        
        return self.flag
    
    def printFinalMatrix(self, save):
        # Print result of the problem
        print()
        dik = 2.1
        print(f'The result of f({dik}) = ', self.func(save[0], save[1], save[2], dik), sep="")

        # Print Error relatif
        tempOfLinierInterpolation = 9.744
        errorRelatif = abs((self.func(save[0], save[1], save[2], dik) - tempOfLinierInterpolation) / self.func(save[0], save[1], save[2], dik)) * 100
        print("Error Relatif : {0:.3f}".format(errorRelatif))



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

# order of matrix n
inum = callGaussJordan = gaussJordan(arr, len(arr), 0)
