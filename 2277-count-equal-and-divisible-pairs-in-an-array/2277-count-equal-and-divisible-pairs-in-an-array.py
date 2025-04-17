class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        index = 0
        n = len(nums)
        count1 = 0

        for i in range(n - 1):
            for j in range(n):
                if (i * j) % k == 0:
                    if i < j < n and nums[i] == nums[j]:
                        count += 1
                    
        return count
        