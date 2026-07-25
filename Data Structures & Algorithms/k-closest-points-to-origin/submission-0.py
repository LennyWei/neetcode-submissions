class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        similar to the kth largest element in stream question.
        '''


        heap = []

        for point in points:
            # sqrt(x^2 + y^2)
            distance = math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2))

            heapq.heappush(heap, (-distance, point))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [i[1] for i in heap]