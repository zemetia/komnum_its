class FixedPointIteration:
    def __init__(self, func, point:float = 0):
        self.func = func
        self.point = point
        self.data = {}
        self.generate()
    
    def compute_next(self):
        return self.func(self.data["point"][-1])

    def generate(self, iteration:int = 5):
        self.data["point"] = [self.point]
        for i in range(iteration):
            self.data["point"].append(self.compute_next())
