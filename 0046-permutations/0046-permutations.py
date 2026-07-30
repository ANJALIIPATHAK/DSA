class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []
        visited = set()

        def backtrack():
            if len(permutation) == len(nums):
                res.append(permutation[:])
                return            
            for num in nums:
                if num in visited:
                    continue
                #Choose
                permutation.append(num)
                visited.add(num)

                #Explore / backtrack call
                backtrack()

                #Undo the choose
                permutation.pop()
                visited.remove(num)
        backtrack()
        return res

            
        