class Solution:
    def maximumCount(self, nums):
        # Find the count of negative numbers
        neg_count = 0
        for num in nums:
            if num < 0:
                neg_count += 1
            else:
                break  # Stop when we hit a non-negative number
        
        # The count of positive numbers is the total length of nums minus the number of negative numbers and zeros
        pos_count = len(nums) - neg_count - nums.count(0)
        
        # Return the maximum of the positive and negative counts
        return max(neg_count, pos_count)
