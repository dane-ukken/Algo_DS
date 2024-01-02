class Solution:
    def numDecodings(self, s: str) -> int:
        codeDict = {"": 1}  # Base case: one way to decode an empty string

        def findPossibleDecodeCount(s):
            if s in codeDict:
                return codeDict[s]

            if s[0] == '0':  # Strings starting with '0' cannot be decoded
                return 0

            # Decode using the first character
            firstTotal = findPossibleDecodeCount(s[1:])

            # Decode using the first two characters if valid
            secondTotal = 0
            if len(s) >= 2 and s[0:2] <= "26":
                secondTotal = findPossibleDecodeCount(s[2:])

            codeDict[s] = firstTotal + secondTotal
            return codeDict[s]

        return findPossibleDecodeCount(s)
