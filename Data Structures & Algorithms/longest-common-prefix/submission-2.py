class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # you can take the longest string, then iterate through. O(n)

        longestWord = ""

        for i in strs:
            if len(i) > len(longestWord):
                longestWord = i
        
        ret = ""

        for index in range(len(longestWord)):
            for word in strs:
                if index >= len(word):
                    return ret

                if longestWord[index] != word[index]:
                    return ret
            
            ret += longestWord[index]
        
        return ret