class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        this one is just the previous one but we cant reuse the same index

        and we need to take care of duplicate answers
        '''
        candidates.sort()
        ret = []
        currentPath = []

        def dfs(startingIndex, currentSum):
            nonlocal ret
            nonlocal currentPath

            if currentSum == target:
                t = currentPath
                ret.append(t[:])
                return
            elif currentSum > target:
                return
            
            prev = -1

            for i in range(startingIndex, len(candidates)):
                if candidates[i] == prev:
                    continue
                currentPath.append(candidates[i])
                dfs(i + 1, currentSum + candidates[i])
                currentPath.pop()
                prev = candidates[i]
            
        dfs(0, 0)
        return ret