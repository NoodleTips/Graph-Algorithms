
# ! Just an explanation page. No working code!

# DFS explores as far as possible along each branch before backtracking.
# It uses a "stack" to keept rack of the nodes to visit next.

# * 1. start at an initial node.
def dfs(graph, start, visited=None):


# * 2. Mark the node as visited.
if visited is None: # checks if the node was initially visited
    visited = set() # initializes the list of visited nodes
visited.add(start)  # marks the starting node as visited.
print(start, end='') # prints the current node in the traversal


# * 3. Explore an adjacent unvisited node.
for neighbor in graph[start]: # Loop through the neighboring nodes
    if neighbor not in visited: # Check if the neighbor is already visited
        dfs(graph, neighbor, visited) # Recursively calls the dfs function for the unvisited neighbors


# * 4. Repeat steps 2-3 until there are no more unvisited nodes.
# * 5. Backtrack if necessary.













