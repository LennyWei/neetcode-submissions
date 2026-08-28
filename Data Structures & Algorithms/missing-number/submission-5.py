class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        m = 0

        for i in range(len(nums)):
            s += i
            m += nums[i]
        
        s += len(nums)
        
        return s - m