class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        can you run the tradition backtracking algorithm, once forward,
        but again with the list reversed? the sum of those lists is the answer? no




        so:

        at 1, we look right, one recursion with 3, one with 2 next.
        
        
        [true, true, true]
        
        temp = []

        for i in nums:
            recurse(i, )
        '''

        chosen = [False] * len(nums)
        currentPath = []
        ret = []

        def dfs():

            if len(currentPath) == len(nums):
                ret.append(currentPath[:])
                return
            
            for i in range(0, len(nums)):

                if chosen[i]: # if true
                    continue
                # choose a valid number
                chosen[i] = True
                currentPath.append(nums[i])
                dfs()

                # need to also reverse changes (for the next iteration)
                chosen[i] = False
                currentPath.pop()

        dfs()

        return ret




            

