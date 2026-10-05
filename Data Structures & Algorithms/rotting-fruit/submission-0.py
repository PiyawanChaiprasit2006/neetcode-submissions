class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rotting = deque()

        rows = len(grid)
        cols = len(grid[0])

        hours = 0

        oranges = 0

        for r in range(rows):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotting.append([r, c])
                if grid[r][c] == 1:
                    oranges += 1

        while rotting and oranges > 0:
            
            for _ in range(len(rotting)):
                rot = rotting.popleft()

                r = rot[0]
                c = rot[1]

                if r < rows -1:
                    if grid[r + 1][c] == 1:
                        grid[r + 1][c] = 2
                        rotting.append([r + 1, c])
                        oranges -= 1
                if r > 0:
                    if grid[r - 1][c] == 1:
                        grid[r - 1][c] = 2
                        rotting.append([r - 1, c])
                        oranges -=1 
                if c < cols -1:
                    if grid[r][c+1] == 1:
                        grid[r][c+1] = 2
                        rotting.append([r, c+1])
                        oranges -= 1
                if c > 0:
                    if grid[r][c-1] == 1:
                        grid[r][c-1] = 2
                        rotting.append([r, c-1])
                        oranges -= 1
                
            hours += 1

        if oranges == 0:
            return hours
        else:
            return -1



