class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0
        preflen = len(pref)
        for word in words:
            if len(word) >= preflen:
                if word[:preflen] == pref:
                    count += 1
        return count
        