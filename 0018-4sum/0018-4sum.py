class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        finalRes = set()
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                numMap = {}
                for k in range(j + 1, len(nums)):
                    l = target - (nums[i] + nums[j] + nums[k])
                    if(l in numMap):
                        res = [nums[i], nums[j], nums[k], l]
                        res = tuple(sorted(res))
                        finalRes.add(res)
                    numMap[nums[k]] = 1
        return list(finalRes)