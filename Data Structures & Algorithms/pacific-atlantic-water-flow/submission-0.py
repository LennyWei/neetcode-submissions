class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        very interesting Solution

        two sets 
        atlantic and pacific. We run dfs twice seperately, once for the pacific starting cells, once for the atlantic starting cells.
        we explore around, marking cells that are greater than the current cell by adding it to their respective sets, continuing
        '''

        atlantic = set()
        pacific = set()

        max_row = len(heights)
        max_col = len(heights[0])

        def dfs(row, col, prev, isPacific = True):
            nonlocal max_row
            nonlocal max_col
            nonlocal atlantic
            nonlocal pacific
            # usual checks
            if (min(row, col) < 0 or row >= max_row or col >= max_col or prev > heights[row][col]):
                return
            
            # skipping if in respective list (dont think its too neccessary)
            if isPacific and (row, col) in pacific:
                return
            elif not isPacific and (row, col) in atlantic:
                return

            # is valid, add to thing
            if isPacific:
                pacific.add((row, col))
            else:
                atlantic.add((row, col))

            # check around
            dfs(row+1, col, heights[row][col], isPacific)
            dfs(row-1, col, heights[row][col], isPacific)
            dfs(row, col+1, heights[row][col], isPacific)
            dfs(row, col-1, heights[row][col], isPacific)
        
        # we do pacific and atlantic
        # col 1 row 1 is pacific
        # last col and last row is atlantic

        for i in range(max_col):
            dfs(0, i, 0, True)
        # print(f"pacific: {pacific}, atlantic: {atlantic}")

        for j in range(max_row):
            dfs(j, 0, 0, True)

        for i in range(max_col):
            dfs(max_row-1, i, 0, False)

        for j in range(max_row):
            dfs(j, max_col-1, 0, False)

        return list(atlantic & pacific)
