class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        keep a visited set, run dfs on EVERY node if not visited, adding it to the visited set and
        incrementing by 1 
        '''
        hashmap = {}

        for i in range(n):
            hashmap[i] = []
        
        for leftNode, rightNode in edges:
            hashmap[leftNode].append(rightNode)
            hashmap[rightNode].append(leftNode)

        visited = set()

        def dfs(node):
            # return if visited already
            if node in visited:
                return
            
            # visit it
            visited.add(node)

            # explore all
            for connectedNode in hashmap[node]:
                dfs(connectedNode)
        
        ret = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                ret += 1
        
        return ret
