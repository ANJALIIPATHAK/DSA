class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numMap = {}
        n = len(nums)

        for num in nums:
            numMap[num] = 1 + numMap.get(num, 0)

        res = []
        for num, count in numMap.items():
            if count > n/3:
                res.append(num)
        
        return res

