class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        store the mappings in a dictionary?

        we can use a for loop version of backtracking

        at every recursion we run a for loop that iterates through each mapping of the number, "choosing" that mapping for that digits
        and then calling the recurse(nextDigitIndex). We can keep a parameter called "currentString" and return it only if it reaches the current height
        '''


        ret = []
        mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }


        def dfs(currentString, index):

            if len(currentString) == len(digits):
                if len(currentString)>0:
                    ret.append(currentString)
                return
            

            for letter in mappings[digits[index]]:
                dfs(currentString + letter, index + 1)
            
        dfs("", 0)
        return ret



        