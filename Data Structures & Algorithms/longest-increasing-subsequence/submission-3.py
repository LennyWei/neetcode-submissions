class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        so at every index, if the next item is larger, we can choose to add the number to the increasing subsequence, or skip it and consider the i+2 one, if it's less, we can choose to skip item

        in other words, if next larger, 

        keep a currLength parameter and a max global variable
        '''
        n = len(nums)
        dp = {}
        ret = 0

        def dfs(i, prevChosen):
            nonlocal dp

            # print(f"i {i} prevChosen {prevChosen}")

            if i >= n:
                return 0
            if (i, prevChosen) in dp:
                return dp[(i, prevChosen)]    
            
            x = 0

            # we can choose the index for subsequence if greater than prevChosen
            if i < n and nums[i] > prevChosen:
                x = 1 + dfs(i+1, nums[i])

            # or we can skip 
            y = dfs(i+1, prevChosen)

            dp[(i, prevChosen)] = max(x, y)

            return dp[(i, prevChosen)]
        
        print(dp)
        return dfs(0, -2000)

