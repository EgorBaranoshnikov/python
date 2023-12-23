def count_pairs(sequence):
    count = 0
    max_sum = 0

    for i in range(len(sequence) - 1):
        if sequence[i] % 10 == 3 and sequence[i+1] % 10 != 3:
            sum_of_squares = sequence[i]**2 + sequence[i+1]**2
            if sum_of_squares >= max_sum:
                max_sum = sum_of_squares
            count += 1

    return count, max_sum

# Пример использования
seq = [-13, 10, 9, -3, 1, -3, 1]
result = count_pairs(seq)
print(result)