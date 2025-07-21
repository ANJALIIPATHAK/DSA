class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1

        left = 0
        right = len(nums)-1

        while(left <= right):
            mid = (left + right) // 2

            if(nums[mid] == target):
                res = mid
                break
            elif(nums[mid] >= nums[left]): # We are in left sorted portion
                if(target > nums[mid]):
                    left = mid + 1
                elif(target < nums[mid]):
                    if(nums[left] > target):
                        left = mid + 1
                    else:
                        right = mid - 1
            elif(nums[mid] < nums[left]): # We are in the right sorted portion
                if(target < nums[mid]):
                    right = mid - 1
                elif(target > nums[mid]):
                    if(nums[right] < target):
                        right = mid - 1
                    else:
                        left = mid + 1
        return res




