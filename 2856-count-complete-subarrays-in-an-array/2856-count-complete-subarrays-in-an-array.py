class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_unique = len(set(nums))
        count = 0
        n = len(nums)

        for i in range(n):
            frequency = set()
            for j in range(i, n):
                frequency.add(nums[j])
                if len(frequency) == total_unique:
                    count += 1
        return count