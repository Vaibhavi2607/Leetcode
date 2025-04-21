class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        sum, maximum, minimum = 0, 0, 0
        for x in differences:
            sum += x
            maximum = max(maximum, sum)
            minimum = min(minimum, sum)
        return max(0, upper - lower - maximum + minimum + 1)