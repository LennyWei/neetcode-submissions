class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        for the "-1 if impossible case", we can sum up all fruits, and keep a tally of how many rotten fruits there are

        if we run a simulation and then end isn't the total sum, then we know its impossible

        it seems to be very similar to the previous treasure example, bfs with a queue of rotten fruits
        '''

        totalFruits = 0
        totalRotten = 0
        max_row = len(grid)
        max_col = len(grid[0])
        queue = []

        for row in range(max_row):
            for col in range(max_col):
                if grid[row][col] == 1:
                    totalFruits += 1
                elif grid[row][col] == 2:
                    totalFruits += 1
                    totalRotten += 1

                    queue.append((row, col))


        def checkRotten(row, col):
            nonlocal totalRotten

            if (min(row, col) < 0 or row >= max_row or col >= max_col or grid[row][col] == 0 or grid[row][col] == 2):
                return
            
            grid[row][col] = 2
            queue.append((row, col))
            totalRotten += 1

        minute = 0

        while queue:
            minute += 1
            for i in range(len(queue)):
                # check all sides
                r, c = queue.pop(0)

                checkRotten(r+1, c)
                checkRotten(r-1, c)
                checkRotten(r, c+1)
                checkRotten(r, c-1)
        if totalFruits == 0:
            return 0

        if totalFruits == totalRotten:
            return minute-1
        else:
            return -1



