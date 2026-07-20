class MinStack:

    def __init__(self):
        self.stack = []
        self.prefixMin = [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if val < self.prefixMin[-1]: # we keep track of a min prefix list 
            self.prefixMin.append(val)
        else:
            self.prefixMin.append(self.prefixMin[-1])
        

    def pop(self) -> None:
        self.stack.pop()
        self.prefixMin.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.prefixMin[-1]

        
