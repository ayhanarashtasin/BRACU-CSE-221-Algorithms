#Taking input____________________________________________________________________________
import queue
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#Taking Input Ends Here__________________________________________________________________

#Main Code Starts Frome Here_____________________________________________________________
    def Topo_Sort(node, visited, stack, pathvisited, adj_list):
       visited[node] = 1
       pathvisited[node] = 1
       for neighbor in adj_list[node]:
           if visited[neighbor] == 0:
               if Topo_Sort(neighbor, visited, stack, pathvisited, adj_list):
                   return True
           elif pathvisited[neighbor] == 1:
               return True
       stack.append(node)
       pathvisited[node] = 0
       return False

    def DFS(adj_list):
      n = len(adj_list)
      visited = [0] * n
      pathvisited = [0] * n
      stack = []
      for i in range(1, n):
        if visited[i] == 0:
            if Topo_Sort(i, visited, stack, pathvisited, adj_list):
                return "Impossible"
      output = stack[::-1]
      return output
      
#Main Code Ends Here_____________________________________________________________________
    
#Drive Code Which I Made_________________________________________________________________
    def matrix_representation(V , edges):
      adj_list = [[]*V for i in range(V)]
      for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        adj_list[u].append(v)
      out_f.write(f"{(DFS(adj_list))}")
    arr = []
    for i in read:
      temp = list(map(int,i.split()))
      arr.append(temp)
    matrix_representation(arr[0][0]+1,arr[1:len(arr)-1])
#Driver Code Ends Here____________________________________________________________________
