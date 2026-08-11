class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowelSet = set(["a", "e", "i", "o", "u"])

        countArr = [0] * len(words)
        validWordsSoFar = 0

        for index, word in enumerate(words):
            if word[0] in vowelSet and word[-1] in vowelSet:
                validWordsSoFar += 1
            countArr[index] = validWordsSoFar

        res = []
        for qLeft, qRight in queries:
            if qLeft == 0:
                res.append(countArr[qRight])
            else:
                res.append(countArr[qRight] - countArr[qLeft - 1])

        return res
