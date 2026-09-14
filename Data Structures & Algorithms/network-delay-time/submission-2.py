# class TreeNode:
#     def __init__(self, val) -> None:
#         self.val = val
#         self.targets = set() # set of (node, cost) pairs
#         self.isEnd = False



class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        starting at k, how long would it take to visit every single node

        usual approach is dijkstras, which is a BFS approach that uses a min heap
        
        make a "time to make it to each node" list: [inf, inf, inf, inf....]

        the goal is to get the max of dist (and if its inf, we return -1)
        
        '''
        visited = set()

        fringe = [(0, k)] # heap

        # think we still need to make the connections
        edges = {}

        for i in range(n):
            edges[i+1] = []

        for source, target, time in times:
            edges[source].append((time, target)) # we want time first bc the heap will look at time as the thing to sort for
        
        ret = 0

        while fringe:
            # bfs
            # process the min heap node, explore the others
            node = heapq.heappop(fringe)
            if node[1] in visited:
                continue
            
            visited.add(node[1])

            ret = max(ret, node[0])

            # add to fringe the neighbors
            for pair in edges[node[1]]:
                newpair = (pair[0] + node[0], pair[1])
                heapq.heappush(fringe, newpair)
        

        if len(visited) == n:
            return ret
        else:
            return -1


