class Solution:
    def check(self, nums: List[int]) -> bool:
        sortedNums = sorted(nums)
        if(nums == sortedNums):
            return True
        rotationIndex = -1
        for i in range(0, len(nums)-1):
            if(nums[i] > nums[i+1]):
                rotationIndex = i
                break

        temp = []
        for i in range(rotationIndex + 1, len(nums)):
            temp.append(nums[i])

        for i in range(0, rotationIndex + 1):
            temp.append(nums[i])

        if(temp == sortedNums):
            return True
        else:
            return False