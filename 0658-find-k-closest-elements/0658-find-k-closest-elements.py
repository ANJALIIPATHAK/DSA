class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1

        while(l < r):
            m = (l + r) // 2
            if arr[m] < x:
                l = m + 1
            else:
                r = m

        left = l - 1
        right = l

        while(right - left - 1 < k):
            if left < 0:
                right += 1
            elif right == len(arr):
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        return arr[left + 1 : right]
