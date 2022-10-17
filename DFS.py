def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'1': set(['2', '3', '5']), 
         '2': set(['1', '3', '4']), 
         '3': set(['1', '2','4','5']), 
         '4': set(['2', '3']), 
         '5': set(['1', '3'])}

dfs(graph, '1')
