class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numMap = {}
        for num in nums:
            numMap[num] = 1 + numMap.get(num, 0)

        for num, freq in numMap.items():
            if(freq > len(nums)//2):
                return num
