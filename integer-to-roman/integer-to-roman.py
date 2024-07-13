class Solution:
    def intToRoman(self, num: int) -> str:
        
        roman = {
            1: ['I', 'X', 'C', 'M'],
            2: ['II', 'XX', 'CC', 'MM'],
            3: ['III', 'XXX', 'CCC', 'MMM'],
            4: ['IV', 'XL', 'CD'],
            5: ['V', 'L', 'D'],
            6: ['VI', 'LX', 'DC'],
            7: ['VII', 'LXX', 'DCC'],
            8: ['VIII', 'LXXX', 'DCCC'],
            9: ['IX', 'XC', 'CM']
        }
        
        resList = []
        divisor = 1000
        count = 3
        while divisor and num:
            if num >= divisor:
                val = num // divisor
                resList.append(roman[val][count])
                num %= divisor
            divisor /= 10
            count -= 1
        
        return ''.join(resList)
            