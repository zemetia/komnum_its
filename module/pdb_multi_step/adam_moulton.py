from adam import Adam

class AdamMoulton(Adam):
    def __init__(self, function) -> None:
        super().__init__(function)
        self.list2 = [9, 1, -5, 19]

    def getAllFuncDataCorrector(self, next, prediction):
        f_result = []
        for i in range(4, 1, -1):
            f_result.append((self.function(self.data['x'][i-1], self.data['y'][i-1]) * self.list2[i-1]))
        f_result.append(self.function(next, prediction) * self.list2[0])
        return f_result

    def computeNextX(data):
        sumOfDiff = 0
        for i in range(3):
            sumOfDiff += data['x'][i+1] - data['x'][i]
        return sumOfDiff/3

    def compute(self, data: dict) -> float:
        prediction = self.predict(data)
        next = AdamMoulton.computeNextX(data) + self.data['x'][-1]
        result = sum(self.getAllFuncDataCorrector(next, prediction))
        yn = self.data['y'][-1]
        h = self.data['x'][1] - self.data['x'][0]

        return yn + (h/24) * result


fungsi = lambda x, y: x + y
contoh_data = {
    'x': [0.2, 0.3, 0.4, 0.5],
    'y': [1.2428, 1.3997, 1.5839, 1.7974]
}

method = AdamMoulton(fungsi)
print(method.compute(contoh_data))