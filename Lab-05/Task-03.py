#Taking input____________________________________________________________________________
import queue
import heapq as hq
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#Taking Input Ends Here__________________________________________________________________
    from queue import PriorityQueue
#Main Code Starts Frome Here_____________________________________________________________
    def path(adj_list,destination):
      n = len(adj_list)
      danger_level = [float("inf")]*n
      min_heap = PriorityQueue()
      danger_level[1]=0
      min_heap.put((0,1))
      while not min_heap.empty():
        PriorityElement = min_heap.get()
        Node = PriorityElement[1]
        current_danger = PriorityElement[0]
        if destination==Node:
          return current_danger
        if current_danger>danger_level[Node]:
          continue
        for i in adj_list[Node]:
          adj_Node = i[0]
          adj_Danger = i[1]
          new_Danger = max(current_danger,adj_Danger)
          if new_Danger<danger_level[adj_Node]:
            danger_level[adj_Node] = new_Danger
            min_heap.put((new_Danger,adj_Node))
      return -1
      
      
#Main Code Ends Here_____________________________________________________________________
      
#Drive Code Which I Made_________________________________________________________________
    def representation(V , edges,src):
      adj_list = [[]*V for i in range(V)]
      for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        weight = edges[i][2]
        adj_list[u].append([v,weight])
      print(path(adj_list,src))
      
    arr = []
    for i in read:
      temp = list(map(int,i.split()))
      arr.append(temp)
    
    representation(arr[0][0]+1,arr[1:len(arr)-2],arr[0][0])
#Driver Code Ends Here____________________________________________________________________
