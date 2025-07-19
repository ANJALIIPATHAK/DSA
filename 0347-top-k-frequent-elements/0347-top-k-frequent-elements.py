class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for num in nums:
            countMap[num] = 1 + countMap.get(num, 0)
        
        countArr = []
        for num, count in countMap.items():
            countArr.append([count, num])

        countArr = sorted(countArr)

        res = []
        for i in range(k, 0, -1):
            res.append(countArr.pop()[1])

        return res


