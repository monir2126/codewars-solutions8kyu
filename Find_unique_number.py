def find_uniq(arr):
    numbers = {}

    for number in arr:
        if number in numbers:
            numbers[number] = numbers[number] + 1
        else:
            numbers[number] = 1

    for number in arr:
        if numbers[number] == 1:
            return number

