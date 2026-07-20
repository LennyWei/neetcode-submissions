class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left < right:

            m = (right+left) // 2
            print(f"{m}")

            if nums[m] >= target:
                right = m
            else:
                left = m + 1
        print(f"left {left} right {right}")

        if nums[left] == target:
            return left
        else:
            return -1