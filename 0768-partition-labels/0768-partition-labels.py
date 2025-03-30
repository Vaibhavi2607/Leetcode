from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        P = [-1] * 26  # Stores the last occurrence of each character
        
        # Step 1: Record last occurrence of each character
        for i, c in enumerate(s):
            P[ord(c) - 97] = i
        
        pLen = []
        start, end = 0, -1
        
        # Step 2: Determine partitions
        for i, c in enumerate(s):
            end = max(end, P[ord(c) - 97])  # Update end boundary
            if i == end:  # If we reach the boundary, make a cut
                pLen.append(end - start + 1)
                start = i + 1
        
        return pLen