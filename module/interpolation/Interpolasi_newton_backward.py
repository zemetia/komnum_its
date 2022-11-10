import numpy as np

class newton_backward:
    def __init__(self, data_x, data_y, n):
        self.x = data_x
        self.y = data_y
        self.generatingNewtonBackward(self.x, self.y, n)
    
    # factorial
    def fact(self, n):
        temp = 1
        for i in range(2, n + 1):
            temp *= i
        return temp

    # calculate u mentioned in the formula of backward newton-gregory
    def calculate_formula(self, u, n):
        temp = u
        for i in range(1, n):
            temp *= (u + i)
        return temp
    
    # calculating the backward difference
    def generatingNewtonBackward(self, data_x, data_y, n):
        for i in range(1, n):
            for j in range(n - 1, i - 1, -1):
                data_y[j][i] = np.round(data_y[j][i - 1] - data_y[j - 1][i - 1], 4)
        self.displayData(data_x, data_y, n)

    def displayData(self, data_x, data_y, n):
        # Displaying the forward difference table
        for i in range(n):
            print(data_x[i], end='\t')
            for j in range(i + 1):
                print(data_y[i][j], end='\t')
            print("")
        self.implementing(data_x, data_y, n)
        
    def implementing(self, data_x, data_y, n):
        # input the desired value
        value = float(input("Enter the point : "))
        
        # initializing u and sum
        sum = data_y[n - 1][0]
        u = (value - data_x[n - 1]) / (data_x[1] - data_x[0])
        for i in range(1, n):
            sum += (self.calculate_formula(u, i) * data_y[n - 1][i]) / self.fact(i)
            
        print("The value at", value, "is", round(sum, 3))
        
        
# driver code
data_x = [0.1, 0.6, 1.1, 1.6, 2.1]
data_y = [[0 for i in range(len(data_x))] for j in range(len(data_x))]
data_y[0][0] = 1.1052
data_y[1][0] = 1.8221
data_y[2][0] = 3.0042
data_y[3][0] = 4.953
data_y[4][0] = 8.1662

inum = newton_backward(data_x, data_y, len(data_x))