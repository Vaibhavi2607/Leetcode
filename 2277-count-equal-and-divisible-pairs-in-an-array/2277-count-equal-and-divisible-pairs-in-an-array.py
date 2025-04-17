class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if (i * j) % k == 0 and nums[i] == nums[j]:
                    count += 1
                    
        return count
        