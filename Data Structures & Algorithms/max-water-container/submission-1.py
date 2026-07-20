class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        was the idea for two pointers to start at the middle, then expand outward if it has a higher area? no

        The main idea with this one is: "move the pointer with the smallest height"
        '''

        maxKnownArea = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            # check water level now, check it against maxKnownArea

            waterAmount = (right-left) * min(heights[left], heights[right])
            print(f"found water amount {waterAmount} when left is {left} and right {right}")

            if waterAmount > maxKnownArea:
                maxKnownArea = waterAmount
            
            # move the smallest height pointer

            if heights[left] < heights[right]: # when it's equal we want the right to move
                left += 1
            else:
                right -= 1
        
        return maxKnownArea