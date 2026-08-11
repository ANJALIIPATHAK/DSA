class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        majorityElem = 0
        count = 0

        for num in nums:
            if count == 0:
                majorityElem = num
                count = 1
            elif num == majorityElem:
                count += 1
            else:
                count -= 1

        leftCount = 0
        rightCount = nums.count(majorityElem)

        for i in range(0, len(nums)):
            if nums[i] == majorityElem:
                leftCount += 1
                rightCount -= 1

            leftLength = i + 1
            rightLength = len(nums) - 1 - i

            if 2 * leftCount > leftLength and 2 * rightCount > rightLength:
                return i
        return -1