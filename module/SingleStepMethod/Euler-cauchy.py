import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')

#Define parameters -> Single step Method
def f(x, y):
    return ((y - x) / (y + x))
h = 0.1 # Step size
x = np.arange(0, 0.5 + h, h) # Grid 
y0 = 2 # initial condition

# Explicit Euler Method with initialize the method
y = np.zeros(len(x))
y[0] = y0

for i in range(0, len(x) - 1) :
    y[i + 1] = y[i] + h*f(x[i], y[i])
    print('iter : ', i + 1, ' | ', 'approximate : ', y[i + 1])
    
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'r--', label='Approximate')
plt.plot(x, -((y - x) / (y + x)), 'g', label='Exact')
plt.title('Methode Euler Cauchy')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend(loc='lower right')
plt.show()