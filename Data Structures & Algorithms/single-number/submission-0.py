class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ret = 0

        for i in nums:
            ret = ret ^ i
        return ret
        