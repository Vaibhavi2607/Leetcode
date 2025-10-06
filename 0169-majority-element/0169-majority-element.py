class Solution(object):
    def majorityElement(self, nums):
    
        res = Counter(nums)
        return max(res, key=res.get)
        