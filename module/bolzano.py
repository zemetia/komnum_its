cek = lambda x: 0 if not x else x/abs(x)

class Bolzano:
    def __init__(self, func, bottomBound:float = 1, topBound:float = 3):
        self.func = func
        self.bottomBound = bottomBound
        self.topBound = topBound
        self.data = []
        self.generate()

    def computeNext(self, bottom, top):
        next = bottom + (top - bottom) / 2
        return { 
            "bottomBound": bottom,
            "f_bottomBound": self.func(bottom),
            "topBound": top,
            "f_topBound": self.func(top),
            "nextBound": next, 
            "f_nextBound": self.func(next) 
            }


    def setNextBound(self, data: dict):
        return (
            data['nextBound'] if cek(data['f_bottomBound']) == cek(data['f_nextBound']) else data['bottomBound'],
            data['nextBound'] if cek(data['f_bottomBound']) != cek(data['f_nextBound']) else data['topBound']
        )
    
    def generate(self, iteration:int = 5):
        self.data = []

        self.data.append(self.computeNext(self.bottomBound, self.topBound))
        for i in range(iteration):
            bottom, top = self.setNextBound(self.data[i])
            self.data.append(self.computeNext(bottom, top))


import pandas as pd
fungsi = lambda x: x*x*x - 3*x - 1
soal1 = Bolzano(fungsi, 1, 5)
soal1.generate(10)
df = pd.DataFrame(soal1.data)
print(df)