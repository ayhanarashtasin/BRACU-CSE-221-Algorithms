#Taking input____________________________________________________________________________
import queue
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#Taking Input Ends Here__________________________________________________________________

#Main Code Starts Frome Here_____________________________________________________________
    def DfsGraph(node,visited,adj_list,pathvisited):
      visited[node]=1
      pathvisited[node]=1
      for i in adj_list[node]:
        if (visited[i]==0):
          if (DfsGraph(i,visited,adj_list,pathvisited)==True):
            return True
        else:
          if pathvisited[i]==1:
            return True
      pathvisited[node]=0
      return False
    def DFS(adj_list):
      n = len(adj_list)
      visited = [0]*n
      pathvisited = [0]*n
      start = 1
      for i in range(n):
         if visited[i]==0:
          if DfsGraph(start,visited,adj_list,pathvisited) ==True:
            return 'Yes'
      return 'No'
#Main Code Ends Here_____________________________________________________________________
    
#Drive Code Which I Made_________________________________________________________________
    def representation(V , edges):
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
    representation(arr[0][0]+1,arr[1:len(arr)])
#Driver Code Ends Here____________________________________________________________________
