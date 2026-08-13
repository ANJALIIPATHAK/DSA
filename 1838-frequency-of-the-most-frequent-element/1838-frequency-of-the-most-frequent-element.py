class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        maxFreq = 0
        
        left = 0
        windowSum = 0

        for right in range(0, len(nums)):
            windowSum += nums[right]
            while nums[right] * (right - left + 1) - windowSum > k:
                windowSum -= nums[left]
                left += 1
            maxFreq = max(maxFreq, (right - left + 1))
        return maxFreq