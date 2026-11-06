class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        we want group sizes of groupSize, so if len isn't divisible, false

        brute force. sort the hand, init the groups [-1, -1]

        [1, 2, 2, 3, 3, 4, 4, 5]

        iterate through the list, iterate through the groups to see if that card is allowed in any of the groups. this is n^2 though

        or use a dictionary/set that stores the "next one it needs"
        '''

        if len(hand) % groupSize != 0: # divisible case
            return False
        
        
        
        hashmap = {}
        heap = [] # heapify

        for i in hand:
            if i not in hashmap:
                hashmap[i] = 1
                heapq.heappush(heap, i)
            else:
                hashmap[i] += 1

        # no need to sort, just heapify hand.sort() 

        print(hashmap)
        print(heap)

        while heap:

            # take lowest
            lowest = heap[0]

            for i in range(lowest, lowest + groupSize):

                if i in hashmap:
                    hashmap[i] -= 1
                    
                    if hashmap[i] == 0:
                        # saying if not lowest that's being 0'd, somethings wrong
                        if i == lowest:  
                            print(f"popping away lowest {lowest} from {heap}")
                            heapq.heappop(heap)
                            if heap:
                                lowest = heap[0]
                            
                        else:
                            return False
                else:
                    return False

        return True





    
        

       







