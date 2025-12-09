class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majElem = 0

        for num in nums:
            if count == 0:
                majElem = num
            if num == majElem:
                count += 1
            else:
                count -= 1
        return majElem
