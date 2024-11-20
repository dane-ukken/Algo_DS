class Solution:
    def numSteps(self, s: str) -> int:
        '''
        11010100
        1110
        111
        1000
        '''

        res = 0

        while s != '1':
            print(s)
            res += 1

            if s[-1] == '0':
                s = s[:-1]
                
            else:
                newS = ''
                carry = 1

                for i in range(len(s) - 1, -1, -1):
                    if carry == 0:
                        newS = s[i] + newS
                        continue
                    if s[i] == '0':
                        carry = 0
                        newS = '1' + newS
                    elif s[i] == '1':
                        newS = '0' + newS
                
                if carry == 1:
                    newS = '1' + newS
            
                s = newS
        
        return res



