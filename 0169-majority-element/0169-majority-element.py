class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for num in nums:
            if(count == 0):
                count = 1
                res = num
            else:
                if(num == res):
                    count += 1
                else:
                    count -= 1
        return res
