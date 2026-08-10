class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        you can probably do that backtracking implementation where you iterate through until find a 1, then traverse, adding all ones that are
        connected to a "seen" set, and then continue, ignore if seen.

        if no extra memory, can just set the number to be 0

        '''

        num_rows = len(grid)
        num_cols = len(grid[0])


        def dfs(row, col):


            if (min(row, col) < 0 or 
            row >= num_rows or col >= num_cols or grid[row][col] == "0"):
                return False

            
            # found 1, search around
            grid[row][col] = "0"

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
            return True

        ret = 0

        for i in range(num_rows):
            for j in range(num_cols):
                if dfs(i, j):
                    ret += 1
        
        return ret