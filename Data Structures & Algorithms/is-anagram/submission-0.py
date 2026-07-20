class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = [0] * 26
        arr2 = [0] * 26

        for i in s:
            arr1[ord(i) - ord("a")] += 1

        for j in t:
            arr2[ord(j) - ord("a")] += 1

        return True if arr1 == arr2 else False


