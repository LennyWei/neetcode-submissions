class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        i = len(grid)
        j = len(grid[0])
        numIs = 0

        for x in range(i):
            for y in range(j):
                visited = [] # stack
                if grid[x][y] == "1":
                    visited.append([x, y])
                    grid[x][y] = "0"
                    if visited:
                        newX, newY = visited.pop()
                        Solution.traverse(newX, newY, i, j, grid, visited)
                    numIs += 1
        
        return numIs


    def traverse(x, y, i, j, grid, visited):
        # left
        if y != 0:
            if grid[x][y-1] == "1" and [x,y-1] not in visited:
                visited.append([x, y-1])
                grid[x][y-1] = "0"
                Solution.traverse(x, y-1, i, j, grid, visited)

        # right
        if y != j-1:
            if grid[x][y+1] == "1" and [x,y+1] not in visited:
                visited.append([x, y+1])
                grid[x][y+1] = "0"
                Solution.traverse(x, y+1, i, j, grid, visited)
        
        # up
        if x != 0:
            if grid[x-1][y] == "1" and [x-1,y] not in visited:
                visited.append([x-1, y])
                grid[x-1][y] = "0"
                Solution.traverse(x-1, y, i, j, grid, visited)
        
        # down
        if x != i-1:
            if grid[x+1][y] == "1" and [x+1,y] not in visited:
                visited.append([x+1, y])
                grid[x+1][y] = "0"
                Solution.traverse(x+1, y, i, j, grid, visited)
        
        # backtrack
        if not visited:
            return
        