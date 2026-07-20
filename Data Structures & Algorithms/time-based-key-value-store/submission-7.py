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
        if key not in self.hashmap: # edge case if key doesn't exist
            return ""

        ls = self.hashmap[key]
        left = 0
        right = len(ls) - 1

        # if wanted time is >= the last added time, then we just return last added time
        if timestamp >= ls[right][0]:
            return ls[right][1]
        
        if timestamp < ls[left][0]:
            return ""

        # do binary search
        while left < right:
            m = (right + left) //2
            if ls[m][0] > timestamp:
                right = m
            else:
                left = m+1
        
        # if our found doesn't match the wanted timestamp, we do -1, because the left found will always be greater
        if timestamp != ls[left][0]:
            left -= 1

        return ls[left][1]
        
