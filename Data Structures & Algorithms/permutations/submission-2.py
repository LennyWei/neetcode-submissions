class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        at every step, we choose between the remaining nums
        we keep a visited set to make sure we dont revisit anything

        psuedocode:

        if length of nums, add to ret 

        for i in nums:
            if not visited
                add to current List
                add to visited set
                run dfs
                remove from current List
                remove from visited set
        '''


        visited = set()
        currentList = []
        ret = []

        def dfs():
            nonlocal currentList, ret, visited

            if len(currentList) == len(nums):
                ret.append(currentList[:])
                return 


            for i in nums:
                if i not in visited:
                    currentList.append(i)
                    visited.add(i)
                    dfs()
                    currentList.pop()
                    visited.remove(i)
            
        
        dfs()

        return ret        



            

