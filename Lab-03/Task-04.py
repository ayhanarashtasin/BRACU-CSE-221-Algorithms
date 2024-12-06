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
      maximum = float('-inf')
      while(left<=mid and right<=high):
        for j in range(right,high+1):
           exp = arr[left] + arr[j]**2
           maximum = max(maximum,exp)
        temp.append(arr[left])
        left+=1
      while(right<=high):
        temp.append(arr[right])
        right+=1
      for i in range(low,high+1,1):
        arr[i] = temp[i-low]
      return maximum
    def MergeSort(arr,low,high):
      maximum = float('-inf')
      if (low<high):
        mid = (low+high)//2
        maximum = max(maximum,MergeSort(arr,low,mid))
        maximum = max(maximum,MergeSort(arr,mid+1,high))
        maximum = max(maximum,Merge(arr,low,mid,high))
      return maximum
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
