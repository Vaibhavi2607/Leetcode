class Solution:
    def maximumCount(self, nums):
        neg = 0
        for i in nums:
            if i < 0:
                neg += 1
            else:
                break 
        pos = len(nums) - neg - nums.count(0)
        return max(neg, pos)
