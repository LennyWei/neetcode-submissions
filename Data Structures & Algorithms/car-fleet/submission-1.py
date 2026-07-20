class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        Observing:

        - any cars that have a mismatch in position vs speed becomes a fleet.
            - if car1 is faster but behind
            - or if car1 is slower but ahead ()
            - slower and behind, faster and ahead don't work

        im thinking we need to sort the positions first. 

        then use this formula:
        time = (target - position) / speed
        
        and stack to iterate backwards through the cars.
        '''

        # use zip()
        ls = sorted(zip(position, speed)) 
        stack = []
        print(ls)

        for pair in reversed(ls):
            time = (target-pair[0]) / pair[1]

            if stack:
                aheadTime = stack[-1]

                if aheadTime >= time:
                    # don't take from stack, same time to finish, leave it
                    pass  
                else:
                    # this car is slow enough to be it's own fleet
                    stack.append(time)
            else:
                stack.append(time)
        
        return len(stack)



