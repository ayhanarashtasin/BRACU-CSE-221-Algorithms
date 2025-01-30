#Taking input____________________________________________________________________________
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#Taking Input Ends Here__________________________________________________________________

#Main Code Starts Frome Here_____________________________________________________________
from collections import defaultdict
def kosaraju_scc(N, edges):
    # Step 1: Build Graph and Reverse Graph
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        reverse_graph[v].append(u)
    def dfs1(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs1(neighbor)
        stack.append(node)
    def dfs2(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in reverse_graph[node]:
            if neighbor not in visited:
                dfs2(neighbor, component)
    stack = []
    visited = set()
    for node in range(1, N + 1):
        if node not in visited:
            dfs1(node)
    visited.clear()
    scc_list = []
    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs2(node, component)
            scc_list.append(sorted(component))
    for scc in sorted(scc_list):
        print(" ".join(map(str, scc)))
#Main Code Ends Here_____________________________________________________________________
