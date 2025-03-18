class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxlength = 1

        left = 0
        visited = 0
        
        for right in range(n):
            while visited & nums[right] != 0:
                visited ^= nums[left]
                left += 1

            visited |= nums[right]

            maxlength = max(maxlength, right - left + 1)

        return maxlength
        