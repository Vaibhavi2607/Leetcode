class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        req = Counter()
        for word in words2:
            freq = Counter(word)
            for char, count in freq.items():
                req[char] = max(req[char], count)
        
        result = []
        for word in words1:
            freq = Counter(word)
            if all(freq[char] >= req[char] for char in req):
                result.append(word)

        return result
        
        