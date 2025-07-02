class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numMap = {}
        for num in nums:
            numMap[num] = 1 + numMap.get(num, 0)

        for num, key in numMap.items():
            while(key != 1):
                nums.remove(num)
                key -= 1
        
        return len(nums)


