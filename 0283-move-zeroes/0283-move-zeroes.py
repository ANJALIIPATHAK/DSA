class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZero = 0

        for i in range(0, len(nums)):
            if(nums[i] != 0):
                nums[nonZero], nums[i] = nums[i], nums[nonZero]
                nonZero += 1