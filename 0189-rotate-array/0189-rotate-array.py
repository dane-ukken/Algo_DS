class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            currentIdx, prev = start, nums[start]
            while True:
                next_idx = (currentIdx + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                currentIdx = next_idx
                count += 1

                if start == currentIdx:
                    break
            start += 1