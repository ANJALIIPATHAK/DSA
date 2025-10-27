class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sMap = defaultdict(list)

        for word in strs:
            charArr = [0]*26
            for char in word:
                charArr[ord(char) - ord("a")] += 1
            sMap[tuple(charArr)].append(word)

        return list(sMap.values())