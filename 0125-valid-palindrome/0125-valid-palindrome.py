class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = [c.lower() for c in s if c.isalnum()]
        if len(s) == 1:
            return True
            
        start = 0
        end = len(string) - 1

        while start < end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        return True


        