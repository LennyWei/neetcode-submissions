class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        do we use tuples and sets to deal with duplicates?

        '''
        nums.sort()

        ret = []
        currentPath = []

        def dfs(index):

            if index >= len(nums):
                ret.append(currentPath[:])
                return

            # include and exclude

            # include
            currentPath.append(nums[index])
            dfs(index + 1)
            currentPath.pop()

            #exclude, skip repeated ones
            while index + 1 <len(nums) and nums[index] == nums[index+1]:
                index += 1
            
            dfs(index + 1)

        dfs(0)

        return ret
