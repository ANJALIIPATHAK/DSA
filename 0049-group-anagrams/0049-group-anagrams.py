class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)

        for string in strs:
            sortedString = "".join(sorted(string))
            strMap[sortedString].append(string)

        return list(strMap.values())
        