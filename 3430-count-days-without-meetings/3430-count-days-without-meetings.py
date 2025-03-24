class Solution:
    def countDays(self, n: int, a: List[List[int]]) -> int:
        res, E = 0, 0
        for s,e in sorted(a)+[[n+1]*2]:
            res += max(0,s-E-1)
            E = max(E,e)
        
        return res