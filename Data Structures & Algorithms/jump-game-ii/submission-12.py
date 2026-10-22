class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        hard thing is to choose the greediest move (to get least amount of jumps) 
        WHILE also making sure you can get to the end

        maybe a backwards implementation?


        [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
        like keep track of index's that you can move to at this index. 

        essentially at index 2, we can move to index 11 since we have 9 moves at that index, so that index's move index is 11
        get the biggest move index, then update the two pointers range to that

        '''
        if len(nums) == 1:
            return 0

        left = 0
        right = 0
        jumps = 0

        while True:
            currentMaxRange = 0
            for i in range(left, right+1):
                currentMaxRange = max(currentMaxRange, i + nums[i])
            
            left = right + 1
            right = currentMaxRange
            jumps += 1

            if right >= len(nums)-1:
                return jumps

        print(f"{left} {right} {jumps}")
        return jumps