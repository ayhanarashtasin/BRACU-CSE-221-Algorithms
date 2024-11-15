file1 = open("input.txt")
file2 = open("output.txt","w")
s = file1.readlines()
N = int(s[0].strip())
for i in range(1,N+1):
    store = s[i].strip()
    parts = store.split()
    number1 = int(parts[1])
    number2 = int(parts[3])
    operation = parts[2]
    if operation == "+":
        file2.write(f"The result of {number1} {operation} {number2} is {number1+number2}.\n")
    if operation == "-":
        file2.write(f"The result of {number1} {operation} {number2} is {number1-number2}.\n")
    if operation == "*":
        file2.write(f"The result of {number1} {operation} {number2} is {number1*number2}.\n")
    if operation == "/":
        file2.write(f"The result of {number1} {operation} {number2} is {number1/number2}.\n")
    
    
file2.close()
