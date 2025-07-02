class Solution:
    def check(self, nums: List[int]) -> bool:
        rotationIndex = -1
        for i in range(0, len(nums)-1):
            if(nums[i] > nums[i+1]):
                rotationIndex = i
                break
        
        if(rotationIndex == -1):
            return True

        temp = []
        for i in range(rotationIndex + 1, len(nums)):
            temp.append(nums[i])

        for i in range(0, rotationIndex + 1):
            temp.append(nums[i])

        for i in range(0, len(temp)-1):
            if(temp[i] <= temp[i+1]):
                continue
            else:
                return False
        return True
