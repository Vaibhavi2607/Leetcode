from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        # Step 1: Collect all indices where nums[i] == key
        key_indices = [i for i, val in enumerate(nums) if val == key]

        result = []  # Step 2: Initialize result list

        # Step 2: Loop through each index of the array
        for i in range(len(nums)):
            # Step 2: Check if i is within distance k from any key index
            for j in key_indices:
                if abs(i - j) <= k:
                    result.append(i)  # Valid index found, add to result
                    break  # No need to check other key indices for this i

        # Step 3: Return the result list
        return result