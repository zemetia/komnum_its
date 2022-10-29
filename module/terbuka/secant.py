class Secant:
    def __init__(self, func, prev_point:float = 0, cur_point:float = 1):
        self.func = func
        self.prev_point = prev_point
        self.cur_point = cur_point
        self.data = []
        self.generate()
    
    def compute_next(self, prev_point, cur_point):
        next_point = cur_point - (self.func(cur_point) * (prev_point - cur_point))/(self.func(prev_point) - self.func(cur_point))
        return {
            "prev_point": prev_point,
            "cur_point": cur_point,
            "f_prev_point": self.func(prev_point),
            "f_cur_point": self.func(cur_point),
            "next_point": next_point
        }
    
    def get_next_point(self, data: dict):
        return (
            data["cur_point"],
            data["next_point"]
        )

    def generate(self, iteration: int = 5):
        self.data.append(self.compute_next(self.prev_point, self.cur_point))
        for i in range(iteration):
            prev_point, cur_point = self.get_next_point(self.data[i])
            self.data.append(self.compute_next(prev_point, cur_point))