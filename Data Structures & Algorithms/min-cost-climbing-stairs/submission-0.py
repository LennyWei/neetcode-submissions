class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        '''
        at every step, what are we asking

        at every step, we need to either take 1 step, or 2 steps (or you can think of it as, at every step, you could have came from one or two steps before that step.) 

        this problem, it's more efficient to solve the problem from right to left, essentially solving the subproblems first, using that info to solve the problems that needed that subproblem 
        
        
        given [1, 2, 3]

        we need a list of [0, 0, 0, 0, 0]
        then work through this   ^
    
        '''

        dp = [0] * len(cost) + [0, 0]


        for i in range(len(cost)-1, -1, -1):

            # at this step, we need the min cost of future steps to get to the end, and this current one
            dp[i] = min(dp[i+1], dp[i+2]) + cost[i]
        
        print(dp)
        
        return min(dp[0], dp[1])
