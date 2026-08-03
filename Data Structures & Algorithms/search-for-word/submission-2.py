class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        essentially we nede to backtrack, at every iteration (we iterate through the entire list)

        we check if the current letter is in the hashmap of required letters:
        {
        C: 1
        A: 1
        T: 1
        }

        If not, return false
        If is, -1 on the hashmap and explore adjacent blocks (use a helper function to figure out which
        of the four directions you can traverse (North, south, east, west))

        Then recurse on them, and return the ORs of those return calls:

        HaveAGoodPath = recurseNorth() or recurseSouth() or recurseWest() or recurseEast()

        if we have a good path, we return true

        we need to make sure that the previous good cell isn't called again when doing the explored new
        cell right?

        I didn't keep into account order (c, then a, then t)
        I can revisit cells i've already been at
        '''
        if len(word) > len(board) * len(board[0]):
            return False

        freq = {}
        remainingLetters = len(word)
        # build freq
        for i in word:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        print(f"freq {freq} with remainingLetters {remainingLetters}")


        # helper function to see which directions can go from current cell
        
        def explore(i, j, comingFrom = ""): # i is row, j is col
            nonlocal freq
            nonlocal remainingLetters

            letter = board[i][j]

            if letter not in freq:
                return False
            elif freq[letter] == 0:
                return False
            elif letter != word[len(word) - remainingLetters]:
                return False

            freq[letter] -= 1
            remainingLetters -= 1

            if remainingLetters == 0:
                print(f"FOUND at {i}, {j}, comingFrom {comingFrom}")
                return True

            valid = False

            if i > 0 and comingFrom != "S": # if not first row, we can explore down
                valid = valid or explore(i-1, j, "N")

            if i < len(board) - 1 and comingFrom != "N": # if not last row, explore up
                valid = valid or explore(i+1, j, "S")
            
            if j > 0 and comingFrom != "L": # if not first col, explore left
                valid = valid or explore(i, j-1, "R")
            
            if j < len(board[0]) - 1 and comingFrom != "R": # if not last col, explore right
                valid = valid or explore(i, j+1, "L")
            
            freq[letter] += 1
            remainingLetters += 1

            return valid 
        
        ret = False

        for i in range(len(board)):
            for j in range(len(board[0])):
                ret = ret or explore(i, j)
        
        return ret






