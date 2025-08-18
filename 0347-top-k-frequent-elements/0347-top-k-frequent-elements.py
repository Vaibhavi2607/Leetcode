class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequents = {}
        for num in nums:
            if num in frequents:
                frequents[num] += 1
            else:
                frequents[num] = 1
        sorted_nums = sorted(frequents, key=frequents.get, reverse=True)
        return sorted_nums[:k]

    



              