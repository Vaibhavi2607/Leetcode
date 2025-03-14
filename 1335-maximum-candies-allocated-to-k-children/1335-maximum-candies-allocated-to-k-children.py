class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def dp(mid , k):
            for i in candies:
                k -= i // mid
                if k <= 0:
                    return True
            return False

        l, r = 0, sum(candies) // k
        while l < r:
            mid = (l+r+1) // 2
            if dp(mid, k):
                l = mid
            else:
                r = mid - 1
        return l