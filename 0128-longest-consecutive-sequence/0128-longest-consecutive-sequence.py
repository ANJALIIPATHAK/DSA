class Solution: 
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        maxLength = 0
        for num in numSet:
            count = 1
            if(num - 1 not in numSet):
                while(num + 1 in numSet):
                    count += 1
                    num = num + 1
                maxLength = max(maxLength, count)
        return maxLength