class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        difference = []
        max_element = abs(nums[0] - nums[-1])
        difference.append(max_element)
        for i in range(len(nums)):
            
            diff = abs(nums[i] - nums[i-1])
            max_element = max(max_element, diff)
        return max_element

        