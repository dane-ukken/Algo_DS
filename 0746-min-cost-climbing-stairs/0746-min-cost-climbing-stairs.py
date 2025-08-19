class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = cost[0], cost[1]
        cost.append(0)

        for i in range(2, len(cost)):
            temp = cost[i] + min(first, second)
            first = second
            second = temp  

        return second
