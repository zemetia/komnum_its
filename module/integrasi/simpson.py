import numpy as np

class Simpson:
    def __init__(self, func, bottomBound:float = 1, topBound:float = 3):
        self.func = func
        self.bottomBound = bottomBound
        self.topBound = topBound
        self.data = {}
        self.generate()

    def getDeltaX(self):
        return abs(self.topBound - self.bottomBound)
    
    def createSetData(self, section:int) -> float:
        # num=section+1; ex: we need 5 values beetwen bottom and top bound
        # then we need 6 sequence from bottom to top (including the bottom, and not the top because endpoint=False)
        dataRange = np.linspace(self.bottomBound, self.topBound, num=section+1, endpoint=False) 
        dataRange = np.delete(dataRange, 0) #deleting index 0
        data = [self.func(i) for i in dataRange]
        
        return data

    def computeOnePerThree(self, section: int):
        data = self.createSetData(section)
        center1 = sum(data)
        center2 = sum(data[1::2])
        result = (self.getDeltaX() / 3)* (self.func(self.bottomBound) + (4 * center1) + (2 * center2) + self.func(self.topBound))
        return result

    def computeThreePerEight(self, section: int):
        data = self.createSetData(section)
        center1 = sum(data)
        center2 = sum(data[2::3])
        result = (3 * self.getDeltaX() / 8) * (self.func(self.bottomBound) + (3 * center1) + (3 * center2) + self.func(self.topBound))
        return result

    