class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # classic two pointer problem

        p1 = 0
        p2 = len(numbers)-1

        s = numbers[p1] + numbers[p2]

        while s != target:
            
            if s > target:
                p2 -= 1
            else:
                p1 +=1

            s = numbers[p1] + numbers[p2]
             
        return [p1+1, p2+1]