class Solution:
    def countBits(self, n: int) -> List[int]:
        

        def algo(num):

            ret = 0

            while num:
                if num & 1:
                    ret += 1
                num >>= 1
            
            return ret

        return [algo(i) for i in range(n+1)]