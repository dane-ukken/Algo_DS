class Solution:
    def numberOfWays(self, s: str) -> int:
        
        
        z, o, zo, oz, total = 0, 0, 0, 0, 0
        for c in s:
            if c == '1':
                total += oz
                zo += z
                o += 1
            elif c == '0':
                total += zo
                oz += o
                z += 1
        return total
        
        """
        clusters = [1]
        res = 0
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                clusters[-1] += 1
            else:
                clusters.append(1)
                
        n = len(clusters)
        for i in range(n):
            for j in range(i+1, n, 2):
                for k in range(j+1, n, 2):
                    res += clusters[i]*clusters[j]*clusters[k]
        return res
        
        """