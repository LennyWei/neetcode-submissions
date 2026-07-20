class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window problem

        '''
        keep a minLeft and maxRight variable?

        we essentially want a best: right-left value

        with two pointers, we base our actions on the difference between left and right

        our left is the anchor, it stays at currently known lowest buy price

        if right > left, we check that difference and see if that beats our known high
        if right < left, we found a new low, meaning we set the left pointer to that right
        if == do nothing but move r right
        '''



        if len(prices) < 2:
            return 0
        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):

            # check values
            difference = prices[right] - prices[left]

            if difference > maxProfit:
                maxProfit = difference
            elif difference < 0:
                left = right

            right += 1
        
        return maxProfit
