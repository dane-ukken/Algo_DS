class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        sumDict = {}
        
        for i in range(len(nums)):
            sumDict[nums[i]] = i

        for i in range(len(nums)):
            if (sumDict.get(target - nums[i]) is not None) and (sumDict[target-nums[i]] is not i):
                result.append(i)
                result.append(sumDict[target-nums[i]])
                break

        return result