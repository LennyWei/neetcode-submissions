class Solution:
    def trap(self, height: List[int]) -> int:
        
        def algo(ls):

            '''
            two pointer solution

            left finds a height

            right searches for a higher to height while adding to water count

            if it does find a higher height than left, left becomes right and we keep going
            '''
            left = 0
            right = 0
            waterTotal = 0

            while right < len(ls):

                if ls[right] > ls[left]:
                    # set left to right
                    left = right
                elif ls[right] < ls[left]:
                    waterTotal += ls[left] - ls[right]
                
                right += 1
            
            return waterTotal
        
        # find the index of the summit

        index = 0
        for i, val in enumerate(height):
            if val >= height[index]:
                index = i 
        
        return algo(height[:index]) + algo(list(reversed(height[index:])))

