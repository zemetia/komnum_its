import numpy as np

class gauss_forward:
    # init 
    def __init__(self, data_x, data_y, n):
        self.x = data_x
        self.y = data_y
        self.generatingGaussForward(self.x, self.y, n)
        
    # factorial
    def fact(self, n):
        temp = 1
        for i in range(2, n + 1):
            temp *= i
        return temp

    # calculate coefficient of y
    def calculate_formula(self, p, n):
        temp = p
        for i in range(1, n):
            if i & 1:
                temp *= (p - i)
            else:
                temp *= (p + i)
        return temp
    
    def generatingGaussForward(self, data_x, data_y, n):
        # Generating gauss forward
        for i in range(1, n):
            for j in range(n - 1):
                data_y[j][i] = np.round(data_y[j + 1][i - 1] - data_y[j][i - 1], 4)
        self.displayData(data_x, data_y, n)
                
    def displayData(self, data_x, data_y, n):
        for i in range(n):
            print(data_x[i], end='\t')
            for j in range(n - i):
                print(data_y[i][j], end='\t')
            print("")
        self.implementing(data_x, data_y, n)
            
    def implementing(self, data_x, data_y, n):
        value = float(input("Enter the point : "))
        sum = data_y[int(n / 2)][0]
        p = (value - data_x[int(n / 2)]) / (data_x[1] - data_x[0])

        for i in range(1, n):
            sum += (self.calculate_formula(p, i) * data_y[int((n - i) / 2)][i]) / self.fact(i)

        print("The value at", value, "is", round(sum, 3))

# Driver code 
data_x = [2, 4, 6, 8, 10]
data_y = [[0 for i in range(len(data_x))] for j in range(len(data_x))]
data_y[0][0] = 9.68
data_y[1][0] = 10.96
data_y[2][0] = 12.32
data_y[3][0] = 13.76
data_y[4][0] = 15.28

# Call class
inum = gauss_forward(data_x, data_y, len(data_x))
