class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        hint one: use array for frequency, the ighest freq is the one we're using 

        hint two: we use a max heap to keep track of the tasks to run next, then something
        else to cool them down (something that holds multiple tasks, and decreases their cooldown timer by one)
        could just be a list of 26  
        '''

        if n == 0:
            return len(tasks)
        

        maxHeap = []

        freq = [0] * 26
        cooldown = [[0, 0] for _ in range(26)] # tuple is for (countdown, freq)

        # first get the frequencies
        for i in tasks:
            freq[ord(i) - ord("A")] += 1
        
        # we fill up the maxHeap with a tuple (frequency, letter index)
        for index, val in enumerate(freq):
            if val != 0:
                heapq.heappush(maxHeap, [-val, index])
        
        print(maxHeap)
        
        # now we simulate until the maxHeap and cooldown is empty
        ret = 0

        while maxHeap or (sum([i[0] for i in cooldown]) > 0): # maybe theres a better way than sum
            # cooldown moving should happen before maxHeap grabbing
            for index, (count, freq) in enumerate(cooldown):
                if count != 0:
                    cooldown[index][0] -= 1 # count down

                    if cooldown[index][0] == 0: # we gotta bring it back
                        if freq != -1: # only if it's not -1 (last letter)
                            heapq.heappush(maxHeap, [freq + 1, index])
                        

            # take a item from maxHeap if possible
            if maxHeap:
                item = heapq.heappop(maxHeap)
                if item[0] == -1:
                    # last occurrence — no need to track its cooldown at all
                    cooldown[item[1]] = [0, 0]
                else:
                    cooldown[item[1]] = [n + 1, item[0]]
            
            ret += 1

        return ret




