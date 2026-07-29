class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        '''
        for every num in nums, we look at every other nums (to the right) and recurse with the number

        and at that point, we also append the list with the number, and without
        '''
        ret = []

        def recurse(currentPath, currIndex):
            nonlocal ret

            print(f"currentPath is {currentPath}, currIndex is {currIndex}")

            # if the recursion gets past the end of list
            if currIndex == len(nums):
                ret.append(currentPath)
                return 
            
            # with and without, make sure to make new lists
            
            nextPath = currentPath[:]
            recurse(nextPath, currIndex + 1)

            nextPath = currentPath[:]
            nextPath.append(nums[currIndex])
            recurse(nextPath, currIndex + 1)
        
        recurse([], 0)

        print(ret)
        return ret


