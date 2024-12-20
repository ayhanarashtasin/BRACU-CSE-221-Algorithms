#Taking input____________________________________________________________________________
import queue
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#Taking Input Ends Here__________________________________________________________________

#Main Code Starts Frome Here_____________________________________________________________
    def BFS(adj_list):
      n = len(adj_list)
      visited = [0]*n
      visited[0]=1
      queue = []
      queue.append(1)
      output = []
      while queue:
        node = queue.pop(0)
        output.append(node)
        for i in adj_list[node]:
          if (visited[i]==0):
            visited[i]=1
            queue.append(i)
      out_f.write(f"{output}")
      

#Main Code Ends Here_____________________________________________________________________
    
#Drive Code Which I Made_________________________________________________________________
    def representation(V , edges):
      adj_list = [[]*V for i in range(V)]
      for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        adj_list[u].append(v)
        adj_list[v].append(u)
      BFS(adj_list)
    arr = []
    for i in read:
      temp = list(map(int,i.split()))
      arr.append(temp)
    representation(arr[0][0]+1,arr[1:len(arr)-1])
#Driver Code Ends Here____________________________________________________________________
