class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        half = total//2
        
        if n1 > n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
        
        l, r = 0, n1 - 1
        print(nums1, nums2, n1, n2)
        while True:
            i = (l+r) // 2
            j = half - (i+1) - 1
            
            aLeft = nums1[i] if i >= 0 else float('-infinity')
            bLeft = nums2[j] if j >= 0 else float('-infinity')
            aRight = nums1[i+1] if (i+1) < n1 else float('infinity')
            bRight = nums2[j+1] if (j+1) < n2 else float('infinity')
            if aLeft <= bRight and bLeft <= aRight:
                if total % 2 == 0:
                    return (max(aLeft, bLeft) + min(aRight, bRight))/2
                else:
                    return min(aRight, bRight)
            elif aLeft > bRight:
                r = i-1
            else:
                l = i+1
        
        print("error")
        