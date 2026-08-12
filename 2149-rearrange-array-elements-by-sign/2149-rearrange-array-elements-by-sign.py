class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posIdx = 0
        negIdx = 1
        res = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                res[posIdx] = nums[i]
                posIdx += 2
            else:
                res[negIdx] = nums[i]
                negIdx += 2
        return res