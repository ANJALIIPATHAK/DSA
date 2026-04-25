class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}

        for num in nums:
            numMap[num] = 1 + numMap.get(num, 0)

        countArr = []
        for num,count in numMap.items():
            countArr.append([count, num])

        countArr.sort()

        res = []
        while(len(res) < k):
            res.append(countArr.pop()[1])
        return res

        
