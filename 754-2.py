strings = open("input.txt").readlines()
stringsx = strings[0].split(" ")
maxWeight = 0
isError = False
for str in stringsx:
    weight = int(str)
    if weight > 727:
        isError = True
        break
    if weight < 94:
        isError = True
        break
    if weight > maxWeight:
        maxWeight = weight
if isError:
    print("Error")
if not isError:
    print(maxWeight)
