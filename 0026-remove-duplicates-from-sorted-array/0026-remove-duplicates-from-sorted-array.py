class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        front = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[front]:
                front += 1
                nums[front] = nums[i]
        return front + 1

        
        