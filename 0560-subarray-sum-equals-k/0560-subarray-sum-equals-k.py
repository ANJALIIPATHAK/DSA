class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSumMap = {}
        prefixSum = 0
        for i in range(0, len(nums)):
            prefixSumMap[prefixSum] = 1 + prefixSumMap.get(prefixSum, 0)
            prefixSum += nums[i]
            if(prefixSum - k in prefixSumMap):
                res = res + prefixSumMap[prefixSum - k]
        return res
