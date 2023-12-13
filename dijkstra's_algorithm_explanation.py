
# ! Just an explanation page. No working code!
# dijkstras algorithm finds the shortest paths from a starting node to all other nodes in a graph  
# with non-negative edge weights.

#* 1
# Create a dictionary to store the shortest distances from the start node to each node. the starting node should be set to 0 and all distances to infinity.
def dijkstra(graph, start):
        distances = {node: float('infinity') for node in graph}
        distances[start] = 0
#* 1
# create a priorirty queue to keep track of nodes and their tentative distances and init it with the starting node and its distance.
        priority_queue = [(0, start)]
#* 1
# While there are nodes in the 'priority_queue':
#  pop the node with the smallest tentative distance from the priority queue

#* 1
# For each neighbor of the current node, calculate the total distance from the start node to the neighbor through the current node.
#  If the total distance is less than the recorded distance to the neighbor, then update the recorded distsance to the neighbor and adds the neighbor and it supdated distance to the priority queue.
#* 1
# 
#* 1
# 
#* 1
# 
#* 1
# 
#* 1
# 
#* 1
# 
#* 1
# 









