class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)

        for word in strs:
            countArr = [0] * 26
            for char in word:
                countArr[ord(char) - ord("a")] += 1
            strMap[tuple(countArr)].append(word)
        return list(strMap.values())