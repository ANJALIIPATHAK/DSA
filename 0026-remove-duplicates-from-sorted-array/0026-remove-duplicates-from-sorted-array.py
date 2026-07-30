class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        count = 1

        while(right < len(nums) and left < right):
            if nums[left] == nums[right]:
                right += 1
            else:
                nums[left + 1] = nums[right]
                left += 1
                right += 1
                count += 1
        return count
