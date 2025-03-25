class Solution:
    def isPossible(self, rectangles: List[List[int]], k: int) -> bool:
        rectangles.sort(key=lambda x: x[k])
        cuts = 0
        mx = rectangles[0][k + 2]  

        for rect in rectangles:
            b, e = rect[k], rect[k + 2]

            if mx <= b:
                cuts += 1

            mx = max(mx, e)

        return cuts >= 2
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        return self.isPossible(rectangles, 0) or self.isPossible(rectangles, 1)