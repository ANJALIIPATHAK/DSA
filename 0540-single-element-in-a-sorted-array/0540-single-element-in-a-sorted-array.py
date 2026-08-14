class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if ((mid == 0 or nums[mid] != nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] != nums[mid + 1])):
                return nums[mid]

            leftWindowLen = mid if nums[mid] != nums[mid - 1] else mid - 1
            if leftWindowLen % 2 == 0:
                left = mid + 1
            else:
                right = mid - 1

