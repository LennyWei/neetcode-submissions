class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ''' 
        recurse, passing through a currentSum (we can use a currentPath global list instead of passing 
        as parameters)
        
        stop case is when sum >= target
        '''

        ret = []
        currentPath = []

        def recurse(currentSum, startIndex):
            nonlocal ret
            nonlocal currentPath

            if currentSum == target:
                # do i pop currentPath?
                ret.append(currentPath[:])
                return
            elif currentSum > target:
                return
            
            # how do i make sure the range is handled right?
            for i in range(startIndex, len(nums)):
                currentPath.append(nums[i])
                recurse(currentSum + nums[i], i)
                currentPath.pop()
        
        recurse(0, 0)

        return ret
