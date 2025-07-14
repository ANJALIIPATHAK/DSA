class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = [ ]
        numMap = {}
        min = (len(nums) // 3) + 1
        for num in nums:
            numMap[num] = 1 + numMap.get(num, 0)
            if(numMap[num] == min):
                res.append(num)
            if(len(res) == 2):
                return res
        return res
