class Solution(object):
    def canConstruct(self, s, k):
        if len(s) < k:
            return False
        
        freq = Counter(s)

        odd_count = sum(1 for count in freq.values() if count%2==1)

        return odd_count <= k