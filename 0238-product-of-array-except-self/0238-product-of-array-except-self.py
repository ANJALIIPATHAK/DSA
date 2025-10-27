class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preArr = [1] * len(nums)
        postArr = [1] * len(nums)

        prefix = 1
        for i in range(1, len(nums)):
            prefix *= nums[i-1]
            preArr[i] = prefix

        postfix = 1
        for i in range(len(nums)-2, -1, -1):
            postfix *= nums[i+1]
            postArr[i] = postfix
        
        res = []
        for i in range(0, len(nums)):
            res.append(preArr[i] * postArr[i])
        
        return res




