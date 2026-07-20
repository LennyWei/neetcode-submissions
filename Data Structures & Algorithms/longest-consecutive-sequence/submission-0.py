class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # make hashmap with all of the nums for quick referencing

        h = {}
        for i in nums:
            if i not in h:
                h[i] = 0


        # find the starting sequences, which is found by looking for a num that doesn't have a num-1.
        startingSequences = []

        for i in nums:
            if i-1 not in h:
                startingSequences.append(i)

        print(startingSequences)

        longest = 0
        for i in startingSequences:
            currLength = 1
            j = i
            while j+1 in h:
                currLength +=1
                j += 1

            if currLength > longest:
                longest = currLength


        return longest 
        # then keep counting up, looking for the next number, if larger than the current known longest, set that as such.
        # keep doing this, except for the higher numbers, like 10 for example 1

