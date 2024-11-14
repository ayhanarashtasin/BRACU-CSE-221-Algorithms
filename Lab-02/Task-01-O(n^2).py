#Taking input
#_______________________________________________________________________
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#_______________________________________________________________________
#Taking Input Ends Here
#Main_Code_Start_From_Here
    def SortedArrayTwoSum(arr,target):
      for i in range(len(arr)):
        for j in range(i+1,len(arr)):
          if arr[i]+arr[j]==target:
            out_f.write(f"{i+1} {j+1}")
    
#Driver_Code_Which_I_MADE
#_____________________________________________________________________
    array = []
    for i in range(len(read)):
      temp = list(map(int,read[i].split()))
      array.append(temp)
    SortedArrayTwoSum(array[1],array[0][1])
#_____________________________________________________________________
