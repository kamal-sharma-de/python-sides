def dfs(graph, start, visited=None):
  """
  Performs a Depth-First Search (DFS) on a graph starting from a given node.

  Args:
      graph (dict): A dictionary representing the graph, where keys are nodes and values are lists of connected nodes.
      start (int): The starting node for the DFS traversal.
      visited (set, optional): A set to keep track of visited nodes. Defaults to None.

  Returns:
      A list containing the nodes visited in the DFS order.
  """

  if visited is None:
    visited = set()  # Initialize visited set if not provided

  visited.add(start)
  for neighbor in graph[start]:
    if neighbor not in visited:
      dfs(graph, neighbor, visited)  # Recursive call for DFS on neighbors

  return visited


# Sample graph representation
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [],
    5: [],
}

# Perform DFS starting from node 0
visited_nodes = dfs(graph, 0)
print("DFS traversal from node 0:", visited_nodes)
