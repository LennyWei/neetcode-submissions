class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        i kinda remember this one, you keep a stack of "waiting days indexes"
        go through the array reverse
        '''
        stack = []
        ret = [0] * len(temperatures)

        for index, val in enumerate(temperatures):
            
            while stack and val > stack[-1][0]:

                sVal, sIndex = stack.pop()

                ret[sIndex] = index-sIndex

            stack.append((val, index))

        return ret