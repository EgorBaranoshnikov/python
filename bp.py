def binary_search(sequence, start_index, letter):
    end_index = len(sequence) - 1
    while start_index <= end_index:
        middle_index = start_index + (end_index - start_index) // 2
        currentLetter = sequence[middle_index]
        if currentLetter == letter:
            return middle_index
        elif currentLetter < letter:
            start_index = middle_index + 1
        else:
            end_index = middle_index - 1
    return -1


# Можно было еще элегантно создать sequence = [i for i range(1, 31)],
# но для наглядности перечислил все элементы
sequence = ["А", "Б", "В", "Г", "Д"]
# Число которое мы ищем
find_element = "А"

result = binary_search(sequence=sequence, start_index=0, letter=find_element)
print(result)