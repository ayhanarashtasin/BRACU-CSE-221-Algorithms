#Taking input____________________________________________________________________________
import queue
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#Taking Input Ends Here__________________________________________________________________

#Main Code Starts Frome Here_____________________________________________________________
    def DfsGraph(node,visited,adj_list,output):
      visited[node]=1
      output.append(node)
      for i in adj_list[node]:
        if (visited[i]==0):
          DfsGraph(i,visited,adj_list,output)
      return output
    def DFS(adj_list):
      n = len(adj_list)
      visited = [0]*n
      output = []
      start = 1
      Traverse = DfsGraph(start,visited,adj_list,output)
      out_f.write(f"{Traverse}")
      
      

#Main Code Ends Here_____________________________________________________________________
    
#Drive Code Which I Made_________________________________________________________________
    def representation(V , edges):
      adj_list = [[]*V for i in range(V)]
      for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        adj_list[u].append(v)
        adj_list[v].append(u)
      DFS(adj_list)
    arr = []
    for i in read:
      temp = list(map(int,i.split()))
      arr.append(temp)
    representation(arr[0][0]+1,arr[1:len(arr)])
#Driver Code Ends Here____________________________________________________________________
