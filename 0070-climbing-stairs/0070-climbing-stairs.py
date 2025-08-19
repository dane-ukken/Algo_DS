class Solution:
    def climbStairs(self, n: int) -> int:
        second, first = 0, 1

        for i in range(n-1, -1, -1):
            temp = first + second
            second = first
            first = temp

        return first
            