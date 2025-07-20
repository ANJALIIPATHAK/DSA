class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(0, len(numbers)):
            numMap[numbers[i]] = i + 1

        for i in range(0, len(numbers)):
            diff = target - numbers[i]
            if(diff in numMap):
                return [i + 1, numMap[diff]]

    