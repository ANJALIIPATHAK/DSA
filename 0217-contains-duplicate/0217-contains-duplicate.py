class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set(nums)
        if(len(nums) == len(numSet)):
            return False
        else:
            return True