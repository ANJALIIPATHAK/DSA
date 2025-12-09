class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)

        for word in strs:
            charArr = [0]*26
            for char in word:
                charArr[ord(char) - ord("a")] += 1
            strMap[tuple(charArr)].append(word)
        
        return list(strMap.values())
