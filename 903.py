def a():
    fin  = open("input.txt")
    strings = fin.readlines()
    numbers = strings[0].split()
    b = int(numbers[0])
    b += 1
    print(b)
a()
a()
a()