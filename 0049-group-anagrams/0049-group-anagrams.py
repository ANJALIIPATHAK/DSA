class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)

        for word in strs:
            sortedWord = "".join(sorted(word))
            strMap[sortedWord].append(word)

        return list(strMap.values())
        