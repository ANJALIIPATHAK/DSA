class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)

        for string in strs:
            charArr = [0]*26
            for char in string:
                charArr[ord(char) - ord("a")] += 1
            strMap[tuple(charArr)].append(string)
        
        return list(strMap.values())