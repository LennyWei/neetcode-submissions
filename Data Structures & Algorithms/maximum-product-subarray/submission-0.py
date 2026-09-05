class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        subarray, so we probably need a 2d array for the memoization again like that other palindrome one
        we wanna keep like dp[i][j] is the product of the subarray[i:j]

        at each step, if the current index is negative, we check if 

        n^2 gaurenteed?

        we need to go through each possible subarray?

        choose the next 
        '''
        n = len(nums)
        ret = max(nums)

        curMin = 1
        curMax = 1

        for n in nums:
            # zero, reset to a neutral number
            if n == 0:
                curMin, curMax = 1, 1
                continue
            
            temp = curMax * n 
            curMax = max(n * curMax, n * curMin, n) # [-1, 8]
            curMin = min(temp, n * curMin, n) 
            
            ret = max(ret, curMax)
        
        return ret





        


