from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # hashmap + sliding window

        # make hash of both s and t

        ht = {}
        hsub = {}
        for i in t:
            hsub[i] = 0
            if i not in ht:
                ht[i] = 1
            else:
                ht[i] += 1
        
        ret, retLength = "", math.inf
        # for the substring
        
        left = 0
        right = 0

        # main problem: how to check if frequency of sub is "at least" freq of t? 
        isValidWindow = False

        while right < len(s) or isValidWindow:
            # if the frequency tables aren't the same, build them
            isValidWindow = not (Counter(ht) - Counter(hsub)) # this is a slow solution

            if not isValidWindow:

                if s[right] in ht:
                    hsub[s[right]] += 1
                
                right += 1
            else: 
                # check if this is better than previous, then move left pointer and remove from freq
                print(f"is valid, {left} and {right}")
                if right-left < retLength:
                    retLength = right-left
                    ret = s[left:right]
                    print(f"set new output to, {ret}")

                #remove left from freq, move left
                if s[left] in hsub:
                    hsub[s[left]] -= 1
                    print(f"removing, {s[left]}")
                
                left += 1
        
        isValidWindow = not (Counter(ht) - Counter(hsub))

        print(f"{left} and {right}")
        while isValidWindow:
            if right-left < retLength:
                retLength = right-left
                ret = s[left:right]
                print(f"set new output to, {ret}")

            if s[left] in hsub:
                hsub[s[left]] -= 1
                print(f"removing, {s[left]}")
            left += 1

            isValidWindow = not (Counter(ht) - Counter(hsub))

        return ret

        


        