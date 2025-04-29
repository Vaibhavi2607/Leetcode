class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < k:
            return 0
        M = max(nums)
        positions = [i for i, x in enumerate(nums) if x == M]
        t = len(positions)
        if t < k:
            return 0
        res = 0
        for i in range(k - 1, t):
            start = positions[i - k + 1]
            prev = positions[i - k] if i - k >= 0 else -1
            left_options = start - prev
            right_options = n - positions[i]
            res += left_options * right_options
        return res