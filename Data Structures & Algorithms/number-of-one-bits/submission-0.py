class Solution:
    def hammingWeight(self, n: int) -> int:
        
        res = 0

        while n:

            isRightOne = n & 1

            if isRightOne:
                res += 1
            
            n >>= 1
        
        return res