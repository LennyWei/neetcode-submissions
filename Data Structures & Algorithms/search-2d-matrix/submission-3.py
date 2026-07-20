class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # will break when theres no matrix[0]
        numOfElements = len(matrix) * len(matrix[0])
        lenOfInner = len(matrix[0])

        left = 0
        right = numOfElements-1

        while left < right:

            m = (right + left)//2

            value = matrix[m // lenOfInner][m % lenOfInner]
            print(f"m is {m} which is val {value}")

            if value > target:
                right = m
            elif value < target:
                left = m + 1
            else:
                return True
        
        val = matrix[right // lenOfInner][right % lenOfInner]

        if val == target:
            return True
        else:
            return False