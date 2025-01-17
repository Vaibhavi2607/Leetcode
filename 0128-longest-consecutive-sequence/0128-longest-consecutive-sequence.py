class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:  # Iterate over the set directly
            # Only start counting if n-1 is not in the set (i.e., n is the start of a sequence)
            if (n - 1) not in num_set:
                length = 1
                current = n
                # Count the length of the consecutive sequence starting from n
                while (current + 1) in num_set:
                    current += 1
                    length += 1
                longest = max(longest, length)

        return longest