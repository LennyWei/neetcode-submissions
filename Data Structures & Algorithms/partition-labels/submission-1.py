class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        '''
        for each letter, it can only be seen in one split.

        first get frequency map

        then iterate through, keeping track of a set of {letters that still have yet to be completely found}
        when we see a new letter, add it to the set. if we see existing letter, reduce frequency, if freq == 0, we remove from set

        if set is 0 length, we add the length to output
        '''

        freq = {}

        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        

        searching = set()
        pointer = -1
        ret = []

        for index, letter in enumerate(s):
            if letter not in searching:
                searching.add(letter)
            
            freq[letter] -= 1

            if freq[letter] == 0:
                searching.remove(letter)

            if len(searching) == 0:
                ret.append(index - pointer)
                pointer = index
        
        return ret