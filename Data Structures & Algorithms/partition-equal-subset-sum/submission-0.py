class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        so at any point, we can choose to either add the num to subset1 or subset2

        when we get to the end, we return True only if the two sets are equal in sum

        in terms of memoization: 
        

        another way: get sum(nums)/2, then try to find a combination that adds up to that sum?

        brute force, i go through each index, choosing/not choosing order to get the target down to 0

        '''

        n = len(nums)

        target = sum(nums)/2

        if target % 1 != 0:
            print(f"{target} is a float")
            return False
        
        # brute force done, now memoization
        dp = {}

        def dfs(i, target):
            if i >= len(nums):
                return False
            if (i, target) in dp:
                return dp[(i, target)]

            if target == 0:
                return True
            elif target < 0:
                return False
            

            # choose and not choose
            dp[(i, target)] = dfs(i+1, target) or dfs(i+1, target-nums[i])
            return dp[(i, target)]
        
        return dfs(0, target)



