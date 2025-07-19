class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(0, len(nums)):
            numMap[nums[i]] = i

        for i in range(0, len(nums)):
            diff = target - nums[i]
            if(diff in numMap and i != numMap[diff]):
                return [i, numMap[diff]]