class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left = 0
        right = len(nums) - 1

        while(left <= right):
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]: # We are in left sorted portion
                left = mid + 1
            elif nums[mid] < nums[left]: # We are in the right sorted portion
                right = mid - 1
        return res

