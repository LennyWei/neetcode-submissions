class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = capacity
        self.ls = []


    def get(self, i: int) -> int:

        return self.ls[i]


    def set(self, i: int, n: int) -> None:
        self.ls[i] = n


    def pushback(self, n: int) -> None:
        if len(self.ls) == self.size:
            self.resize()
        
        self.ls.append(n)
        


    def popback(self) -> int:
        return self.ls.pop(-1)
 

    def resize(self) -> None:
        self.size *= 2


    def getSize(self) -> int:
        return len(self.ls)
        
        
    
    def getCapacity(self) -> int:
        return self.size
