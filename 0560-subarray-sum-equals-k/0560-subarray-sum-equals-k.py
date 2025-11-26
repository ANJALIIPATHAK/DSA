class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = 0
        prefixMap = {}

        for i in range(0, len(nums)):
            prefixMap[prefix] = 1 + prefixMap.get(prefix, 0)
            prefix += nums[i]

            if(prefix - k) in prefixMap:
                res += prefixMap[prefix - k]
        return res