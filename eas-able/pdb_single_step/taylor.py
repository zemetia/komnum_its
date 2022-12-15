import math

class Taylor:
    def __init__(self, func, func1, func2, x_0, y_0, x_n, dx):
        self.func = func
        self.func1 = func1
        self.func2 = func2
        self.cur_x = x_0
        self.cur_y = y_0
        self.target_x = x_n
        self.dx = dx
        self.data = []
        self.generate()

    def compute_next(self):
        if self.target_x - self.cur_x > 1e-6:
            y = []
            sum = 0

            y.append(self.cur_y)
            y.append(self.func(self.cur_x, y[0]))
            y.append(self.func1(self.cur_x, y[1]))
            y.append(self.func2(self.cur_x, y[2]))

            for i in range(4):
                sum += y[i] * (1 / math.factorial(i+1))

            prev_x = self.cur_x
            prev_y = self.cur_y
            self.cur_x = self.cur_x + self.dx
            self.cur_y = sum

            return {
                'x_i': prev_x,
                'y_i': prev_y,
                'y_data': y,
                'y_(i+1)': self.cur_y
            }
        else:
            return None

    def generate(self):
        next_data = self.compute_next()
        while(next_data is not None):
            self.data.append(next_data)
            next_data = self.compute_next()
        self.data.append({
            'x_i': self.cur_x,
            'y_i': self.cur_y,
            'y_data': [],
            'y_(i+1)': ''
        })
import pandas as pd

fy = lambda x, y: y * (x ** 2) - y
fy1 = lambda x, y: y * 2 * x - y
fy2 = lambda x, y: y

taylor = Taylor(fy, fy1, fy2, 0, 1, 2, 0.5)
df = pd.DataFrame(taylor.data)
print(df)