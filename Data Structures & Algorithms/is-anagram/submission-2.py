class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = {}
        h2 = {}

        for i in s:
            if i in h1:
                h1[i] += 1
            else:
                h1[i] = 1

        for j in t:
            if j in h2:
                h2[j] += 1
            else:
                h2[j] = 1

        return True if h1 == h2 else False


