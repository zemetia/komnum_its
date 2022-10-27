cek = lambda x: 0 if not x else x/abs(x)

class Bolzano:
    def __init__(self, func:function, bottomBound:float = 1, topBound:float = 3):
        self.func = func
        self.bottomBound = bottomBound
        self.topBound = topBound
        self.data = []
        self.generate()

    def computeNext(self, bottom, top):
        next = bottom + (top - bottom) / 2
        return { "bottomBound": bottom, "topBound": top, "nextBound": next }

    def computeFunction(self, data: dict):
        new_data = {}
        for key, val in data.items():
            new_data[key] = self.func(val)
        return new_data

    def setNextBound(self, data: dict):
        f_data = self.computeFunction(data)
            
        return (
            data['nextBound'] if cek(f_data['bottomBound']) == cek(f_data['nextBound']) else data['bottomBound'],
            data['nextBound'] if cek(f_data['topBound']) == cek(f_data['nextBound']) else data['topBound']
        )
    
    def generate(self, iteration:int = 5):
        self.data = []

        self.data.append(self.computeNext(self.bottomBound, self.topBound))
        for i in range(iteration):
            bottom, top = self.setNextBound(self.data[i])
            self.data.append(self.computeNext(bottom, top))

    def showTable(self):
        pass