class Solution:
    def search(self, nums: List[int], target: int):
        # find the pivot first

        left = 0
        right = len(nums) - 1

        while left < right:

            m = (right + left)//2

            if nums[m] > nums[right]:
                # means that middle is on the larger half
                left = m + 1
            else:
                # middle is on the lesser half
                right = m
        
        # now both should be at correct pivot point
        pivot = left

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        result = binary_search(0, pivot - 1)
        if result != -1:
            return result

        return binary_search(pivot, len(nums) - 1)
