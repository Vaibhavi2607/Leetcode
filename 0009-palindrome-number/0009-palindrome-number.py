class Solution:
    def isPalindrome(self, x: int) -> bool:
        xs = str(x)
        return True if xs == xs[::-1] else False
        