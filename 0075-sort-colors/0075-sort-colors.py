class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums)-1):
            min = i
            for j in range(i, len(nums)):
                if(nums[j] < nums[min]):
                    min = j
            nums[i], nums[min] = nums[min], nums[i]
