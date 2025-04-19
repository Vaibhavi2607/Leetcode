from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n):
            # We want nums[j] such that:
            # lower - nums[i] <= nums[j] <= upper - nums[i]
            left = bisect_left(nums, lower - nums[i], i + 1, n)
            right = bisect_right(nums, upper - nums[i], i + 1, n)
            count += right - left

        return count
