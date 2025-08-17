class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        if len(nums) == 1:
            return False

        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                return True

        return False
        