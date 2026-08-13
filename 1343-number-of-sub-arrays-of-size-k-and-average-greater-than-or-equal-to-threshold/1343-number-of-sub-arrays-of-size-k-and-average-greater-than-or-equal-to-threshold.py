class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        validSubArrays = 0
        sum = 0
        
        for i in range(0, k - 1):
            sum += arr[i]

        for left in range(0, len(arr) - k + 1):
            right = left + k - 1
            sum += arr[right]
            if sum / k >= threshold:
                validSubArrays += 1
            sum -= arr[left]
        return validSubArrays
