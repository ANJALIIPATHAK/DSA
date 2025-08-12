class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = []
        while(k > 0):
            res = (-(heapq.heappop(nums)))
            k -= 1
        return res