#Taking input____________________________________________________________________________
import queue
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#Taking Input Ends Here__________________________________________________________________

#Main Code Starts Frome Here_____________________________________________________________
    from collections import deque, defaultdict
    def bfs(start, graph, visited):
        queue = deque([start])
        visited[start] = 0
        count = [1, 0]

        while queue:
            node = queue.popleft()
            current_faction = visited[node]
        
            for neighbor in graph[node]:
                if visited[neighbor] == -1:  # Not visited yet
                    visited[neighbor] = 1 - current_faction  # Assign opposite faction
                    count[visited[neighbor]] += 1
                    queue.append(neighbor)
        return max(count)

#Main Code Ends Here_____________________________________________________________________
