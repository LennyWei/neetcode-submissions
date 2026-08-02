class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        maybe keep a set variable to keep track of

        '''

        nums.sort()

        ret = []

        subset = []

        def dfs(index, prev):
            nonlocal ret
            nonlocal subset
            
            if index >= len(nums):
                ret.append(subset[:])
                return

            # with and without
            subset.append(nums[index])
            dfs(index + 1, nums[index])
            subset.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
                
            dfs(index + 1, nums[index])

        dfs(0, -1)
        print(ret)

        return ret