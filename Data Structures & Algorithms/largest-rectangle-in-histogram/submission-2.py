class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        We wanna interate thru the bars
        there are 3 cases,
        
        current bar is less than the previous one
        current bar is greater/the same as the previous one

        when >=, we add to the monotonic stack that keeps an increasing list
        when <, we start cutting down the stack
            while the top of the stack is still < current bar, 
                we calculate the area it would give
                    using that height and the index diff, comparing it to a global max
            
            Then also set the current bar's index to be the last cut bar
        

        At the end, we just do the algorithm but with a extra 0 height bar


        '''
        heights.append(0)

        stack = [(0, heights[0])] # tuple containing (adjIndex, value)

        maxSoFar = 0

        print(f"{stack}, max known is {maxSoFar}")

        for i in range(1, len(heights)):
            # 1, 2, 3, 4, 2,
            value = heights[i]

            if value > stack[-1][1]: # add
                stack.append((i, heights[i]))
            elif value < stack[-1][1]: # main algo, remove
                lastRemoved = 0
                area = 0
                
                while stack and value < stack[-1][1]:
                    removed = stack.pop()
                    # calc area
                    area = removed[1] * (i-removed[0])
                    # print(f"we calced {area} with {removed[1]} * {i-removed[0]}")

                    if area > maxSoFar:
                        maxSoFar = area
                    lastRemoved = removed[0]
                
                # add the new one in
                stack.append((lastRemoved, value))
            
            # print(f"{stack}, max known is {maxSoFar}")
        
        return maxSoFar
                


        