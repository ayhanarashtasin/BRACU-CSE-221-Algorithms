#Taking input____________________________________________________________________________
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#Taking Input Ends Here__________________________________________________________________

#Main Code Starts Frome Here_____________________________________________________________
    def adj_List_representation(V , edges):
      adj_List = [[] for i in range(V)]
      for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        weight = edges[i][2]
        adj_List[u].append((v,weight))
      return adj_List
#Main Code Ends Here_____________________________________________________________________
    
#Drive Code Which I Made_________________________________________________________________
    arr = []
    for i in read:
      temp = list(map(int,i.split(" ")))
      arr.append(temp)
    adj_List = adj_List_representation(arr[0][0]+1,arr[1:])
#Driver Code Ends Here____________________________________________________________________

#This Part for printng the output_________________________________________________________
    count = 0
    for i in adj_List:
        if len(i)==0:
          out_f.write(f"{count} : {" "}\n")
        else:
          out_f.write(f"{count} : {i}\n")
        count+=1
