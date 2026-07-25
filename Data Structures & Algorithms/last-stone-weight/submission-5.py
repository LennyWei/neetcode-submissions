class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]
        stones = [-i for i in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            print(stones)
            Rocky = heapq.heappop(stones)
            Stony = heapq.heappop(stones)

            DESTRUCTION = -abs(Rocky - Stony)

            if DESTRUCTION < 0:
                heapq.heappush(stones, DESTRUCTION)
        print(stones)
        if stones:
            return -stones[0] 
        return 0