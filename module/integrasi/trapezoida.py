import numpy as np

class Trapezoida:
    def __init__(self, func, bottomBound:float = 1, topBound:float = 3):
        self.func = func
        self.bottomBound = bottomBound
        self.topBound = topBound
        self.data = {}
        self.generate()

    def createSetData(self, section:int) -> float:
        # num=section+1; ex: we need 5 values beetwen bottom and top bound
        # then we need 6 sequence from bottom to top (including the bottom, and not the top because endpoint=False)
        dataRange = np.linspace(self.bottomBound, self.topBound, num=section+1, endpoint=False) 
        dataRange = np.delete(dataRange, 0) #deleting index 0
        data = [self.func(i) for i in dataRange]
        
        return data

    def computeIntegration(self, section:int) -> float:
        center = sum(self.createSetData)
        result = (1/2) * (self.func(self.bottomBound) + 2*(center) + self.func(self.topBound))
        return result
    
    def computeTipCorrection(self, section:int) -> float:
        tip = (1/12) * (self.func(self.topBound) - self.func(self.bottomBound))
        return self.computeIntegration - tip

    def generate(self, section:int = 5) -> float:
        self.data = {
            "integrantion": self.computeIntegration(section),
            "tipCorrection": self.computeTipCorrection(section)
        }

        return self.data

