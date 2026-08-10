class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        numIslands problem, but we count how big each island is
        '''
        num_rows = len(grid)
        num_cols = len(grid[0])


        def dfs(row, col):

            if (min(row, col) < 0 or 
            row >= num_rows or col >= num_cols or grid[row][col] == 0):
                return 0
            
            # found 1, search around
            grid[row][col] = 0

            
            total = (
            dfs(row+1, col)
            + dfs(row-1, col)
            + dfs(row, col+1)
            + dfs(row, col-1)
            )


            return total + 1

        ret = 0

        for i in range(num_rows):
            for j in range(num_cols):
                islandSize = dfs(i, j)
                if islandSize > ret:
                    ret = islandSize
        
        return ret