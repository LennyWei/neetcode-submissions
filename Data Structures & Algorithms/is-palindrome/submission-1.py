class Solution:
    def isPalindrome(self, s: str) -> bool:
        # get rid of spaces
        # compare the first half with the reverse of second half.
        # what about no space complex? probably two pointers

        s = "".join([char for char in s if char.isalnum()]).lower()

        print(s)
        lastIndex = len(s)-1
        pointer = 0

        while pointer < (lastIndex+1 // 2):

            if s[pointer] != s[lastIndex-pointer]:
                return False
            pointer +=1

        return True

