class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(0, len(nums)):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            left = i + 1
            right = len(nums)-1
            while(left < right):
                sum = nums[i] + nums[left] + nums[right]
                if(sum > 0):
                    right -= 1
                elif(sum < 0):
                    left += 1
                elif(sum == 0):
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while(left < right and nums[left] == nums[left-1]):
                        left += 1
                    while(left < right and nums[right] == nums[right + 1]):
                        right -= 1
        return res


