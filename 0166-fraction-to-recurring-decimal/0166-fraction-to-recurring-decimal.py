class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # long division
        if denominator == 0: 
            if numerator == 0:
                return 'Indeterminate'
            return 'Undefined'

        if numerator == 0:
            return '0'
        
        res = []
        a, b = numerator, denominator # a / b
        if not ((a > 0 and b > 0) or (a < 0 and b < 0)):
            res.append('-')

        a, b = abs(a), abs(b)
        q = a // b
        r = a % b
        res.append(str(q))
        if r:
            res.append('.')

        seen = {}
        while r != 0:
            seen[r] = len(res)
        
            a = r * 10
            q = a // b
            r = a % b
            res.append(str(q))
            if r in seen:
                res.insert(seen[r], '(')
                res.append(')')
                break

        return ''.join(res)