class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encodedStr = ""
        for word in strs:
            encodedStr = encodedStr + str(len(word)) + "#" + word
        print(encodedStr)
        return encodedStr


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decodedStr = []
        i = 0

        while(i < len(s)):
            j = i
            while(s[j] != "#"):
                j += 1
            wordLength = int(s[i : j])
            i = j + 1
            j = i + wordLength
            decodedStr.append(s[i:j])
            i = j
        return decodedStr




        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))