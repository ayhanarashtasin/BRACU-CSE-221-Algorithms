def selection_Sort(arr): #Code of selection sort
  for i in range(len(arr)):
    minimum_index = i
    for j in range(i+1,len(arr)):
      if arr[j]>arr[minimum_index]:
        minimum_index = j
    arr[i],arr[minimum_index] = arr[minimum_index],arr[i]
  return arr            #End here

#Input taking procedure start 
file1 = open("input1a.txt")
file2 = open("output1a.txt","w")
s = int(file1.readline())
student_ID = list(map(int,file1.readline().split(" ")))
student_marks = list(map(int,file1.readline().split(" ")))
N = len(student_ID)
#End Here

#Output procedure start
database = {}
for i in range(N):
  if student_marks[i] not in database:
    database[student_marks[i]] = [student_ID[i]]
  else:
    database[student_marks[i]].append(student_ID[i])
selection_Sort(student_marks)
for key,value in database.items():
  selection_Sort(value)
for i in range(N):
  if i==0 or student_marks[i]!=student_marks[i-1]:
    for j in range(len(database[student_marks[i]])):
      file2.write(f"ID: {database[student_marks[i]][j]} Mark: {student_marks[i]}.\n")

file2.close()
#End Here


