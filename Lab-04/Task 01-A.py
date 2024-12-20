#Taking input____________________________________________________________________________
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#Taking Input Ends Here__________________________________________________________________

#Main Code Starts Frome Here_____________________________________________________________
    def matrix_representation(V , edges):
      Matrix = [[0]*V for i in range(V)]
      for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        Matrix[u][v] = edges[i][2]
      return Matrix
#Main Code Ends Here_____________________________________________________________________
    
#Drive Code Which I Made_________________________________________________________________
    arr = []
    for i in read:
      temp = list(map(int,i.split(" ")))
      arr.append(temp)
    Matrix = matrix_representation(arr[0][0]+1,arr[1:])
#Driver Code Ends Here____________________________________________________________________

#This Part for printng the output_________________________________________________________
    for i in Matrix:
      out_f.write(f"{i}\n")
