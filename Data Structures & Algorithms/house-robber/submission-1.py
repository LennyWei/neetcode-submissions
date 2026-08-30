class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        houses:  1 , 1 , 3 , 3

        we need to find a permutation where max value, but no choices are adjacent
        brute force, you can go through every permutation and choice 2^n time complexity  


        kinda similar to previous problem, except max, and the choosing position is a bit different (we're choosing the two after the one after the house)
        '''
        l = len(nums) # need to grab length before i extend

        nums += [0]

        for i in range(l-3,  -1, -1):

            nums[i] = max(nums[i+2], nums[i+3]) + nums[i]
        
        print(nums)

        return max(nums[0], nums[1])