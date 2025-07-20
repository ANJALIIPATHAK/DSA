class Solution: 
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0

        nums = sorted(nums)

        maxCount = 1
        count = 1

        i = 0
        j = 1
        while(i < len(nums) -1 and j < len(nums)):
            if(nums[i] == nums[j]):
                i += 1
                j += 1
            elif(nums[j] - nums[i] == 1):
                count += 1
                i += 1
                j += 1
            else:
                count = 1
                i = j
                j = i + 1
            maxCount = max(maxCount, count)

        return maxCount