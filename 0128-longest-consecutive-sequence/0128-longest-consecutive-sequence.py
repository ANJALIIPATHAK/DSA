class Solution: 
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        numSet = set(nums)

        for num in numSet:
            if num - 1 not in numSet:
                count = 1
                while(num + 1 in numSet):
                    count += 1
                    num += 1
                maxLength = max(maxLength, count)
        return maxLength          