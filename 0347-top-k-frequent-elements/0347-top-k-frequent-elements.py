class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        countArr = [[] for i in range(0, len(nums)+1)]

        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)

        for num, freq in freqMap.items():
            countArr[freq].append(num)

        res = []
        for i in range(len(countArr) - 1, 0, -1):
            for num in countArr[i]:
                res.append(num)
                if(len(res) == k):
                    return res






