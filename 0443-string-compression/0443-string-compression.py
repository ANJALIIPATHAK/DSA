class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        target = 0

        while(i < len(chars)):
            chars[target] = chars[i]
            target += 1
            j = i + 1
            while(j < len(chars) and chars[i] == chars[j]):
                j += 1
            if j - i > 1:
                groupLength = str(j - i)
                for char in groupLength:
                    chars[target] = char
                    target += 1
            i = j
        return target