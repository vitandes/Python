def sum_two_smallest_numbers(numbers):

    min = numbers[0]  

    for number in numbers:
        if number< min:
            min = number

    index = numbers.index(min)
    firstNumber = numbers.pop(index)
    min = numbers[0]

    for number in numbers:
        if number< min:
            min = number
    
    index = numbers.index(min)
    secondoNumber = numbers.pop(index)

    return firstNumber + secondoNumber
    

a = sum_two_smallest_numbers([19, 5, 42, 2, 77])
print(a)