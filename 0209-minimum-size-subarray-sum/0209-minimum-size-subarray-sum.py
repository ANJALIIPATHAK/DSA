class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        minLength = float("inf")
        for right in range(0, len(nums)):
            sum += nums[right]
            while(sum >= target):
                minLength = min(minLength, right - left + 1)
                sum -= nums[left]
                left += 1
        return 0 if minLength == float("inf") else minLength