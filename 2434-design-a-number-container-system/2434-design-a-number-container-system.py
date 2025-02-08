from collections import defaultdict
from heapq import heappush, heappop

class NumberContainers:

    def __init__(self):
        self.mp = {}  # This will store the mapping from index to number.
        self.idx = defaultdict(list)  # This will store a heap for each number.

    def change(self, index: int, number: int) -> None:
        self.mp[index] = number  # Store the number at the given index.
        heappush(self.idx[number], index)  # Add the index to the heap for the given number.

    def find(self, number: int) -> int:
        if number not in self.idx:  # If no such number exists, return -1.
            return -1
        
        while self.idx[number]:  # While there are indices for this number.
            i = self.idx[number][0]  # Peek at the smallest index in the heap.
            if self.mp[i] == number:  # If the number matches, return the index.
                return i
            heappop(self.idx[number])  # If the index is outdated, pop it from the heap.
        
        return -1  # If no valid index is found, return -1.
