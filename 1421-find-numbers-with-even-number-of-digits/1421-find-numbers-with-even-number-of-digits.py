class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for i in nums:
            if self.countDigits(i) % 2 == 0:
                count += 1
        return count

    def countDigits(self, x):
        cnt = 0
        while x > 0:
            x //= 10
            cnt += 1
        return cnt