class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = count2 = 0
        elem1 = elem2 = -10**-9 - 1

        for num in nums:
            if(count1 == 0 and num != elem2):
                count1 = 1
                elem1 = num
            elif(count2 == 0 and num != elem1):
                count2 = 1
                elem2 = num
            elif(num == elem1):
                count1 +=1
            elif(num == elem2):
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = count2 = 0
        for num in nums:
            if(num == elem1):
                count1 += 1
            if(num == elem2):
                count2 += 1

        res = []
        min = (len(nums) // 3 + 1)
        if(count1 >= min):
            res.append(elem1)
        if(count2 >= min):
            res.append(elem2)
        return res

