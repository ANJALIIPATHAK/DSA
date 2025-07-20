class Solution: 
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        
        numSet = set(nums)

        maxCount = 1
        for num in numSet:
            count = 1
            if((num-1) not in numSet):
                while((num + 1) in numSet):
                    count +=  1
                    num = num + 1
            maxCount = max(maxCount, count)
        return maxCount