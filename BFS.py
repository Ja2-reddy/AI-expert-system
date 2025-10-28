from collections import deque

# Function to perform BFS traversal
def bfs(graph, start):
    visited = set()          # To keep track of visited nodes
    queue = deque([start])   # Initialize queue with the start node
    
    print("BFS Traversal Order:")
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting node
start_node = 'A'
bfs(graph, start_node)
