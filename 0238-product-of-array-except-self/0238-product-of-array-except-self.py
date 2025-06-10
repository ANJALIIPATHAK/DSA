class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroCount = 0
        for num in nums:
            if(num == 0):
                zeroCount += 1
                continue
            else:
                product *= num
        
        answer = [0]*len(nums)

        for i in range(0, len(nums)):
            if(zeroCount == 1):
                if(nums[i] == 0):
                    answer[i] = product
            elif(zeroCount > 1):
                return answer
            else:
                answer[i] = (product // nums[i])

        return answer
