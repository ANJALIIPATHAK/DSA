class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numMap = {}

        for num in nums:
            if(num in numMap):
                return True
            else:
                numMap[num] = 1
        return False