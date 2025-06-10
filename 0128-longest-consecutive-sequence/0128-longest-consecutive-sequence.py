class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for num in numSet:
            count = 1
            if(num-1 not in numSet):
                while(num+1 in numSet):
                    count += 1
                    num += 1
                res = max(res, count)
        return res