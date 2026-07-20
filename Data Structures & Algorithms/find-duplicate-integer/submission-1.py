class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
            After hints:

            how do we know it's dupe?
            if you head to the index and it's negative
            When you iterate through, it's okay if its negative. but when you get that val and
            have to navigate to the certain index, if it's negative, then it means you've already set that
            before, meaning this is a dupe
        '''


        for i in range(len(nums)): 
            # it could be negative
            print(f"Looking at {i} in {nums}")

            if nums[abs(nums[i]) - 1] < 0:
                return abs(nums[i])
            
            nums[abs(nums[i]) - 1] *= -1
        
        return -1



        