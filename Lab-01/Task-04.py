#sorting Algorithms
def bubble_sort(arr):
  for i in range(len(arr)):
    for j in range(len(arr)-i-1):
      if arr[j][0]>arr[j+1][0]:
        arr[j],arr[j+1] = arr[j+1],arr[j]
      elif arr[j][0]==arr[j+1][0]:
          if arr[j][2]<arr[j+1][2]:
              arr[j],arr[j+1] = arr[j+1],arr[j]
  return arr
#End here

#Input start from here
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read_files = inp_f.read().split("\n")
#Input End Here
#Output_Procedure start from here
    nums = []
    for i in range(1,13+1):
      nums.append([read_files[i].split(" ")[0],read_files[i].split(" ")[4],read_files[i].split(" ")[6]])
    bubble_sort(nums)
    for i in range(len(nums)):
      out_f.write(f"{nums[i][0]} will departure for {nums[i][1]} at {nums[i][2]}\n")
#End here.
