class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        posIdx = 0
        negIdx = 1
        for i in range(0, len(nums)):
            if(nums[i] > 0):
                res[posIdx] = nums[i]
                posIdx += 2
            else:
                res[negIdx] = nums[i]
                negIdx += 2
        return res
