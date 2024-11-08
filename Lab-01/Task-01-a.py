with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    arr = inp_f.read().split("\n")
    for i in range(1,len(arr)+1):
      if (int(arr[i])&1)==1: # I use bitwise operator . You can use Modulo.
        out_f.write(f"{arr[i]} is an ODD number.\n")
      else:
        out_f.write(f"{arr[i]} is an EVEN number.\n")
