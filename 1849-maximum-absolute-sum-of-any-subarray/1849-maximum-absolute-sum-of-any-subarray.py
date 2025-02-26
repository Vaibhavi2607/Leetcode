class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minsum = 0
        maxsum = 0
        prefix = 0

        for i in range(0, len(nums)):
            prefix += nums[i]
            minsum = min(minsum, prefix)
            maxsum = max(maxsum, prefix)

        return maxsum - minsum
        