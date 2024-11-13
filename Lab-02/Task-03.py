#Taking input 
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
    N = int(read[0])
    arr = []
    for i in range(1,N+1):
      arr.append(list(map(int,read[i].split())))
#Creating array ends here array looks like [(1,2),(3,4)] format = (start,end)
      
    arr.sort(key = lambda x: x[1]) # sorting array basis of second element which is end.
    output_array = [] # store this value for printing 
    output_array.append(arr[0])# we append 1st pait because work always start from here
    EndTime = arr[0][1] #Storing the end time for checking next work.
    count = 1
    for i in range(len(arr)):
      if arr[i][0]>=EndTime:
        count+=1
        EndTime = arr[i][1]
        output_array.append(arr[i])
        
#Output_Code start from Here
    out_f.write(f"{count}\n")
    for i in range(len(output_array)):
      out_f.write(f"{output_array[i][0]} {output_array[i][1]} \n")
#Output_Code End Here
