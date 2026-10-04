class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        do we use tuples and sets to deal with duplicates?

        '''
        nums.sort()

        ret = []
        currentPath = []

        def dfs(prevSkipped, index):

            if index >= len(nums):
                ret.append(currentPath[:])
                return

            if nums[index] == prevSkipped: #skip
                dfs(nums[index], index + 1)
                return
            
            # include and exclude

                
            #exclude 
            dfs(nums[index], index + 1)

            # include
            currentPath.append(nums[index])
            dfs(-99999, index + 1)
            currentPath.pop()

        dfs(-99999, 0)

        return ret
