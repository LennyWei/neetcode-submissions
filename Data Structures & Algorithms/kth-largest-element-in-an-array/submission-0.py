class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        keep a min heap

        whenever we push something and we have more than k number of nodes, pop
        otherwise just push 
        '''

        heap = []

        for i in nums:

            heapq.heappush(heap, i)

            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]