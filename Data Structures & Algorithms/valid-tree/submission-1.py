class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        is this just, make sure there are no cycles? again?

        kahns algorithm,


        simply just run dfs and if you dont explore an already explored node, we good right? 
        hashmap first
        '''
        hashmap = {}

        for i in range(n):
            hashmap[i] = []
        
        for leftNode, rightNode in edges:
            hashmap[leftNode].append(rightNode)
            hashmap[rightNode].append(leftNode)
        

        visit = set()

        def dfs(prev, node):
            nonlocal visit
            # check if in visit, if is, return False
            if node in visit:
                return False
            
            valid = True
            visit.add(node)

            # check around, except prev
            for nextNode in hashmap[node]:
                if nextNode != prev:
                    valid = valid and dfs(node, nextNode)
            
            return valid 

        if dfs(-1, 0) and len(visit) == n:
            return True
        return False


        