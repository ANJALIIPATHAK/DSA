class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        validSubArrays = 0
        left = 0
        right = k - 1
        sum = 0

        for i in range(left, right + 1):
            sum += arr[i]

        while(right < len(arr)):
            if sum / k >= threshold:
                validSubArrays += 1
            sum -= arr[left]
            left += 1
            right += 1
            if right < len(arr):
                sum += arr[right]
        return validSubArrays

            