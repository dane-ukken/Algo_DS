class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitDict = defaultdict()
        res = 1
        l, r = 0, 0

        while r < len(fruits):
            fruitDict[fruits[r]] = r
            while len(fruitDict) > 2:
                curr = fruits[l]
                if fruitDict[curr] == l:
                    fruitDict.pop(curr)
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        
        return res
