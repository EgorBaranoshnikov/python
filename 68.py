fin  = open("input.txt")
strings = fin.readlines()
first_line = strings[0]
second_line = int(strings[1])

if first_line == 'Home\n':
        print('Yes')
else:
    if second_line % 2 == 0:
        print('No')
    else:
        print('Yes')
