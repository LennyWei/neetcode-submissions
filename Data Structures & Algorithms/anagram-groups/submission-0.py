class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        naive solution:

        sort each individual string

        keep a hashmap that looks like:

        {
            act : ["act", "cat"]       Where the list is the index of strs
            aht : ["hat"]
            stop : ["pots", "tops", "stops"]
        }

        and then at the end just create a for loop (or two) that adds everything 



        Without sorting: 

        Build a hashmap for every string? no

        '''

        array = [0] * 26 # O(26)

        hashmap = {}

        for word in strs:

            for char in word:
                convertedChar = ord(char) - 97
                array[convertedChar] += 1
            

            # [0, 1, 0, 1, ...., 0]

            if tuple(array) in hashmap:
                hashmap[tuple(array)].append(word)
            else:
                hashmap[tuple(array)] = [word]

            #reset
            array = [0] * 26

        ret = []

        for i in hashmap.values():
            ret.append(i)
        
        return ret




