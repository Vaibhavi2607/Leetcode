class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        for i in range(len(s)):
            seen = set()
            current_len = 0
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                current_len += 1
                max_len = max(max_len, current_len)
        return max_len