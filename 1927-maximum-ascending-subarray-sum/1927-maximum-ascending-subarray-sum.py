class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = nums[0]
        max_sum = current_sum

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]
            
            max_sum = max(max_sum, current_sum)
        
        return max_sum
        