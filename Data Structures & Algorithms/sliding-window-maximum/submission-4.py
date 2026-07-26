class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        maxHeap
        [val, index]

        what the hint are saying: we add numbers to heap normally, but when
        removing from heap, we should only start the process of removing when the thing being removed is 
        the maximum. We would remove and remove until we find a max that is in the range of [left, right] 
        '''

        ret = [0] * (len(nums)-k+1)

        left = 0 
        right = k

        maxHeap = []

        # first get the initial heap values

        for i in range(left, right):
            heapq.heappush(maxHeap, [-nums[i], i]) # we want the index and we want to use - for maxheap
        


        # now we traverse
        while right < len(nums):
            # get the max of current, place it in ret
            ret[left] = -maxHeap[0][0]

            # add right
            heapq.heappush(maxHeap, [-nums[right], right])
            right += 1

            # move left, do removing logic
            if maxHeap[0][1] == left:
                while maxHeap[0][1] <= left:
                    heapq.heappop(maxHeap)
            
            left += 1

        ret[left] = -maxHeap[0][0]
        return ret    
            

