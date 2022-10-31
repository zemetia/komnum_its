import numpy as np

class Trapezoida:
    def __init__(self):
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

    def computeIntegration(self, section:int) -> float:
        if self.checkType("function"):
            center = sum(self.createSetData(section))
            f_bottom = self.func(self.bottomBound)
            f_top = self.func(self.topBound)
        elif self.checkType("datas"):
            center = sum(self.datasY)
            f_bottom = self.f_bottomBound
            f_top = self.f_topBound
        else: return

        result = (self.getDeltaX()/2) * (f_bottom + 2*(center) + f_top)

        return result
    
    def computeTipCorrection(self, section:int) -> float:
        if self.checkType("function"):
            f_bottom = self.func(self.bottomBound)
            f_top = self.func(self.topBound)
        elif self.checkType("datas"):
            f_bottom = self.f_bottomBound
            f_top = self.f_topBound
        else: return 

        tip = (self.getDeltaX()/12) * (f_top - f_bottom)
        return self.computeIntegration(section) - tip

    def getIntegration(self, section:int = 5) -> float:
        if self.checkType("none"):
            print("there is no datas/function")
            return 

        self.data = {
            "integrantion": self.computeIntegration(section),
            "tipCorrection": self.computeTipCorrection(section)
        }

        return self.data

