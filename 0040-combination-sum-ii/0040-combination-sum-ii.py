class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort(reverse=True)
        
        def backtracking(i, currSum, curr):
            if currSum == target:
                res.append(curr[:])
                return
            if i == len(candidates) or currSum > target:
                return
            
            curr.append(candidates[i])
            currSum += candidates[i]
            backtracking(i+1, currSum, curr[:])
            curr.pop()
            currSum -= candidates[i]
            
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtracking(i+1, currSum, curr[:])
        
        backtracking(0, 0, [])
        return res