#Taking input____________________________________________________________________________
import queue
import heapq as hq
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#Taking Input Ends Here__________________________________________________________________
    from queue import PriorityQueue
#Main Code Starts Frome Here_____________________________________________________________
    def DijksTras(V, adj_list, src):
      min_heap = PriorityQueue()
      distance = [float("inf")] * V
      distance[src] = 0
      min_heap.put((0, src))
      value = 0
      while not min_heap.empty():
        PriorityElement = min_heap.get()
        current_distance = PriorityElement[0]
        node = PriorityElement[1]
        value = node
        for i in adj_list[node-1]:
            edgeWeight = i[1]
            adjNode = i[0]
            if current_distance + edgeWeight < distance[adjNode]:
                distance[adjNode] = current_distance + edgeWeight
                min_heap.put((distance[adjNode], adjNode))
      return distance
#Main Code Ends Here_____________________________________________________________________
    
#Drive Code Which I Made_________________________________________________________________
    def representation(V , edges,src):
      adj_list = [[]*V for i in range(V)]
      for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        weight = edges[i][2]
        adj_list[u].append([v,weight])
      Alice = (DijksTras(V,adj_list[1:],src[0]))
      Bob = (DijksTras(V,adj_list[1:],src[1]))
      mintime = float("inf")
      meetingNode = -1
      for i in range(1,len(Alice)):
        if Alice[i] != float('inf') and Bob[i]!=float("inf"):
          maxtime = max(Alice[i],Bob[i])
          if maxtime<mintime:
            mintime = maxtime
            meetingNode = i
      if meetingNode ==-1:
        out_f.write(f"IMPOSSIBLE")
      else:
        out_f.write(f"TIME : {mintime}\nNode : {meetingNode}")
      
    arr = []
    for i in read:
      temp = list(map(int,i.split()))
      arr.append(temp)
    representation(arr[0][0]+1,arr[1:len(arr)-2], (arr[len(arr)-2][0],arr[len(arr)-2][1]))
#Driver Code Ends Here____________________________________________________________________
