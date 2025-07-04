class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumExpected = (n * (n + 1)) // 2
        sumActual = sum(nums)
        return (sumExpected - sumActual)