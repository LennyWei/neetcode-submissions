class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        binary search: sorted start
        have left and right pointer
        
        get mid, compare it to target, less or more, move the left or right pointer.

        usually left = mid+1, right = mid
        
        do until left > right
        '''


        left = 0
        right = len(nums)-1

        while left < right:
            
            mid = (left + right)//2

            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid
            else:
                return mid
        
        if nums[right] == target:
            return right

        return -1
        