class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0, len(numbers)):
            left = i + 1
            right = len(numbers) - 1
            diff = target - numbers[i]
            while(left <= right):
                mid = (left + right) // 2
                if numbers[mid] > diff:
                    right = mid - 1
                elif numbers[mid] < diff:
                    left = mid + 1
                else:
                    return [i+1, mid+1]