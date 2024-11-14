#Taking input
#_______________________________________________________________________
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#_______________________________________________________________________
#Taking Input Ends Here
#Main_Code_Start_From_Here
    def MergeTwoSortedArray(Alice_array,Bob_array):
      Merge_array = [0]*(len(Alice_array)+len(Bob_array))
      index = 0
      for i in range(len(Alice_array)):
        Merge_array[index] = Alice_array[i]
        index+=1
      for i in range(len(Bob_array)):
        Merge_array[index] = Bob_array[i]
        index+=1
      Merge_array.sort()
      return Merge_array
    
#Driver_Code_Which_I_MADE
#_____________________________________________________________________
    array = []
    for i in range(len(read)):
      temp = list(map(int,read[i].split()))
      array.append(temp)
    out_f.write(f"{MergeTwoSortedArray(array[1],array[3])}")
#_____________________________________________________________________
