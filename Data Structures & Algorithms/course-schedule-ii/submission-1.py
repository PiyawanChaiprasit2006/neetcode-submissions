class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #bfs?

        #no it has to be dfs because it needs to be in order

        preqs = defaultdict(list)

        for c in range(numCourses):
            preqs[c] = []
        
        for p in prerequisites:
            preqs[p[0]].append(p[1])

        result = []

        visited = set()

        def dfs(course):
            if preqs[course] == []:
                if course not in result:
                    result.append(course)
                return True
            
            if course in visited:
                return False

            visited.add(course)

            for c in preqs[course]:
                if not dfs(c): return False
            preqs[course] = []
            visited.remove(course)
            result.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        
        return result

        
            





        