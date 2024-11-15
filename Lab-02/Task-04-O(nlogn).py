input_file = open("input4.txt", "r")

output_file = open("output4'.txt","w")
tasks, people = map(int, input_file.readline().split())
# Store data in a list
all = []
for i in range(tasks):
  all.append(list(map(int, input_file.readline().split(" "))))
def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  middle = len(arr) // 2
  left_half = arr[:middle]
  right_half = arr[middle:]
  left_half = merge_sort(left_half)
  right_half = merge_sort(right_half)
  sorted_arr = []
  left_index, right_index = 0, 0
  while left_index < len(left_half) and right_index < len(right_half):
    if left_half[left_index][1] < right_half[right_index][1]:
      sorted_arr.append(left_half[left_index])
      left_index += 1
    else:
      sorted_arr.append(right_half[right_index])
      right_index += 1
  sorted_arr.extend(left_half[left_index:])
  sorted_arr.extend(right_half[right_index:])
  return sorted_arr
all = merge_sort(all)

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
