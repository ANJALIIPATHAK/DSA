class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if ((i == len(nums) - 1 or nums[i] > nums[i + 1]) and (i == 0 or nums[i] > nums[i - 1])):
                return i