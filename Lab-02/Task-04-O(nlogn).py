#Taking input____________________________________________________________________________
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#Taking Input Ends Here__________________________________________________________________
    from queue import PriorityQueue
#Main_Code_Start_from_Here________________________________________________________________
    def MeetingRooms(arr,length):
      min_heap = PriorityQueue()
      arr.sort(key = lambda x: x[1])
      count = 0
      for i in arr:
        if not min_heap.empty() and i[0]>=min_heap.queue[0]:
            min_heap.get()
        if min_heap.qsize()<length:
                min_heap.put(i[1])
                count+=1
      return count
#Main_code_Ends_Here______________________________________________________________________

#Drive_Code_Which_I_Made__________________________________________________________________
    arr = []
    for i in range(len(read)):
      temp = list(map(int,read[i].split()))
      arr.append(temp)
    out_f.write(f"{MeetingRooms(arr[1:],arr[0][1])}")
#Driver_Code_Ends_Here
