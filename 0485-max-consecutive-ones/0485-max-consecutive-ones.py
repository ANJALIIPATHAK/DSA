class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        ones = 0
        for i in range(0, len(nums)):
            if(nums[i] == 1):
                ones += 1
                res = max(res, ones)
                print(res)
            else:
                ones = 0
        return res