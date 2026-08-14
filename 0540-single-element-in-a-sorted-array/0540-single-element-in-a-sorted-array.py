class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        for i in range(0, len(nums)):
            if i > 0 and i < len(nums) - 1:
                if nums[i] == nums[i - 1] or nums[i] == nums[i + 1]:
                    continue
                else:
                    return nums[i]
            elif i == 0:
                if nums[i] == nums[i + 1]:
                    continue
                else:
                    return nums[i]
            elif i == len(nums) - 1:
                if nums[i] == nums[i - 1]:
                    continue
                else:
                    return nums[i]