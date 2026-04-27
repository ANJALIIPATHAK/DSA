class Solution: 
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        i = 1
        maxCount = 1
        currCount = 1
        while(i < len(nums)):
            if nums[i] - nums[i - 1] == 0:
                i += 1
            elif nums[i] - nums[i - 1] == 1:
                i += 1
                currCount += 1
            else:
                i += 1
                currCount = 1
            maxCount = max(maxCount, currCount)
        return maxCount
            