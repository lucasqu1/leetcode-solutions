class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        explored_neighbors = {}

        if not node:
            return None

        def dfs(curr_node):
            if curr_node in explored_neighbors:
                return explored_neighbors[curr_node]

            neighbors = []

            explored_neighbors[curr_node] = Node(curr_node.val, neighbors)

            for neighbor in curr_node.neighbors:
                neighbors.append(dfs(neighbor))

            return explored_neighbors[curr_node]

        return dfs(node)

'''
Keep track of a mapping from original nodes to new nodes.

Results in us not attempting to continue a search in the graph if we've seen the node before. 

Assuming the graph is connected, this allows us to clone the whole graph.

Pitfalls: Need to return something in all cases, when I previously did this question
I hadn't returned a value in the case where we hadn't seen the node before. Results in 
unexpected behavior
'''
