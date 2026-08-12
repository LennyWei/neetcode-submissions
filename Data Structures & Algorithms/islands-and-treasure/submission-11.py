class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        we can either recurse and search from land cell, or recurse from each treasure chest

        its probably better to recurse from from each land cell, then pass back the shortest distance chest that they find to other 
        land cells too

        essentially, we run recurse on the first element, it searches for the closest teasre chest by recursing in all directions and 
        picking the smallest one. -1 cells return INF, stop there.

        we need to iterate through everything to make sure all inf lands are considered


        bfs: for all treasure chests, you insert nearby lands into the queue, 
        then you work through the queue layer by layer, every time adding one and inserting the nearby lands

        '''
        max_rows = len(grid)
        max_col = len(grid[0])
        visited = set()

        # bfs implementation, first insert 0 spots to queue
        queue = []

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row, col))
                    visited.add((row, col))

        def addAround(row, col, cellVal):
            nonlocal queue
            nonlocal visited

            if (min(row, col) < 0  or row >= max_rows or col >= max_col or grid[row][col] == -1 or (row, col) in visited):
                return
            
            #otherwise, add to queue
            queue.append((row, col))
            visited.add((row, col))

        layer = 0
        while queue:
            
            numCellsToGo = len(queue)

            for _ in range(numCellsToGo):
                #extract the front
                front = queue.pop(0)
                row = front[0]
                col = front[1]
                grid[row][col] = min(layer, grid[row][col])

                # add new nearby to queue (only if they're larger than current+1), what about double appending the same cell?
                addAround(row+1, col, layer)
                addAround(row-1, col, layer)
                addAround(row, col+1, layer)
                addAround(row, col-1, layer)

            layer += 1




            


