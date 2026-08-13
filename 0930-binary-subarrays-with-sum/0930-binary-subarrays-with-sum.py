class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(x): # This function Calculates number of subarrays with sum <= x
            if x < 0:
                return 0
            left = 0
            sum = 0
            subArrays = 0
            for right in range(0, len(nums)):
                sum += nums[right]
                while sum > x:
                    sum -= nums[left]
                    left += 1
                subArrays += (right - left + 1) # Window size gives all possible subarrays with sum <= x
            return subArrays
        
        return helper(goal) - helper(goal - 1) # This returns number of subArrays with sum exactly equals to goal