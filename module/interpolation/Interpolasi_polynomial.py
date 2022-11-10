# Import library python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class interpolation_polynomial:
    def __init__(self):
        # cek data frame
        self.inisialize()
        data = pd.DataFrame({'x' : self.data_x, 'f(x)' : self.data_y})
        #print(data)
        self.generatePolynomial(self.p, self.data_x, self.data_y, len(self.data_x))
        
    # Create Tabel
    def inisialize(self):
        self.data_x = np.array([2, 4, 6, 8, 10], float)
        self.data_y = np.array([9.68, 10.96, 12.32, 13.76, 15.28])
        self.n = len(self.data_x)
        self.p = np.zeros([self.n, self.n + 1])
        
        # this suppress the sciencetific symbol (e) and return value in normal digits
        np.set_printoptions(suppress=True)  
    
    def generatePolynomial(self, p, data_x, data_y, n):
        # firss two column of the table are filled with x and y data points
        for i in range(n):
            p[i, 0] = data_x[i]
            p[i, 1] = data_y[i]

        for i in range(2, n + 1):
            for j in range(n + 1 - i):
                p[j, i] = np.round((p[j + 1, i - 1] - p[j,  i - 1]) / (data_x[j + i - 1] - data_x[j]), 3)
        
        self.printTemp(p, data_x, n)
        self.calculate(self.b, data_x, n)
    
    def printTemp(self, p, data_x, n):
        self.b = p[0][1:]
        print("b = ", self.b)
        print("x = ", data_x)
    
    def calculate(self, b, data_x, n):
        # input the desired value
        value = float(input("Enter the point : "))
        listt = [] # list where we will append the values of product terms
        temp = 1

        for i in range(len(data_x)):
            temp *= (value - data_x[i])     
            listt.append(np.round(temp, 4))
            
        print("The list of product elements : ", listt)
        self.resultPolynomial(b, listt)

    def resultPolynomial(self, b, listt):
        # Creating a general function
        func = b[0]
        for k in range(1, len(b)):
            func += b[k] * listt[k - 1]
            
        print("The value of polynomial: ", "{0:.3f}".format(func))
                
                
inum = interpolation_polynomial()