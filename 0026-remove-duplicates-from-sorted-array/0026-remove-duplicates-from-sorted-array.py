class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        target = 0

        while i < len(nums):
            nums[target] = nums[i]
            target += 1
            j = i + 1
            while(j < len(nums) and nums[i] == nums[j]):
                curr = nums[j]
                j += 1
            if j - i > 1:
                nums[target] = curr
            i = j
        return target
