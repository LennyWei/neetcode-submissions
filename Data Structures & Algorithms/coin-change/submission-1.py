class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        
        so brute force, we can find every sequence that adds up to the amount, then grab the lowest one

        another way to look at it is, at every point, we choose between 3 choices (len(amount)), we need the shortest height
        of that decision tree

        base condition:
        if greater than amount, return something that signals bad path (returning 99999 or -1)

        if equal to amount, return 0, signaling this is a good path 


        greedy approach wouldn't work with this:
        [1, 3, 4] amount - 6

        '''



        dp = {}



        def dfs(amountLeft):
            
            if amountLeft < 0:
                return math.inf
            if amountLeft == 0:
                return 0
            if amountLeft in dp:
                return dp[amountLeft]
            
            ret = math.inf

            for i in coins:

                nextChoice = dfs(amountLeft - i)

                ret = min(ret, 1 + nextChoice)
            
            dp[amountLeft] = ret

            return ret
        
        ans = dfs(amount)


        if ans == math.inf:
            return -1
        
        return ans




