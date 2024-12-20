#Taking input____________________________________________________________________________
import queue
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#Taking Input Ends Here__________________________________________________________________

#Main Code Starts Frome Here_____________________________________________________________
    def BFS(adj_list,end):
      n = len(adj_list)
      distance = [float("inf")]*(n)
      parent = [-1]*n
      queue = []
      distance[1]=0
      queue.append(1)
      while queue:
        node = queue.pop(0)
        for i in adj_list[node]:
          if distance[node]+1<distance[i]:
            distance[i] = distance[node]+1
            parent[i] = node
            queue.append(i)
      path = []
      current = end
      while current!=-1:
        path.append(current)
        current  = parent[current]
      path.reverse()
      return f"Time : {distance[end]}\n Shortest Path : {" ".join(map(str, path))}"
      
#Main Code Ends Here_____________________________________________________________________
    
#Drive Code Which I Made_________________________________________________________________
    def representation(V , edges,end):
      adj_list = [[]*V for i in range(V)]
      for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        adj_list[u].append(v)
        adj_list[v].append(u)
      out_f.write(f"{(BFS(adj_list,end))}")
    arr = []
    for i in read:
      temp = list(map(int,i.split()))
      arr.append(temp)
    representation(arr[0][0]+1,arr[1:len(arr)-1],arr[0][2])
#Driver Code Ends Here____________________________________________________________________
