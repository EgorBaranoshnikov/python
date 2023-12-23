fin  = open("input.txt")
strings = fin.readlines()
numbers = strings[0].split()

arr_a = [int(numbers[0]), int(numbers[1]), int(numbers[2])]
arr_b = [int(numbers[3]), int(numbers[4]), int(numbers[5])]
for i in range(len(arr_a) - 1):
    for q in range(len(arr_a) - 1):
        if arr_a[q] > arr_a[q + 1]:
            arr_a[q], arr_a[q + 1] = arr_a[q + 1], arr_a[q]

for i in range(len(arr_b) - 1):
    for q in range(len(arr_b) - 1):
        if arr_b[q] > arr_b[q + 1]:
            #q_plus_1 = arr_b[q + 1]
            #arr_b[q + 1] = arr_b[q]
            #arr_b[q] = q_plus_1
            arr_b[q], arr_b[q + 1] = arr_b[q + 1], arr_b[q]

otv1 = arr_a[0] * arr_b[0]
otv2 = arr_a[1] * arr_b[1]
otv3 = arr_a[2] * arr_b[2]
otv = otv1 + otv2 + otv3
print(otv)