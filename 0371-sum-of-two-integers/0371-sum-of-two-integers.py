class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 4 + 3
        # 100 + 11 = 111
        
        # 5 + 7
        # 101 + 111 = 1100
        
        # res = res | (r_bit << i)
        # a_bit = (a >> i)
        # b_bit = (b >> i)
        # r_bit = a_bit ^ b_bit ^ carry 
        
        # if a_bit == 1 and b_bit == 1 or b_bit == 1 and carry == 1 or a_bit == 1 and carry == 1: carry = 1
        mask = 0xffffffff
        while b:
            temp = (a ^ b) & mask
            b = ((a & b) << 1) & mask
            a = temp

        if a > mask // 2:
            return ~(a ^ mask)
        else:
            return a
        """
        carry = 0
        res = 0
        a_bit = a % 2
        b_bit = b % 2
        if a_bit == 1 and b_bit == 1:
            carry = 1
        for i in range(1, 32):
            if (a == 0) and (b==0) and (carry == 0):
                break
            r_bit = a_bit ^ b_bit ^ carry
            res = res | (r_bit << i-1)
            a_bit = (a >> i)
            b_bit = (b >> i)
            print(a_bit, b_bit, carry, r_bit, res)
            if (a_bit == 1 and b_bit == 1) or (b_bit == 1 and carry == 1) or (a_bit == 1 and carry == 1): 
                carry = 1
            else:
                carry = 0
            b = b >> 1
            a = a >> 1
        
        return res
        """