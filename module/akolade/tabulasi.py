class Tabulasi:
    def __init__(self, func, firstBound: float = 0, triggerPerIteration: int = 11):
        self.func = func
        self.firstBound = firstBound
        self.triggerPerIteration = triggerPerIteration
        self.data = []
        self.generate()

    def check(x): 
        return 0 if not x else x/abs(x)

    def computeNext(self, first: float, iteration: int, trigger: int):
        tempFunc = Tabulasi.check(self.func(first))
        plus = 1/iteration
        next = first

        while tempFunc == Tabulasi.check(self.func(next)):
            next += plus
            trigger -= 1
            if not trigger: break
        
        next -= plus

        return { 
            "firstBound": first,
            "f_firstBound": self.func(first),
            "nextBound": next, 
            "f_nextBound": self.func(next) 
            }

    def getNextBound(self, data: dict):
        return data['nextBound']        
    
    def generate(self, iteration:int = 5):
        self.data = []

        tenHolder = 1
        self.data.append(self.computeNext(self.firstBound, tenHolder, self.triggerPerIteration))
        
        for i in range(iteration):
            tenHolder *= 10
            next = self.getNextBound(self.data[i])
            self.data.append(self.computeNext(next, tenHolder, self.triggerPerIteration))
