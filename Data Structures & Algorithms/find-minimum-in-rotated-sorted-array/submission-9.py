class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        [3,4,5,6,1,2]
        we need to find a cut:
        so we need a position where 

        left > m < right (cut is m index (where it resets down))
        
        if 
        left < m < right,
        left moves to m

        if 
        left > m > right,
        right moves to m

        what about
        left < m > right?

        we can find the cut in this situation too^
        (cut is right index (where it resets down))
        '''
        if len(nums) < 3:
            return min(nums)
        
        left = 0
        right = len(nums) - 1
        mid = (right + left)//2

        cut = -1

        while left < right:
            if (nums[left] > nums[mid] and nums[mid] < nums[right]):    # left > m < right
                if left+2 == right:
                    cut = mid
                    break
                right = mid+1

            elif nums[left] < nums[mid] and nums[mid] > nums[right]:    # left < m > right
                if left+2 == right:
                    cut = right
                    break
                left = mid
            elif nums[mid] > nums[right] and nums[mid] > nums[right]:   # left > m > right
                right = mid+1
            else:                                                       # left < m < right
                cut = left
                break

            mid = (right + left)//2

        # now we have cut, return
        return nums[cut]


