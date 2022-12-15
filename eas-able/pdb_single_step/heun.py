class Heun:
    def __init__(self, func_x_y, x_0, y_0, x_n, dx):
        self.func_x_y = func_x_y
        self.cur_x = x_0
        self.cur_y = y_0
        self.target_x = x_n
        self.dx = dx
        self.data = []
        self.generate()

    def compute_next(self):
        if self.target_x - self.cur_x > 1e-6:
            left_slope = self.func_x_y(self.cur_x, self.cur_y)
            right_slope = self.func_x_y(
                            self.cur_x + self.dx, 
                            self.cur_y + self.dx *
                            left_slope)
            ideal_slope = (left_slope + right_slope) / 2
            dy = self.dx * ideal_slope

            prev_x = self.cur_x
            prev_y = self.cur_y
            self.cur_x = self.cur_x + self.dx
            self.cur_y = self.cur_y + dy

            return {
                'x_i': prev_x,
                'y_i': prev_y,
                'left slope': left_slope,
                'right slope': right_slope,
                'ideal slope': ideal_slope,
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
            'left slope': '',
            'right slope': '',
            'ideal slope': '',
            'y_(i+1)': ''
        })

import pandas as pd

func = lambda x, y: y * (x ** 2) - y
heun = Heun(func, 0, 1, 2, 0.25)
df = pd.DataFrame(heun.data)
print(df)