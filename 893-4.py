fin = open("input.txt")
strings = fin.readlines()
a = int(strings[0])
vremGoda = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
names = ["Winter", "Spring", "Summer", "Autumn"]
printMsg = "Error"

for num in range(len(vremGoda)):
    for mes in vremGoda[num]:
        if mes == a:
            printMsg = names[num]
            break

print(printMsg)
print(vremGoda[[1]])