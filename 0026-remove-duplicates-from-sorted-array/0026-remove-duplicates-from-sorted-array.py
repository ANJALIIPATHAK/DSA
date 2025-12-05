class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numSet = set(nums)
        i = 0
        for num in numSet:
            nums[i] = num
            i += 1
        nums[ : len(numSet)] = sorted(numSet)
        return len(numSet)