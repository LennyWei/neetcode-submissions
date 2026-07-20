class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        sort first?
        Iterate through each element, then do fast Two Sum on the remaining right numbers
        '''
        ret = set()

        nums.sort()

        for index, value in enumerate(nums[:-2]): # we wanna stop at the 3rd to last one, to leave room for two pointer
            left = index + 1
            right = len(nums) - 1

            while left < right:

                totalSum = value + nums[left] + nums[right]

                if totalSum > 0: # too much, move right 
                    right -= 1
                elif totalSum < 0: # too little, move left
                    left += 1
                else: # just right
                    ret.add((value, nums[left], nums[right])) # how to deal with dupe?
                    left += 1
        
        return list(ret)
                


            
            





