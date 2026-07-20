class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Have:

        A hashmap to keep frequencies
        An array of size k to keep track of which elements are the top amounts 

        another hashmap
        
        '''

        # first make frequency map
        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        # now we make the buckets
        buckets = [[] for _ in range(len(nums))]
        
        # place the numbers in the buckets based off frequency (where the index of buckets is freq)
        for num, f in freq.items():
            buckets[f-1].append(num)

        # now we iterate through backwards to find the most k frequent nums
        print(buckets)
        ret = []

        for i in reversed(buckets):
            
            for j in i:
                ret.append(j)
                print(f"added to ret, {ret}")
                if len(ret) == k:
                    return ret

        return [-1]


