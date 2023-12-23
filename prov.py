my_string = "2.7182818284590452353602875"
result_string = ""

fin  = open("input.txt")
strings = fin.readlines()
b = strings[0]
index = int(b) + 2

for i in range(len(my_string)):
   if i != index:
       result_string += my_string[i]

print(result_string)