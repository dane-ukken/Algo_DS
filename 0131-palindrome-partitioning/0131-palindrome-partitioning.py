class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        currSplit = []
        
        def backtracking(i):
            if i >= len(s):
                res.append(currSplit[:])
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    currSplit.append(s[i:j+1])
                    backtracking(j+1)
                    currSplit.pop()
            
        
        backtracking(0)
        return res
    
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True