
# ! Just an explanation page. No working code!

# BFS explores all nodes at the current depth prior to moving on to nodes at the next depth.
# It uses a queue to keep track of the ndoes visited.

# *1. Start at the initial node
def bfs(graph, start): # define the bfs function that takes a graph and a starting node.
# *2. Mark the node as visited.
visited = set() # initialize a set to keep track of the visited nodes.
queue = deque([start]) # initialize deque witht he starting node.
visited.add(start) # mark the starting node as visited.
# *3. Enqueue the node.
while queue:
# *4. Dequeue the node and explore unvisited neighbors.
node = queue.popleft()
print(node, end='') # prints the current node for the traversal.

for neighbor in graph[node]:
    if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)
# *5. Repeat steps 2-4 until the queue is empty.











