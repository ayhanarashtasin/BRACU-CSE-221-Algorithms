#Taking input____________________________________________________________________________
import queue
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#Taking Input Ends Here__________________________________________________________________


#Main Code Starts Frome Here_____________________________________________________________
import heapq
from collections import defaultdict, deque
def lexicographically_smallest_toposort(N, M, prerequisites):
    graph = defaultdict(list)
    in_degree = {i: 0 for i in range(1, N + 1)}
    for A, B in prerequisites:
        graph[A].append(B)
        in_degree[B] += 1
    min_heap = []
    for course in range(1, N + 1):
        if in_degree[course] == 0:
            heapq.heappush(min_heap, course)
    topo_order = []
    while min_heap:
        course = heapq.heappop(min_heap
        topo_order.append(course)
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(min_heap, neighbor)
    if len(topo_order) != N:
        return "IMPOSSIBLE"
    return " ".join(map(str, topo_order))
