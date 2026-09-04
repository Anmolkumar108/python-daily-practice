numbers = [1, 2, 2, 3, 1, 4, 2, 5]


frequency_list = []

for num in numbers:
    already_exists = False
    for item in frequency_list:
        if item[0] == num:
            already_exists = True
            break
            
    if not already_exists:
        count = numbers.count(num)
        frequency_list.append((num, count))

print(frequency_list)
