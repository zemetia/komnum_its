from functools import reduce

class Adam:
    def __init__( self, function) -> None:
        self.function = function
        self.list = [-9, 37, -59, 55]

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

    def multiply(data: list) -> float:
        return reduce(lambda x, y: x*y, data)

    def changeFunction(self, function):
        self.function = function

    def compute(self, data: dict) -> float:
        if(not self.verifDataLength(data)):
            return -0.01
        yn = self.data['y'][-1]
        h = self.data['x'][1] - self.data['x'][0]
        f_result = []

        for i in range(4, 0, -1):
            f_result.append((self.function(self.data['x'][i-1], self.data['y'][i-1]) * self.list[i-1]))

        result = sum(f_result)

        return yn + (h/24) * result



fungsi = lambda x, y: x + y
contoh_data = {
    'x': [0.2, 0.3, 0.4, 0.5],
    'y': [1.2428, 1.3997, 1.5839, 1.7974]
}

method = Adam(fungsi)
print(method.compute(contoh_data))