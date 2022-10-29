import math

#lebih bagus jadi fungsi
class Kuadratur:
    def __init__(self):
        self.boundOne = 1/math.sqrt(3)
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
            return
        self.bottomBound = x[0]
        self.f_bottomBound = y[0]
        self.topBound = x[-1]
        self.f_topBound = y[-1]
        self.type = "datas"

    def computeIntegration(self) -> float:
        if self.checkType("none"):
            print("there is no datas/function")
            return 
            
        tpb = (self.topBound + self.bottomBound) / 2
        tmb = (self.topBound - self.bottomBound) / 2
        x0 = tpb - (tmb * self.boundOne)
        x1 = tpb + (tmb * self.boundOne)

        if self.checkType("function"): result = (self.func(x0) * tmb) + (self.func(x1) * tmb)
        elif self.checkType("datas"): result = (self.f_bottomBound * tmb) + (self.f_topBound * tmb)

        return result 

