class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        return A valid ordering, not all valid orderings

        '''

        hashmap = {}

        for course, prereq in prerequisites:
            if course not in hashmap:
                hashmap[course] = [prereq]
            else:
                hashmap[course].append(prereq)
            
            if prereq not in hashmap:
                hashmap[prereq] = []

        print(hashmap)
        path = set()
        visit = set()
        ret = []

        def dfs(course):
            nonlocal path, hashmap, ret, visit
            if course in path:
                return False
            if course in visit:
                return True

            if course not in hashmap: # if there was no mention at all, 
                ret.append(course)
                visit.add(course)
                return True

            # we wanna explore to other classes
            path.add(course)

            for prereq in hashmap[course]:
                if not dfs(prereq):
                    return False

            path.remove(course)
            hashmap[course] = []
            visit.add(course)
            ret.append(course)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return ret