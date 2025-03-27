from collections import Counter
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Step 1: Find the dominant element in the entire array
        candidate, count = None, 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        
        # Verify the candidate is actually dominant
        total_count = nums.count(candidate)
        if total_count * 2 <= len(nums):
            return -1  # No valid split possible
        
        # Step 2: Find the minimum valid index for the split
        left_count = 0  # Count of dominant element in left part
        for i in range(len(nums)):
            if nums[i] == candidate:
                left_count += 1
            
            left_size = i + 1  # Size of left partition
            right_size = len(nums) - left_size  # Size of right partition
            
            if left_count * 2 > left_size and (total_count - left_count) * 2 > right_size:
                return i  # First valid split found
        
        return -1  # No valid split
