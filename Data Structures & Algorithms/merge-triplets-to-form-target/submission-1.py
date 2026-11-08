class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        '''
        theres max only ever 3 things to merges right?

        so for every triplet, we analyze their worth?

        < > =

        we need to find = triplets, but they cant have any elements that are >
        we can ignore any that do actually.

        '''

        target1Satisfied = False
        target2Satisfied = False
        target3Satisfied = False

        for one, two, three in triplets:
            # skip triplet if over target
            if one > target[0] or two > target[1] or three > target[2]:
                continue
            
            if one == target[0]:
                target1Satisfied = True
            if two == target[1]:
                target2Satisfied = True
            if three == target[2]:
                target3Satisfied = True
        


        if target1Satisfied and target2Satisfied and target3Satisfied:
            return True
        else:
            return False
