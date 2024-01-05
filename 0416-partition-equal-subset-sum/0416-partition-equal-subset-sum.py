class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        
        target = s // 2
        possSums = set()
        possSums.add(0)
        
        for num in nums:
            tempSet = set()
            for s in possSums:
                if s+num == target:
                    return True
                tempSet.add(s)
                tempSet.add(s+num)
            possSums = tempSet
        
        return False
        