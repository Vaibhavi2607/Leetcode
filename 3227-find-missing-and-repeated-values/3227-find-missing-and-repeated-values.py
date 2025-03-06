class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l: int = len(grid)
        size: int = l * l
        freq: List[int] = [0] * (size + 1)
        repeat: int = -1
        missed: int = -1

        for row in grid:
            for num in row:
                freq[num] += 1

        for num in range(1, size + 1):
            if freq[num] == 2:
                repeat = num
            if freq[num] == 0:
                missed = num

        return [repeat, missed]