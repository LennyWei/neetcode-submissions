class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        keep a variable for the sum of the negatives within the window, 
        if that gets above the left pointer, we move the 
        
        [8, -20, 1, -10, 900]

        what the new greedy rule?
        if sum is <= 0, move left pointer?
        '''

        # main algo
        totalVal = 0
        ret = nums[0]
        right = 0

        for right in range(len(nums)):

            val = nums[right]
            totalVal += val
            
            if totalVal <= 0:
                totalVal = 0
                
            if totalVal > ret:
                ret = totalVal
        
        if max(nums) < 0:
            return max(nums)

        return ret



