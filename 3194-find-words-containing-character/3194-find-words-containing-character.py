class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        count = []
        for i in range(len(words)):
            for char in words[i]:
                if char == x:
                    count.append(i)
                    break
        return count
        
                    

        