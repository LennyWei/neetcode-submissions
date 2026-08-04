class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        split the string up into multiple substrings, every possible split of substrings

        in every split, we return the strings that are palindromes


        is the decision being made being "start a new substring with this letter or not?"

        '''

        ret = []

        def isPalindrome(s):
            lastIndex = len(s)-1
            pointer = 0

            while pointer < (lastIndex+1 // 2):

                if s[pointer] != s[lastIndex-pointer]:
                    return False
                pointer +=1

            return True

        def dfs(currentSubstring, lsOfSubstrings, index):
            nonlocal ret
            print(currentSubstring)

            
            
            # return condition
            if index >= len(s):
                palin = isPalindrome(currentSubstring)

                if palin:
                    lsOfSubstrings.append(currentSubstring)
                    ret.append(lsOfSubstrings[:])
                    lsOfSubstrings.pop()
                    
                return


            # start a new substring or not, continue with the previous one

            # continuing means dfs(currentSubstring+s[index], lsOfSubstrings, index + 1)
            dfs(currentSubstring+s[index], lsOfSubstrings, index + 1)

            # starting a new means dfs(s[index], lsOfSubstrings appended, index+1)
            if currentSubstring != '' and isPalindrome(currentSubstring):
                lsOfSubstrings.append(currentSubstring)
                dfs(s[index], lsOfSubstrings, index+1)
                lsOfSubstrings.pop()                




        dfs("", [], 0)

        return ret


