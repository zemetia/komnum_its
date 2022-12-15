import numpy as np

class bessel_method:
    def __init__(self):
        self.inisialize()
        self.generateBesselMethod(self.data_x, self.data_y, len(self.data_x))
        self.tempOfSum(self.data_y, len(self.data_x))
        
    def inisialize(self):
        # Driver code
        self.data_x = [2, 4, 6, 8, 10]
        self.data_y = [[0 for i in range(len(self.data_x))] for j in range(len(self.data_x))]
        self.data_y[0][0] = 9.68
        self.data_y[1][0] = 10.96
        self.data_y[2][0] = 12.32
        self.data_y[3][0] = 13.76
        self.data_y[4][0] = 15.28
        
    # factorial
    def fact(self, n):
        temp = 1
        for i in range(2, n + 1):
            temp *= i
        return temp

    # calculate formula stirling and bessel's
    def calculate_formula(self, u, n):
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
    
    def generateBesselMethod(self, data_x, data_y, n):
        # calculate table
        for i in range(1, n):
            for j in range(n - i):
                data_y[j][i] = np.round(data_y[j + 1][i - 1] - data_y[j][i - 1], 4)
        
        self.displayData(data_x, data_y, n)
    
    def displayData(self, data_x, data_y, n):
        # Display a table
        for i in range(n):
            print(data_x[i], end='\t')
            for j in range(n - i):
                print(data_y[j][i], '\t', end=" ")
            print("") 
            
    def tempOfSum(self, data_y, n):
        up = int(n / 2 + 1)
        mid = int(n / 2)
        sum = (data_y[up][0] + data_y[mid][0]) / 2
        self.implementation(sum, self.data_x, self.data_y, len(self.data_x))

    def implementation(self, sum, data_x, data_y, n):
        # input the desired value
        value = float(input("Enter the point : "))
        # k for origin
        k = (int(n / 2) if n & 1 else int(n / 2 - 1))

        u = (value - data_x[k]) / (data_x[1] - data_x[0])

        for i in range(1, n):
            if n & 1:
                sum += ((u - 0.5) * (self.calculate_formula(u, i - 1) * data_y[k][i]) / self.fact(i))
            else:
                sum += (self.calculate_formula(u, i) * (data_y[k][i] + data_y[k - 1][i]) / (2 * self.fact(i)))
                k -= 1

        print("The value at", value, "is", round(sum, 3))

bessel_method()