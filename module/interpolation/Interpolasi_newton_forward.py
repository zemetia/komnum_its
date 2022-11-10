import numpy as np

class newton_forward:
    # init
    def __init__(self, data_x, data_y, n):
        self.x = data_x
        self.y = data_y
        self.generatingNewtonForward(self.x, self.y, n)
        
    # factorial
    def fact(self, n):
        temp = 1
        for i in range(2, n + 1):
            temp *= i
        return temp

    # calculate u mentioned in the formula
    def calculate_formula(self, u, n):
        temp = u
        for i in range(1, n):
            temp *= (u - i)
        return temp
    
    # calculating newton forward difference
    def generatingNewtonForward(self, data_x, data_y, n):
        for i in range(1, n):
            for j in range(n - i):
                data_y[j][i] = np.round(data_y[j + 1][i - 1] - data_y[j][i - 1], 4)
        self.displayData(data_x, data_y, n)
    
    # Displaying the forward difference table
    def displayData(self, data_x, data_y, n):
        for i in range(n):
            print(data_x[i], end='\t')
            for j in range(n - i):
                print(data_y[i][j], end='\t')
            print("")
        self.implementation(data_x, data_y, n)
    
    def implementation(self, data_x, data_y, n):
        # input the desired value
        value = float(input("Enter the point : "))

        # initializing u and sum
        sum = data_y[0][0]
        u = (value - data_x[0]) / (data_x[1] - data_x[0])
        for i in range(1, n):
            sum += (self.calculate_formula(u, i) * data_y[0][i]) / self.fact(i)
            
        print("The value at", value, "is", round(sum, 3))
        

# driver code
data_x = [2, 4, 6, 8, 10]
data_y = [[0 for i in range(len(data_x))] for j in range(len(data_x))]
data_y[0][0] = 9.68
data_y[1][0] = 10.96
data_y[2][0] = 12.32
data_y[3][0] = 13.76
data_y[4][0] = 15.28

inum = newton_forward(data_x, data_y, len(data_x))
