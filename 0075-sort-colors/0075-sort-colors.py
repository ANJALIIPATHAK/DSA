class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        countArr = [0] * 3
        for num in nums:
            countArr[num] += 1

        write = 0
        for color in range(3):
            while(countArr[color] > 0):
                nums[write] = color
                write += 1
                countArr[color] -= 1
        