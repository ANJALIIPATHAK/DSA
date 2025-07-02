class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numSet = set()
        nextIndex = 0
        for i in range(0, len(nums)):
            if(nums[i] in numSet):
                continue
            else:
                numSet.add(nums[i])
                nums[nextIndex] = nums[i]
                nextIndex += 1

        return len(numSet)

