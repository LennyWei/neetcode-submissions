class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        sliding window

        start two points at index 0

        left is the anchor
        right explores until we find a duplicate (duplicate lookup can be done with a set)

        if we find a duplicate, set the left to anchor on that duplicate now, and keep exploring 
        '''


        maxLength = 0

        left = 0
        right = 0

        seen = {}

        while right < len(s):
            # check right value
            if s[right] not in seen: # no dupe
                seen[s[right]] = right
                if len(seen) > maxLength: # or right-left
                    maxLength = len(seen)
            else: # found duplicate
                # we need to move the left one to where the first occurance of the duped element is + 1
                # can't just set it, need to get rid of all the other letters on the way
                
                while True: # we need to find the previous index of the 
                    if s[left] == s[right]:
                        left += 1
                        break
                    else:
                        seen.pop(s[left])
                        left += 1

                seen[s[right]] = right
            
            right += 1
        
        return maxLength


