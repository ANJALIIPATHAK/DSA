class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(0, len(nums)):
            diff = target - nums[i]
            if(diff in numMap):
                return ([numMap[diff], i])
            else:
                numMap[nums[i]] = i
