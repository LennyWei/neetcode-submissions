class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        '''
        for every num in nums, we look at every other nums (to the right) and recurse with the number

        and at that point, we also append the list with the number, and without
        '''
        ret = []
        currentPath = []

        def recurse(currIndex):
            nonlocal ret
            nonlocal currentPath

            print(f"currentPath is {currentPath}, currIndex is {currIndex}")

            # if the recursion gets past the end of list
            if currIndex == len(nums):
                ret.append(currentPath[:])
                return 
            
            # with and without, make sure to make new lists

            recurse(currIndex + 1)

            currentPath.append(nums[currIndex])
            recurse(currIndex + 1)

            currentPath.pop()
        
        recurse(0)

        print(ret)
        return ret


