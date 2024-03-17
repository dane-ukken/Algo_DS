class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        smallLimits = ((0, 2), (3, 5), (6, 8))
        
        #row and col wise
        for i in range(9):
            rowNumCount = defaultdict(lambda: 0)
            colNumCount = defaultdict(lambda: 0)
            for j in range(9):
                ele = board[i][j]
                if ele != ".":
                    rowNumCount[ele] += 1
                    if rowNumCount[ele] > 1:
                        return False
                
                ele = board[j][i]
                if ele != ".":
                    colNumCount[ele] += 1
                    if colNumCount[ele] > 1:
                        return False
                    
        for iStart, iEnd in smallLimits:
            for jStart, jEnd in smallLimits:
                numCount = defaultdict(lambda: 0)
                for i in range(iStart, iEnd+1):
                    for j in range(jStart, jEnd+1):
                        ele = board[i][j]
                        if ele ==".":
                            continue
                        numCount[ele] += 1
                        if numCount[ele] > 1:
                            return False
        
        return True
        
        
        
        