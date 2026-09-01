class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        the only difference is that the houses are in a circle (first connects to last)

        we can simply use a variable denoting whether or not 

        or we just use the same algorithm but use it in two different scenarios

        [0, n-1] #essentially ignoring end
        and
        [1, n] # ignoring start

        and taking the max of both


        '''

        if len(nums) == 1:
            return nums[0]

        memo = [-1] * (len(nums)-1)


        def dfs(i, ls):

            if i >= len(ls):
                return 0
            
            if memo[i] != -1:
                return memo[i]
            

            # pick the next one, or pick this and next next one
            memo[i] = max(dfs(i+1, ls), ls[i] + dfs(i+2, ls))

            return memo[i]
        

        noEnd = dfs(0, nums[0:-1])
        
        memo = [-1] * (len(nums)-1)

        noStart = dfs(0, nums[1:])

        print(f"NoEnd {noEnd}, noStart {noStart}")

        return max(noEnd, noStart)

        