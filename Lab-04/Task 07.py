#Taking input____________________________________________________________________________
import queue
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#Taking Input Ends Here__________________________________________________________________

#Main Code Starts Frome Here_____________________________________________________________
   from collections import deque
   def bfs(start, N, adj):
       visited = [-1] * (N + 1)  # Distance from start
       queue = deque()
       queue.append(start)
       visited[start] = 0
       farthest_node = start
       max_distance = 0
       while queue:
            u = queue.popleft()
            for v in adj[u]:
                if visited[v] == -1:
                    visited[v] = visited[u] + 1
                    queue.append(v)
                    if visited[v] > max_distance:
                        max_distance = visited[v]
                        farthest_node = v
       return farthest_node, max_distance
  def find_diameter(N, adj):
       X, val = bfs(1, N, adj)
       Y, diameter = bfs(X, N, adj)
       return X, Y
#Main Code Ends Here_____________________________________________________________________

