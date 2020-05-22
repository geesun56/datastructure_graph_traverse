def bfs(graph, s):
    start = graph.vertices[s]
    level = {}
    
    j = 0
    frontier = [start]

    while len(level) != graph.vertex_number:
        times = len(frontier)
        for i in range(times):
            current_vt = frontier.pop(0)
            if not current_vt.value in level:
                level[current_vt.value] = j
            for vt in current_vt.adjacent:
                if not vt.value in level:
                    frontier.append(vt)
            j += 1
            print(current_vt.value)

def dfs(graph, s):
    start = graph.vertices[s]
    check = {}
    
    frontier = [start]

    while len(check) != graph.vertex_number:
        
        while len(frontier):
            current_vt = frontier.pop()
            if not current_vt.value in check:
                check[current_vt.value] = 1
            for vt in reversed(current_vt.adjacent):
                if not vt.value in check:
                    frontier.append(vt)
            print(current_vt.value)



