from typing import List
from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create an adjacency list to represent the graph
        graph = defaultdict(set)  # Dictionary where each key (node) maps to a set of its neighbors
        
        for u, v in edges:
            graph[u].add(v)  # Add edge from u to v
            graph[v].add(u)  # Add edge from v to u (undirected graph)

        visited = set()  # Set to keep track of visited nodes
        complete_components = 0  # Counter for complete connected components

        def dfs(node, component):
            """
            Depth-First Search (DFS) function to traverse the graph.
            It finds all nodes in the current component and adds them to `component`.
            """
            stack = [node]  # Initialize stack with the starting node
            while stack:
                curr = stack.pop()  # Pop a node from the stack
                if curr not in visited:  # If the node is unvisited, process it
                    visited.add(curr)  # Mark as visited
                    component.add(curr)  # Add to the current component
                    stack.extend(graph[curr] - visited)  # Push unvisited neighbors onto the stack

        # Iterate through all nodes from 0 to n-1
        for node in range(n):
            if node not in visited:  # If the node is unvisited, start a new DFS traversal
                component = set()  # Set to store nodes in this connected component
                dfs(node, component)  # Perform DFS to gather all nodes in the component
                
                # Check if the component is complete
                size = len(component)  # Number of nodes in the component
                if all(len(graph[v]) == size - 1 for v in component):  
                    # A component is complete if each node has exactly (size-1) connections
                    complete_components += 1  # Increase the count of complete components

        return complete_components  # Return the total count of complete connected components

