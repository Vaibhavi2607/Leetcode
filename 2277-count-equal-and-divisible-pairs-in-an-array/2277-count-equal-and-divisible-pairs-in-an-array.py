class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ideal_pairs = 0
        n = len(nums)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if (i * j) % k == 0 and nums[i] == nums[j]:
                    ideal_pairs += 1
                    
        return ideal_pairs
        