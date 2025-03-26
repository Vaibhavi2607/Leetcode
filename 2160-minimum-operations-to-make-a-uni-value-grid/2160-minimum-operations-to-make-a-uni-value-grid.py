from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        """
        Find the minimum number of operations to make all elements in the grid equal.
        
        Parameters:
            grid (List[List[int]]): 2D list of integers
            x (int): Allowed increment/decrement value
        
        Returns:
            int: Minimum number of operations or -1 if impossible
        """
        # Flatten the grid into a single list
        values = [num for row in grid for num in row]
        
        # Check if all numbers have the same remainder when divided by x
        remainder = values[0] % x
        for num in values:
            if num % x != remainder:
                return -1  # Not possible
        
        # Sort the values to find the median
        values.sort()
        median = values[len(values) // 2]  # Median minimizes the sum of absolute differences

        # Calculate the total number of operations to make all values equal to the median
        return sum(abs(num - median) // x for num in values)
