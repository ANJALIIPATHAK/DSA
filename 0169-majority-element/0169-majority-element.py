class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numMap = {}
        for num in nums:
            numMap[num] = 1 + numMap.get(num, 0)

        for num in numMap:
            if numMap[num] > len(nums) / 2:
                return num