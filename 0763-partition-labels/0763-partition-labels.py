class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # count the last occurrence
        
        # split to new if last occurrence is the curr
        
        charLastDict = defaultdict(int)
        for i, c in enumerate(s):
            charLastDict[c] = i
        
        res = []
        st, e = 0, 0
        for i, c in enumerate(s):
            e = max(e, charLastDict[c])
            if i == e:
                res.append(e - st + 1)
                st = i+1
        
        return res
            
            