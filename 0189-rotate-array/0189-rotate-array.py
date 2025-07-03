class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if(k > len(nums)):
            k = k % len(nums)
            
        temp = []
        i = 0
        while(len(temp) + k != len(nums)):
            temp.append(nums[i])
            i += 1
        rotationIndex = i

        for i in range(0, k):
            nums[i] = nums[i + rotationIndex]

        for i in range(k, len(nums)):
            nums[i] = temp[i - k]



        
