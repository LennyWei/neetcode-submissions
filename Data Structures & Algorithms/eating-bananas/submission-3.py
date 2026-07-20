class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        range(1, highestNumberInArray)
        [1, 2, 3, 4]
        
        with that range above, we do binary search where we pick a middle number, 
        see if it works, If yes, we need a lower number. If not, we need a high number
        '''

        left = 1
        right = max(piles)

        # pick the middle
        while left <= right:
            m = left + math.ceil((right-left)//2) # this is zero
            print(f"middle is {m} from right {right} - left {left}")

            # test with middle
            numOfHoursNeeded = 0
            for i in piles:
                hoursSpent = math.ceil(i/m)
                numOfHoursNeeded += hoursSpent

            print(f"num of hours needed {numOfHoursNeeded}")
            if numOfHoursNeeded > h:
                # doesn't work
                left = m+1
            elif numOfHoursNeeded <= h:
                # does work
                right = m-1
            # else:
            #     print(f"Is correct, returning")
            #     return m

        print(f"left {left} + right {right}")
        return left 
        #1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11