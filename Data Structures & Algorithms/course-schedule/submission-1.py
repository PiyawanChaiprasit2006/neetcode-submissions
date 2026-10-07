class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #BFS // this is a topological sort question
        # we can use an adjacency list tho
        # if we detect a loop, it's impossible

        prereqs = defaultdict(list)

        for course, preq in prerequisites:
            prereqs[course].append(preq)
            
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if prereqs[course] == []:
                return True
            
            visited.add(course)
            for c in prereqs[course]:
                if not dfs(c): return False
            visited.remove(course)
            prereqs[c] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True

       
            