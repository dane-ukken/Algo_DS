class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        tarSet = Counter()
        res = 0
        
        for n4 in nums4:
            for n3 in nums3:
                tarSet[-n4-n3] += 1
            
        for n1 in nums1:
            for n2 in nums2:
                res += tarSet[n1+n2]
        
        return res