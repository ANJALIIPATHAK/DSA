class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}

        for num in nums:
            numMap[num] = 1 + numMap.get(num, 0)

        countArr = [[] for i in range(0, len(nums) + 1)]
        for num, count in numMap.items():
            countArr[count].append(num)

        res = []
        for i in range(len(countArr)-1, 0, -1):
            for num in countArr[i]:
                res.append(num)
                if(len(res) == k):
                    return res





