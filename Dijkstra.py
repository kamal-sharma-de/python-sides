class Node:
  def __init__(self, name):
    self.name = name
    self.neighbors = []  # List of connected nodes and their weights
    self.visited = False
    self.distance = float('inf')  # Initialize distance as infinity

class Graph:
  def __init__(self):
    self.nodes = {}

  def add_node(self, name):
    if name not in self.nodes:
      self.nodes[name] = Node(name)

  def add_edge(self, source, dest, weight):
    if source not in self.nodes:
      self.add_node(source)
    if dest not in self.nodes:
      self.add_node(dest)
    self.nodes[source].neighbors.append((self.nodes[dest], weight))

  def dijkstras_algorithm(self, start_node):
    self.nodes[start_node].distance = 0  # Set starting node distance to 0

    # Use a priority queue to efficiently process nodes based on distance
    priority_queue = [(0, self.nodes[start_node])]  # (distance, node)

    while priority_queue:
      current_distance, current_node = heapq.heappop(priority_queue)

      # Already processed this node with a shorter distance
      if current_node.visited:
        continue

      current_node.visited = True

      for neighbor, weight in current_node.neighbors:
        new_distance = current_distance + weight
        if new_distance < neighbor.distance:
          neighbor.distance = new_distance
          heapq.heappush(priority_queue, (new_distance, neighbor))

    # Print shortest distances to all nodes from the starting node
    print("Shortest distances from", start_node)
    for node in self.nodes.values():
      print(node.name, ":", node.distance if node.distance != float('inf') else "unreachable")

# Example usage
graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")

graph.add_edge("A", "B", 5)
graph.add_edge("A", "C", 3)
graph.add_edge("B", "D", 2)
graph.add_edge("C", "D", 1)
graph.add_edge("C", "E", 4)
graph.add_edge("D", "E", 8)

graph.dijkstras_algorithm("A")  # Find shortest paths from node A
