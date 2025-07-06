class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        sum = 0
        ansStart = -1
        ansEnd = -1
        for i in range(0, len( nums)):
            if(sum == 0):
                start = i
            sum += nums[i]
            if(sum > maxSum):
                maxSum = sum
                ansStart = start
                ansEnd = i
            if(sum < 0):
                sum = 0
        res = []
        for i in range(ansStart, ansEnd + 1):
            res.append(nums[i])
        print(res)
        return maxSum
        