class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        res = right

        while(left <= right):
            k = (left + right) // 2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile/k)
            if(totalTime <= h):
                res = min(res, k)
                right = k - 1
            elif(totalTime > h):
                left = k + 1
        return res
