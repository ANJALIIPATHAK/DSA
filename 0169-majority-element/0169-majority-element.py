class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numMap = {}
        n = len(nums)
        for num in nums:
            numMap[num] = 1 + numMap.get(num, 0)
            if numMap.get(num, 0) > n/2:
                return num

