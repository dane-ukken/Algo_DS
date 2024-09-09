# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        matrix = [[-1 for j in range(n)] for i in range(m)]
        borders = [[0, n-1], [m-1, n-1], [m-1, 0], [1, 0]]
        countX, countY = n, m-1
        x, y = 0, 0
        d = 0
        
        i, j = 0, 0
        while (0 <= i < m) and (0 <= j < n) and matrix[i][j] == -1 and head:
            matrix[i][j] = head.val
            head = head.next
            if d % 2 == 0:
                x += 1
                if x == countX:
                    d = (d + 1) % 4
                    countX -= 1
                    x = 0
            else:
                y += 1
                if y == countY:
                    d = (d + 1) % 4
                    countY -= 1
                    y = 0
            
            dx, dy = directions[d]
            i, j = i + dx, j + dy
            
            
        
        
        return matrix