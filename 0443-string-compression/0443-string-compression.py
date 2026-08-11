class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        target = 0

        while(left < len(chars)):
            chars[target] = chars[left]
            target += 1
            right = left + 1
            while(right < len(chars) and chars[left] == chars[right]):
                right += 1
            if right - left > 1:
                groupLength = str(right - left)
                for char in groupLength:
                    chars[target] = char
                    target += 1
            left = right
        return target