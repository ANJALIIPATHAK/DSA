class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        prefixArr = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            prefixArr[i] = prefix

        postfix = 1
        postfixArr = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            postfix *= nums[i + 1]
            postfixArr[i] = postfix

        res = []
        for i in range(0, len(nums)):
            res.append(prefixArr[i] * postfixArr[i])
        return res