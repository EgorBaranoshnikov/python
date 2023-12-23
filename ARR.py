

arr1 = []

for i in range(10):
    if i < 5:
        arr1.insert(i, 1)
    if i >= 5:
        arr1.insert(i, i + 1)


sum = 0
for i in range(len(arr1)):
    print(i)

if 100 in arr1:
    print("OK")