class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        '''
        we need to find a substring (longest) that has 2 or less alien characters than the targeted char

        hashmap for frequency
        '''


        freq = {}

        ret = 0
        left = 0 

        # currentMostFreq = ("#", 0)

        for right in range(len(s)):

            # add to frequency
            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1

            # heres the main idea:
            # numReplace = length of substring (right - left) - most frequent char (we can keep a "currentMostFrequent" var)
            # naive way of finding frequent char: loop thru freq and get highest
            mostFreqChar = max(freq.values())
            numReplace = (right-left)+1 - mostFreqChar
            print(f"right is at {right} and the num rep is {numReplace}")
            # move the left til numReplace is at a safe level
            while numReplace > k:
                freq[s[left]] -= 1
                left += 1

                mostFreqChar = max(freq.values())
                numReplace = (right-left) - mostFreqChar


            if right-left > ret:
                ret = right-left
        
        return ret+1
            
            
                


