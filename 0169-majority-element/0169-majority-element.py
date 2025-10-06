class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = Counter(nums)
        return max(res, key=res.get)
        