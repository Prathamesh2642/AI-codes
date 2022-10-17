def bfs(graph, source):
    visited = set() 
    bfs_traversal = list()
    queue = list()
    
    queue.append(source)
    visited.add(source)
    
    while queue:
        current_node = queue.pop(0)
        bfs_traversal.append(current_node)
        
        for neighbour_node in graph[current_node]:
            if neighbour_node not in visited:
                visited.add(neighbour_node)
                queue.append(neighbour_node)
    return bfs_traversal

graph = {
    '1': ['2', '3', '5'], 
    '2': ['1', '3', '4'], 
    '3': ['1', '2','4','5'], 
    '4': ['2', '3'], 
    '5': ['1', '3']
}

bfs_traversal = bfs(graph, '1')
print(f"BFS: {bfs_traversal}")
