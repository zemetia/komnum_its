class NewtonRaphson:
    def __init__(self, func, d_func, cur_point:float = 0):
        self.func = func
        self.d_func = d_func
        self.cur_point = cur_point
        self.data = []
        self.generate()

    def compute_next(self, cur_point):
        next_point = cur_point - (self.func(cur_point)/self.d_func(cur_point))
        return {
            "cur_point": cur_point,
            "f_cur_point": self.func(cur_point),
            "d_f_cur_point": self.d_func(cur_point),
            "next_point": next_point
        }
    
    def get_next_point(self, data: dict):
        return (
            data["next_point"]
        )

    def generate(self, iteration: int = 5):
        self.data.append(self.compute_next(self.cur_point))
        for i in range(iteration):
            cur_point = self.get_next_point(self.data[i])
            self.data.append(self.compute_next(cur_point))