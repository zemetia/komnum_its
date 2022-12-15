class RungeKuttaOrde2:
    def __init__(self, func_x_y, x_0, y_0, x_n, dx, a1, a2, p):
        self.func_x_y = func_x_y
        self.cur_x = x_0
        self.cur_y = y_0
        self.target_x = x_n
        self.dx = dx
        self.a1 = a1
        self.a2 = a2
        self.p = p
        self.data = []
        self.generate()

    def compute_next(self):
        if self.target_x - self.cur_x > 1e-6:
            k1 = self.func_x_y(self.cur_x, self.cur_y)
            k2 = self.func_x_y(
                            self.cur_x + (self.p * self.dx), 
                            self.cur_y + self.p * self.dx * k1
                            )
            prev_x = self.cur_x
            prev_y = self.cur_y
            self.cur_x = self.cur_x + self.dx
            self.cur_y = self.cur_y + (self.a1 * k1 + self.a2 * k2) * self.dx

            return {
                'x_i': prev_x,
                'y_i': prev_y,
                'k1': k1,
                'k2': k2,
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
            'k1': '',
            'k2': '',
            'y_(i+1)': ''
        })

import pandas as pd

func = lambda x, y: y * (x ** 2) - y
# RungeKuttaOrde2(fungsi, x0, y0, x akhir, h atau delta x, a1, a2, p1 atau q11)
rk = RungeKuttaOrde2(func, 0, 1, 2, 0.25, (1/3), (2/3), 0.75) #Runge Kutta Orde 2 Raltson
df = pd.DataFrame(rk.data)
print(df)