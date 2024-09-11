class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # 5 -> 5%2 + (5//2)%2 * 10 + ((5//2) // 2) % 2 * 100 = 101
        def get_binary(num):
            mul = 1
            res = 0
            while num:
                res = (num % 2) * mul + res
                num = num // 2
                mul = mul * 10
            return res
                
        start_bin, goal_bin = get_binary(start), get_binary(goal)
        
        def get_bit_difference(a, b):
            if a < b:
                a, b = b, a
            res = 0
            while a:
                if a % 10 != b % 10:
                    res += 1
                a = a // 10
                b = b // 10
            return res
    
        return get_bit_difference(start_bin, goal_bin)
        
            
            
            
            