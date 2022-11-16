class Milne:
    def __init__( self, function) -> None:
        self.function = function

    def verifDataLength(self, data: dict) -> bool:
        try:
            if len(data['x']) == len(data['y']):
                self.data = data
                self.data_length = len(data['x'])
                return True
            else: return False
        except:
            print("Data format is unmatch")
            return False

    def changeFunction(self, function):
        self.function = function

    def getAllFuncData(self):
        f_result = []
        for i in range(4):
            f_result.append(self.function(self.data['x'][i], self.data['y'][i]))
        return f_result

    def computeNextX(data):
        sumOfDiff = 0
        for i in range(3):
            sumOfDiff += data['x'][i+1] - data['x'][i]
        return sumOfDiff/3

    def predict(self, h):
        data = self.getAllFuncData()
        return self.data['y'][0] + (4*h/3) * (2 * data[1] - data[2] + 2 * data[3])

    def corrector(self, h, prediction):
        data = self.getAllFuncData()
        return self.data['y'][2] + (h/3) * (data[2] + 4 * data[3] + prediction)

    def compute(self, data: dict) -> float:
        if(not self.verifDataLength(data)):
            return -0.01

        h = self.data['x'][1] - self.data['x'][0]
        prediction = self.predict(h)
        f_prediction = self.function(Milne.computeNextX(data) + self.data['x'][-1], prediction)
        correction = self.corrector(h, f_prediction)

        return [prediction, correction]



fungsi = lambda x, y: x + y
contoh_data = {
    'x': [0.2, 0.3, 0.4, 0.5],
    'y': [1.2428, 1.3997, 1.5839, 1.7974]
}

method = Milne(fungsi)
print(method.compute(contoh_data))