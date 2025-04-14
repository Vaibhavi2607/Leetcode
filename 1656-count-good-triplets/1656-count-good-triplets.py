class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        index = 0
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if abs(arr[i] - arr[j]) <= a:
                        if abs(arr[j] - arr[k]) <= b:
                            if abs(arr[i] - arr[k]) <= c:
                                index += 1
        return index
        