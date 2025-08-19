class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = cost[0], cost[1]
        cost.append(0)

        for i in range(2, len(cost)):
            first, second = second, cost[i] + min(first, second)

        return second
