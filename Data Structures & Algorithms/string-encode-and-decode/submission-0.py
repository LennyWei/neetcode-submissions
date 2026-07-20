class Solution:

    def encode(self, strs: List[str]) -> str:
        # so we need to encode, take the list to make a str, but how do we show the splits?
        # would have to be "5#Hello5#World", so we know when to stop.
        t = ""

        for i in strs:
            t += str(len(i)) + "#" + i
        
        return t


    def decode(self, s: str) -> List[str]:
        # read the first number

        ret = []
        pointer = 0
        currentNumber = ""

        while pointer < len(s):
            # read the number until #

            while s[pointer] != "#":
                currentNumber += s[pointer]
                pointer += 1

            # at #, now need to read the "currentNumber" amount of characters

            pointer += 1
            length = int(currentNumber)
            stringToRet = ""

            for i in range(pointer, pointer + length):
                stringToRet += s[pointer]
                pointer += 1
            
                
            ret.append(stringToRet)

            #reset
            currentNumber = "" 
        
        return ret
                
            

