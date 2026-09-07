class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''
        so we make n number of choices every time, in nums

        so at each point, we are asking: how many ways of getting to the target are there at sum sumSoFar?

        i think we need a 2d memoization, where we use (sumSoFar, numWeWantToUse) or just sumSoFar?

        '''


        dp = {}

        n = len(nums)


        def dfs(sumSoFar):

            if sumSoFar == target:
                return 1
            elif sumSoFar > target:
                return 0
            
            if sumSoFar in dp:
                return dp[sumSoFar]

            # now we choose every posibility from nums
            ways = 0
            for num in nums:
                ways += dfs(sumSoFar + num)

            dp[sumSoFar] = ways

            return ways
        
        return dfs(0)



            


