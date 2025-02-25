class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 1000000007
        odd = 0 
        even = 1
        result = 0
        summ = 0

        for num in arr:
            summ += num
            if summ % 2 == 1:
                result = (result + even) % mod
                odd += 1
            else:
                result = (result + odd) % mod
                even += 1
        return result