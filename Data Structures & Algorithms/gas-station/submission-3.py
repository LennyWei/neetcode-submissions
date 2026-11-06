class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        greedy, so 

        at every index, you can describe a net value, gasGained - costToGetToNext

        you can make the whole list with that in mind
        ex1
        [-1, 0, -1, 3]


        '''
        if sum(gas) < sum(cost):
            return -1

        total = 0
        result = 0

        # if total goes negative, result is next num
        for index, val in enumerate(gas):
            gasValue = val - cost[index] # gas - cost
            
            total += gasValue

            if total < 0:
                total = 0
                result = index + 1 # out of bounds will never happen?

        return result

            