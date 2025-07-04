class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numMap = {}
        for num in nums:
            numMap[num] = 1 + numMap.get(num, 0)
        for num, freq in numMap.items():
            if(freq == 1):
                return num