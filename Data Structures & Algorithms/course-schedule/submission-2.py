class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #DFS // this is a topological sort question
        # we can use an adjacency list tho
        # if we detect a loop, it's impossible

        preqs = defaultdict(list)
        for c in range(numCourses):
            preqs[c] = []
        for p in prerequisites:
            preqs[p[0]].append(p[1])

        visited = set()

        def dfs(course):
            if preqs[course] == []:
                return True
            
            if course in visited:
                return False

            visited.add(course)
            for p in preqs[course]:
                if not dfs(p): return False

            preqs[course] = []
            
            visited.remove(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
        
        return True
