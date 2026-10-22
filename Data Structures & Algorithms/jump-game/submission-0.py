class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        can do dp with bottom up recursion + memoization

        greedy?
        think it's an iterative algorithm, where at each movement you -1 power, and decide whether to either stick with your current power,
        or go to the given power at that index.
        '''


        power = nums[0]

        for i in range(1, len(nums)):

            # remove the power
            if power <= 0:
                return False
            else:
                power -= 1
            
            #decide to keep what you have or charge to the given amount

            if nums[i] > power:
                power = nums[i]
        

        return True