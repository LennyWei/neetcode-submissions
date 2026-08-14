class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        essentially we're looking for cycles 

        prereqs are gaurenteed lower than numCourses

        We can make a graph node implementation, and first build the graph, 
        then iterate through nodes, running the cycle detection algorithm 
        '''

        hashmap = {}

        for course, prereq in prerequisites:
            if course not in hashmap:
                hashmap[course] = [prereq]
            else:
                hashmap[course].append(prereq)
            
            if prereq not in hashmap:
                hashmap[prereq] = []

        
        path = set()

        def dfs(course):
            nonlocal path, hashmap
            
            if course in path:
                return False
            if course not in hashmap:
                return True

            # we wanna explore to other classes
            path.add(course)

            for prereq in hashmap[course]:
                if not dfs(prereq):
                    return False

            path.remove(course)
            hashmap[course] = []

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        
        return True