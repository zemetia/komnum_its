class EulerCauchy:
    def __init__(self, func_x_y, x_0, y_0, x_n, dx: float = 0):
        self.func_x_y = func_x_y
        self.cur_x = x_0
        self.cur_y = y_0
        self.target_x = x_n
        self.data = []
        self.generate(dx=dx)

    def compute_next(self, dx):
        if self.target_x - self.cur_x + dx > 1e-6:
            dy = self.func_x_y(self.cur_x, self.cur_y) * dx
            data = {
                'x_i': self.cur_x,
                'y_i': self.cur_y,
                'dy_i': dy
            }
            self.cur_x = self.cur_x + dx
            self.cur_y = self.cur_y + dy
            return data
        else:
            return None


    def generate(self, iteration: int = 5, dx: float = 0):
        if dx == 0:
            dx = (self.target_x - self.cur_x) / iteration

        next_data = self.compute_next(dx)
        while(next_data is not None):
            self.data.append(next_data)
            next_data = self.compute_next(dx)

        

import pandas as pd

func = lambda x, y: y * (x ** 2) - y
euler = EulerCauchy(func, 0, 1, 2, 0.5)
df = pd.DataFrame(euler.data)
print(df)