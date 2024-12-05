#Taking input____________________________________________________________________________
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#Taking Input Ends Here__________________________________________________________________

#Main_Code_Starts_From_Here______________________________________________________________
    def Merge(arr,low,mid,high):
      left = low
      right = mid+1
      maximum = -9999999999999999
      while(left<=mid and right<=high):
        if arr[left]<=arr[right]:
          maximum = max(maximum,arr[right])
          left+=1
        else:
          maximum = max(maximum,arr[left])
          right+=1
      while(left<=mid):
        maximum = max(maximum,arr[left])
        left+=1
      while(right<=high):
        maximum = max(maximum,arr[left])
        right+=1
      return maximum
          
    def MergeSort(arr,low,high):
      if (low==high):
        return arr[low]
      else:
        mid = (low+high)//2
        left = MergeSort(arr,low,mid)
        right = MergeSort(arr,mid+1,high)
        merge_result = Merge(arr,low,mid,high)
      return max(left,right,merge_result)
#Main_Code_Ends_Here_____________________________________________________________________


#Driver_Code_which_I_Made________________________________________________________________
    arr = []
    for i in range(len(read)):
      temp = list(map(int,read[i].split()))
      arr.append(temp)
    low = 0
    high = arr[0][0]-1
#This Line for Output____________________________________________________________________
    out_f.write(f"{MergeSort(arr[1],low,high)}")
