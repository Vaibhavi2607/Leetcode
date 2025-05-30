class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def get_reachable(from_node):
            reachable = {}
            node = from_node
            distance = 0
            
            while node != -1 and node not in reachable:
                reachable[node] = distance
                distance += 1
                node = edges[node]
            
            return reachable
        
        r1 = get_reachable(node1)
        r2 = get_reachable(node2)
        
        common_nodes = set(r1.keys()) & set(r2.keys())
        
        if not common_nodes:
            return -1
        
        return min(common_nodes, key=lambda node: (max(r1[node], r2[node]), node))