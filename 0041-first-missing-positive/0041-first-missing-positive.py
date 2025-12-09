class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums)-1):
            if 1 in nums:
                if nums[i+1] - nums[i] > 1 and nums[i] >= 0:
                    res = nums[i] + 1
                    return res
        if 1 in nums:
            res = nums[-1] + 1
        else:
            res = 1
        return res

            

                
