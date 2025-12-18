class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        left = 0
        countMap = {}

        for right in range(0, len(s)):
            countMap[s[right]] = 1 + countMap.get(s[right], 0)
            while(right - left + 1 - max(countMap.values()) > k):
                countMap[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength