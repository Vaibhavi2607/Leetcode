class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        i = 2
        for j in range(2, n):
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i+=1

        return i
        
        