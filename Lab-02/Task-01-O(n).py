#Taking input
#_______________________________________________________________________
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#_______________________________________________________________________
#Taking Input Ends Here
#Main_Code_Start_From_Here
    def SortedArrayTwoSum(arr,target):
      start = 0
      end = len(arr)-1
      while(start<end):
        if arr[start]+arr[end]==target:
          return (f"{start+1} {end+1}")
        elif arr[start]+arr[end]>target:
          end-=1
        else:
          start+=1
      return f"IMPOSSIBLE"
    
#Driver_Code_Which_I_MADE
#_____________________________________________________________________
    array = []
    for i in range(len(read)):
      temp = list(map(int,read[i].split()))
      array.append(temp)
    out_f.write(f"{SortedArrayTwoSum(array[1],array[0][1])}")
#_____________________________________________________________________
