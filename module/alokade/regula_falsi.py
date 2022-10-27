cek = lambda x: 0 if not x else x/abs(x)

class RegulaFalsi:
    def __init__(self, func, bottomBound:float = 1, topBound:float = 3):
        self.func = func
        self.bottomBound = bottomBound
        self.topBound = topBound
        self.data = []
        self.generate()

    def computeNext(self, bottom, top):
        next = top - (self.func(top) * (bottom - top))/(self.func(bottom) - self.func(top))
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
            data['nextBound'],
            data['topBound'] if data['f_nextBound'] < data['f_bottomBound'] else data['bottomBound']
        )
    
    def generate(self, iteration:int = 5):
        self.data = []

        self.data.append(self.computeNext(self.bottomBound, self.topBound))
        for i in range(iteration):
            bottom, top = self.setNextBound(self.data[i])
            self.data.append(self.computeNext(bottom, top))

