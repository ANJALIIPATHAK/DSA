class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        nums = sorted(nums)

        left = 0
        right = nums[-1] - nums[0]
        res = right

        while left <= right:
            mid = (left + right) // 2
            i = 0
            pairs = p
            while pairs > 0 and i < len(nums)-1:
                if nums[i + 1] - nums[i] <= mid:
                    pairs -= 1
                    i += 2
                else:
                    i += 1
            if pairs == 0:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res
                
