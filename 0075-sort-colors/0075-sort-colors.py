class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def merge(nums, low, mid, high):
            left = low
            right = mid + 1
            temp = []
            while(left <= mid and right <= high):
                if(nums[left] <= nums[right]):
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
            while(left <= mid):
                temp.append(nums[left])
                left += 1
            while(right <= high):
                temp.append(nums[right])
                right += 1
            for i in range(low, high + 1):
                nums[i] = temp[i-low]
        def helper(low, high):
            if(low >= high):
                return
            mid = (low + high) // 2
            helper(low, mid)
            helper(mid + 1, high)
            merge(nums, low, mid, high)
        
        helper(0, len(nums)-1)

        
