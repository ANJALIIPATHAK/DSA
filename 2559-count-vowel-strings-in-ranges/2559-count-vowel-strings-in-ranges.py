class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        vowelSet = set(["a", "e", "i", "o", "u"])

        countArr = [0] * len(words)

        sumSoFar = 0

        for i in range(len(words)):
            if words[i][0] in vowelSet and words[i][-1] in vowelSet:
                sumSoFar += 1
            countArr[i] = sumSoFar

        res = []
        for q in queries:
            if q[0] == 0:
                res.append(countArr[q[1]])
            else:
                res.append(countArr[q[1]] - countArr[q[0] - 1])

        return res