class EulerCauchy:
    def __init__(self, func_x_y, x_0, y_0, x_n, dx: float = 0):
        self.func_x_y = func_x_y
        self.cur_x = x_0
        self.cur_y = y_0
        self.target_x = x_n
        self.data = []
        self.generate(dx=dx)

    def compute_next(self, dx):
        if self.target_x - self.cur_x > 1e-6:
            dy = self.func_x_y(self.cur_x, self.cur_y) * dx
            self.cur_x = self.cur_x + dx
            self.cur_y = self.cur_y + dy
            return {
                'x_i': self.cur_x,
                'y_i': self.cur_y
            }
        else:
            return None


    def generate(self, iteration: int = 5, dx: float = 0):
        if dx == 0:
            dx = (self.target_x - self.cur_x) / iteration
        
        self.data.append({
            'x_i': self.cur_x,
            'y_i': self.cur_y
        })

        next_data = self.compute_next(dx)
        while(next_data is not None):
            self.data.append(next_data)
            next_data = self.compute_next(dx)
