class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for index, val in enumerate(nums):
            difference = target - val

            if difference in hashmap:
                return [hashmap[difference], index]
            
            hashmap[val] = index
        
        return -1