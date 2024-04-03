class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = False
        
        if len(a) < len(b):
            a, b = b, a
            
        res = [0]*(len(a)+1)
        i = -1
        while len(b) >= -i:
            curr = '0'
            if a[i] == '1' and b[i] == '1':
                if carry:
                    curr = '1'
                else:
                    carry = True
            elif a[i] == '1':
                if carry:
                    carry = True
                else:
                    curr = '1'
            elif b[i] == '1':
                if carry:
                    carry = True
                else:
                    curr = '1'
            else:
                if carry:
                    curr = '1'
                carry = False
            res[i] = curr
            i -= 1
            
        while len(a) >= -i:
            curr = '0'
            if a[i] == '1' and not carry:
                curr = '1'
            elif a[i] == '0' and carry:
                curr = '1'
                carry = False
            res[i] = curr
            i -= 1
        
        if carry:
            res[i] = '1'
        else:
            res = res[1:]
            
        return ''.join(res)