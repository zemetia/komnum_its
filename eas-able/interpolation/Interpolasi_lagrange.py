from functools import reduce

class Lagrange:
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
        return reduce(lambda x, y: x*y, data)

    def getValueMinDatas(self, value: float) -> list:
        return [(value - data) for data in self.data['x']]

    def computeAtIndex(self, upper_data: list, bottom_data: list, fx: float) -> float:
        upper = Lagrange.multiply(upper_data)
        bottom = Lagrange.multiply(bottom_data)
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

        return sum


contoh_data = {
    'x': [361, 367, 378, 387, 399],
    'fx': [154.9, 167, 191, 212.5, 244.2]
}

interpolasi = Lagrange(contoh_data)
print(interpolasi.interpolation(372))
