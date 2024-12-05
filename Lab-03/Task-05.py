#Taking input____________________________________________________________________________
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#Taking Input Ends Here__________________________________________________________________

#Main_Code_Starts_From_Here______________________________________________________________
    def Find_Partition_Index(arr,low,high):
      left = low
      right = high
      pivot = arr[low]
      while(left<right):
        while(left<high and  arr[left]<=pivot ):
          left+=1
        while( right>low and arr[right]>pivot):
          right-=1
        if (left<right):
           arr[left],arr[right]=arr[right],arr[left]
      arr[low],arr[right]=arr[right],arr[low]
      return right
    def QuickSort(arr,low,high):
      if (low<high):
        partition = Find_Partition_Index(arr,low,high)
        QuickSort(arr,low,partition-1)
        QuickSort(arr,partition+1,high)
      return arr
#Main_Code_Ends_Here_____________________________________________________________________


#Driver_Code_which_I_Made________________________________________________________________
    arr = []
    for i in range(len(read)):
      temp = list(map(int,read[i].split()))
      arr.append(temp)
    low = 0
    high = arr[0][0]-1
#This Line for Output____________________________________________________________________
    out_f.write(f"{QuickSort(arr[1],low,high)}")
