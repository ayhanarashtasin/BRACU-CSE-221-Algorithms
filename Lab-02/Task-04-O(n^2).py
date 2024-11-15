input_file = open("input4.txt", "r")
output_file = open("output4.txt","w")
tasks, people = map(int, input_file.readline().split())
all = []
for i in range(tasks):
  all.append(list(map(int, input_file.readline().split(" "))))

# Sort data according to end time
def bubbleSort(arr):
  swapped = False
  for i in range(tasks):
    for j in range(tasks-i-1):
      if arr[j][1] > arr[j+1][1]:
        swapped = True
        arr[j], arr[j+1] = arr[j+1], arr[j]
    if swapped == False:
      return
bubbleSort(all)
# Create list for M people
m = [all[0]]
n = []
all.pop(0)                             
count = 1
idx1 = 0
idx2 = 0

# Calculate Maximum Tasks
for j in range(len(all)):
  if m[idx1][1] <= all[j][0] or m[idx1][0] == all[j][0] and m[idx1][1] < all[j][1] or m[idx1-1][1] == all[j][0]:
    m.append(all[j])
    idx1 += 1
    count += 1
  elif n != []:
    if n[idx2][1] <= all[j][0] or n[idx2][0] == all[j][0] and n[idx2][1] < all[j][1] or n[idx2-1][1] == all[j][0]:
      n.append(all[j])
      idx2 += 1
      count += 1
  else:
      n.append(all[j])
      count += 1
output_file.write(f"{count}")
output_file.close()
