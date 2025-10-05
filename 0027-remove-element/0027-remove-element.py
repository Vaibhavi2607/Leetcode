class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for x in nums:
            if x != val:
                nums[index] = x
                index += 1
        return index