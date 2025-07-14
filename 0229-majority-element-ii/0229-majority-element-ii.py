class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numMap = {}
        for num in nums:
            numMap[num] = 1 + numMap.get(num, 0)

        res = []
        for num, freq in numMap.items():
            if(freq > len(nums)//3):
                res.append(num)
            if(len(res) == 2):
                return res
        return res
