class MedianFinder:
    '''
    we learned this in class i think

    have two heaps, a min and max heap?

    It's like we want to keep them the same length, but also pop and push such that 

    max heap keeps the lower half of the elements
    min heap keeps the higher half of the elements

    such that median is the pop of whichever is longest, OR the pop-of-both/2 if same length


    so, given a new item. 
    if heaps are equal:

    max: [4, 3, 2]
    min: [5, 6, 7]

    if <= max[0], place in max, otherwise, place in min

    if heaps are skewed in size, (ie the difference between the lnegths > 1), we pop push to whichever is less


    how do we maintain the maxheapness of the maxheap
    '''
    def __init__(self):
        self.maxHeap = [] # lower half
        self.minHeap = [] # upper half

    def addNum(self, num: int) -> None:
        if not self.maxHeap:
            heapq.heappush(self.maxHeap, -num)
        elif not self.minHeap:
            
            if num < -self.maxHeap[0]:
                #pop push, swap
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.minHeap, num)

        else:
            # if at least 1 element in each heap
            if num <= -self.maxHeap[0]:
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.minHeap, num)
            
            # check if either heap is larger than another

            difference = len(self.maxHeap) - len(self.minHeap)
            print(f"difference is {difference} and heaps are min {self.minHeap} and max {self.maxHeap}")

            if difference == -2: # min is 2 bigger
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
            elif difference == 2: # max is 2 bigger
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            
            print(f"difference is {difference} and heaps are min {self.minHeap} and max {self.maxHeap}")

    def findMedian(self) -> float:
        print(f"finding median min {self.minHeap}, max {self.maxHeap}")
        difference = len(self.maxHeap) - len(self.minHeap)

        if difference == 1:
            return float(-self.maxHeap[0])
        elif difference == -1:
            return float(self.minHeap[0])
        elif difference == 0:
            return (-self.maxHeap[0] + self.minHeap[0])/2
        else:
            return -1.0
        