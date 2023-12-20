class Solution:
    def rob(self, nums: List[int]) -> int:
        s1, s2 = 0, 0
        
        for n in nums:
            temp = max(n+s1, s2)
            s1 = s2
            s2 = temp
        
        return s2
        
        