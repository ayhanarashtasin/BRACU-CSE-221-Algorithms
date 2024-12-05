#Taking input____________________________________________________________________________
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#Taking Input Ends Here__________________________________________________________________

#Main_Code_Starts_From_Here______________________________________________________________
    def Merge(arr,low,mid,high):
      left = low
      right = mid+1
      temp = []
      count = 0
      while(left<=mid and right<=high):
        if arr[left]<=arr[right]:
          temp.append(arr[left])
          left+=1
        else:
          temp.append(arr[right])
          count += (mid-left+1)
          right+=1
      while(left<=mid):
        temp.append(arr[left])
        left+=1
      while(right<=high):
        temp.append(arr[right])
        right+=1
      for i in range(low,high+1,1):
        arr[i] = temp[i-low]
      return count
    def MergeSort(arr,low,high):
      count = 0
      if (low==high):
        return 0
      else:
        mid = (low+high)//2
        count+=MergeSort(arr,low,mid)
        count+=MergeSort(arr,mid+1,high)
        count+=Merge(arr,low,mid,high)
      return count
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
