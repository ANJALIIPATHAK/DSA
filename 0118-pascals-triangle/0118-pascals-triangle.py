class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTriangle = []
        for i in range(0, numRows):
            pascalTriangle.append([1]*(i + 1))

        for i in range(2, len(pascalTriangle)):
            for j in range(1, len(pascalTriangle[i])-1):
                pascalTriangle[i][j] = pascalTriangle[i - 1][j - 1] + pascalTriangle[i - 1][j]
        
        return pascalTriangle