class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        rev = 0
        temp = x

        while temp != 0:
            rev = rev*10 + temp%10
            temp = temp//10
        
        return rev==x
        