class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numMap = defaultdict(int)

        for num in nums:
            numMap[num] += 1
            
            if len(numMap) <= 2:
                continue
            
            newNumMap = defaultdict(int)
            for num, count in numMap.items():
                if count > 1:
                    newNumMap[num] = count-1
            numMap = newNumMap

        res = []
        for num in numMap:
            if nums.count(num) > len(nums)/3:
                res.append(num)
        return res

