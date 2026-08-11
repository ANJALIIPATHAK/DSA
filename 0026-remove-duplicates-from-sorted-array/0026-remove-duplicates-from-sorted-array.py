class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        target = 0

        while(left < len(nums)):
            nums[target] = nums[left]
            target += 1
            right = left + 1
            while(right < len(nums) and nums[left] == nums[right]):
                nextElem = nums[right]
                right += 1
            if right - left > 1:
                nums[target] = nextElem
            left = right
        return target