class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        group_sizes = defaultdict(lambda: 0)

        for num in nums:
            curr = group_sizes[num - k]
            group_sizes.pop(num - k)
            group_sizes[num] = curr + 1
        
        def fib(x):
            phi = (1 + 5**0.5)/2
            fib_x = (phi**x - (1-phi)**x) / 5**0.5
            return round(fib_x)
        
        sizes = group_sizes.values()
        res = 1
        for size in sizes:
            res *= fib(size + 2)
        
        return res