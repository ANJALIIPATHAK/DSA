class Solution: 
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount = 0
        numSet = set(nums)

        for num in numSet:
            if num - 1 not in numSet:
                count = 1
                while(num + 1 in numSet):
                    count += 1
                    num += 1
                maxCount = max(maxCount, count)
        return maxCount          