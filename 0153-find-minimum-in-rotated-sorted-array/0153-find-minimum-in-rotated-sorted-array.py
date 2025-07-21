class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        res = nums[left]

        while(left <= right):
            if(nums[left] < nums[right]):
                res = min(res, nums[left])
                return res

            mid = (left + right) // 2
            res = min(res, nums[mid])
            if(nums[mid] >= nums[left]):
                left = mid + 1
            elif(nums[mid] < nums[left]):
                right = mid - 1           
        return res