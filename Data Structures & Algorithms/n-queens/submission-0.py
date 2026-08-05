class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        essentially a queen means that we can't have another queen in the same diagonal/row/col, 


        ok so we need a queen at every col

        we can keep a hashmap of places that aren't allowed (to the right columns, not current column)
        '''

        ret = []
        board = [["."] * n for i in range(n)]

        print(["".join(i) for i in board])


        def isValid(row, col):
            nonlocal board
            # look left, top left diagonal, bottom left diagonal
            if col == 0: # first column is always good
                return True

            # limits
            minLimit = 0
            maxLimit = n-1
            # pointers for the diagonals
            topDia = row + 1
            botDia = row - 1

            # look left
            for column in range(col-1, -1, -1): # this will start at just before current col, will search left
                # check row
                if board[row][column] == "Q":
                    print(f"invalid row at {row}, {col}")
                    return False
                
                # check top diagonal
                if topDia <= maxLimit:
                    if board[topDia][column] == "Q":
                        print(f"invalid topdia at {row}, {col}")
                        return False
                    topDia += 1
                
                # check bottom diagonal
                if botDia >= minLimit:
                    if board[botDia][column] == "Q":
                        print(f"invalid botdia at {row}, {col}")
                        return False
                    botDia -= 1
            
            print(f"row {row} and col {col} is valid")
            return True




        def dfs(currentColumn):
            nonlocal ret
            nonlocal board

            # stop if we get to the end
            if currentColumn == n:
                ret.append(["".join(i) for i in board])
                return


            for row in range(n):
                if isValid(row, currentColumn):
                    
                    board[row][currentColumn] ="Q"
                    dfs(currentColumn + 1)
                    board[row][currentColumn] ="."
        

        dfs(0)
        return ret

        


