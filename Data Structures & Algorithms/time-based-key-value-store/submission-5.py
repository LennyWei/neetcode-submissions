class TimeMap:
    '''
    Think about brute case:

    a hashmap that stores key:[(timeStamp, value), ...]

    '''

    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append((timestamp, value))
        else:
            self.hashmap[key] = [(timestamp, value)]
        
# set calls are always increasing. 

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""

        # if timestamp 
        ls = self.hashmap[key]
        left = 0
        right = len(ls) - 1

        # if wanted time is >= the last added time, then we just return last added time
        if timestamp >= ls[right][0]:
            print("too big, returning")
            return ls[right][1]
        
        if timestamp < ls[left][0]:
            print("too small, returning")
            return ""

        # do binary search
        
        while left < right:
            m = (right + left) //2
            print(m)
            if ls[m][0] >= timestamp:
                right = m
            else:
                left = m+1
        
        
        if timestamp != ls[left][0]:
            left -= 1

        print(f"left {left} and right {right} and dict {self.hashmap}")

        return ls[left][1]
        
