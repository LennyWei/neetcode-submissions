class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        elif val < self.min:
            self.stack.append(val - self.min)
            self.min = val
        else:
            self.stack.append(val - self.min)
    
    def pop(self) -> None:
        if not self.stack:
            return
        
        pop = self.stack.pop()

        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        diff = self.stack[-1]
        if diff < 0:
            return self.min
        return self.min + diff

    def getMin(self) -> int:
        return self.min
