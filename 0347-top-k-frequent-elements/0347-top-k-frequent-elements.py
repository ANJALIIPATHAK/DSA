class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        res = []

        for num in nums:
            numMap[num] = 1 + numMap.get(num, 0)
        
        numFreq = sorted(numMap.items(), key = lambda x : x[1], reverse = True)

        for i in range(0, k):
            res.append(numFreq[i][0])
        
        return res
        