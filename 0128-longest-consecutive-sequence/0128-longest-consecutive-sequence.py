class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        if(len(nums) == 0):
            return 0
        res = 1
        count = 1
        for i in range(0, len(nums)-1):
            if(nums[i+1] - nums[i] == 1):
                count += 1
            else:
                count = 1
            res = max(res, count)
        return res