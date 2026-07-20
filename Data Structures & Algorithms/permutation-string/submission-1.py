class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        make a freq hashmap of s1 (No, we do [0] * 26, easier for comparisons and technically O(1) comparison) 

        sliding window s2, keep a hashmap for s2, keep searching right until you contain
        all of s1, then you move left until all other extraneous letters are gone (by check if removing current )
        
        sliding with a fixed length

        
        '''
        if len(s1) > len(s2):
            return False

        freqs1 = [0] * 26
        freqs2 = [0] * 26

        # make freqs1
        for i in s1:
            freqs1[ord("a") - ord(i)] += 1
        
        # loop through s2, keeping track of freqs2
        left = 0
        right = 0

        # first populate with the initial window size
        for right in range(len(s1)):
            letter = s2[right]
            freqs2[ord("a") - ord(letter)] += 1

        while right < len(s2):
            # compare the freqs
            matching = True
            for i in range(26):
                if freqs1[i] != freqs2[i]:
                    matching = False
                    break
            
            if matching: # if fully matching. return true
                return True

            # after, we move the window and update freqs2
            

            freqs2[ord("a") - ord(s2[left])] -= 1
            left +=1

            right += 1 # problem, right can go out of range
            if right < len(s2):
                freqs2[ord("a") - ord(s2[right])] += 1
        
        return False





