import numpy as np
from functools import reduce
from math import sin

class Hermite:
    def __init__( self, data: dict ) -> None:
        self.verifDataLength(data)

    def verifDataLength(self, data: dict) -> None:
        try:
            if len(data['x']) == len(data['fx']):
                self.data = data
                self.data_length = len(data['x'])
        except:
            print("Data format is unmatch")

    def multiply(data: list) -> float:
        return reduce(lambda x, y: x * y, data)

    def getValueMinDatas(self, value: float) -> list:
        return [(sin(value - data)) for data in self.data['x']]

    def computeAtIndex(self, upper_data: list, bottom_data: list, fx: float) -> float:
        upper = Hermite.multiply(upper_data)
        bottom = Hermite.multiply(bottom_data)
        return (upper/bottom) * fx

    def interpolation(self, value: float) -> float:
        vmd = self.getValueMinDatas(value)
        sum = 0

        for index in range(self.data_length):
            temp_vmd = vmd.copy()
            temp_vmd.pop(index)
            bottom = self.getValueMinDatas(self.data['x'][index])
            bottom.pop(index)

            sum += self.computeAtIndex(temp_vmd, bottom, self.data['fx'][index])

        return np.round(sum, 5)


contoh_data = {
    'x': [0.4, 0.5, 0.7, 0.8],
    'fx': [0.0977, 0.0088, -0.1577, -0.2192]
}

interpolasi = Hermite(contoh_data)
print(interpolasi.interpolation(0.6))   