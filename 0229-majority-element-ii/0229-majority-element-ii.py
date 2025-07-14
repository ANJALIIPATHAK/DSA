class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = [ ]
        numMap = {}
        n = len(nums)
        for num in nums:
            numMap[num] = 1 + numMap.get(num, 0)
            if(numMap[num] == n//3 + 1):
                res.append(num)
            if(len(res) == 2):
                return res
        return res
