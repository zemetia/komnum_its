import numpy as np

class Simpson:
    def __init__(self, func, bottomBound:float = 1, topBound:float = 3):
        self.type = "none"

    def checkType(self, type):
        return self.type == type

    def setByFunction(self, func, bottomBound:float = 1, topBound:float = 3):
        self.func = func
        self.bottomBound = bottomBound
        self.topBound = topBound
        self.type = "function"

    def setByDatas(self, x: list = [], y: list = []):
        if len(x) != len(y):
            print("the x size and y size is different")
            return
        self.bottomBound = x[0]
        self.f_bottomBound = y[0]
        self.datasY = y[1:-1] 
        self.topBound = x[-1]
        self.f_topBound = y[-1]
        self.type = "datas"

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
        if self.checkType("function"): data = self.createSetData(section)
        elif self.checkType("datas"): data = self.datasY 
        else: return

        center1 = sum(data)
        center2 = sum(data[1::2])
        if self.checkType("function"): 
            result = (self.getDeltaX() / 3)* (self.func(self.bottomBound) + (4 * center1) + (2 * center2) + self.func(self.topBound))
        elif self.checkType("datas"):
            result = (self.getDeltaX() / 3)* (self.f_bottomBound + (4 * center1) + (2 * center2) + self.f_topBound)
        return result

    def computeThreePerEight(self, section: int):
        if self.checkType("function"): data = self.createSetData(section)
        elif self.checkType("datas"): data = self.datasY 
        
        center1 = sum(data)
        center2 = sum(data[2::3])
        
        if self.checkType("function"): 
            result = (3 * self.getDeltaX() / 8) * (self.func(self.bottomBound) + (3 * center1) + (3 * center2) + self.func(self.topBound))
        elif self.checkType("datas"):
            result = (3 * self.getDeltaX() / 8) * (self.f_bottomBound + (3 * center1) + (3 * center2) + self.f_topBound)
        return result

    