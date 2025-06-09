class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        for num in nums:
            numMap[num] = 1 + numMap.get(num, 0)

        freqCount = [[] for i in range(0, len(nums) + 1)]
        for num in numMap:
            freqCount[numMap[num]].append(num)

        res = []
        for i in range(len(freqCount)-1, -1, -1):
            if(k == 0):
                return res
            for num in freqCount[i]:
                res.append(num)
                k -= 1

