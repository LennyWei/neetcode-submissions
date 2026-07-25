class KthLargest:
    '''
    We can use heapq, which is a min-heap/priority queue

    since it's a min heap, we can use negatives to flip it to be a max heap, no not neccessary
    as long as we keep the size of the heap to k, the first index will always be the kth largest
    '''



    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)
        
        return None

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            # pop first, push val
            heapq.heappushpop(self.heap, val)
        
        return self.heap[0]

