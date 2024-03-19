class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row
        m, n = len(matrix), len(matrix[0])
        
        low, high = 0, m
        row = 0
        while low <= high:
            med = low + (high - low)//2
            
            if matrix[med][0] > target:
                if med > 0:
                    high = med - 1
                    continue
                else:
                    row = -1
                    break
            if matrix[med][0] < target:
                if matrix[med][-1] >= target:
                    row = med
                    break
                if med < m-1:
                    low = med + 1
                    continue
                else:
                    row = -1
                    break
            return True
                    
        if row == -1 or target > matrix[row][-1] or target < matrix[row][0]:
            return False
        low, high = 0, n - 1
        while low <= high:
            med = low + (high - low)//2
            
            if matrix[row][med] == target:
                return True
            
            if matrix[row][med] > target:
                high = med - 1
            
            else:
                low = med + 1
        
        return False
        
                
    