class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        strings = s.split('-')
        chars = []
        res = ''

        for string in strings:
            chars += list(string)
        
        firstCount = len(chars) % k
        res = ''.join(chars[:firstCount]).upper()
        idx = firstCount
        while idx < len(chars):
            if len(res):
                res += '-'
            res += ''.join(chars[idx: idx + k]).upper()
            idx += k
        return res