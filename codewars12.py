def solution(s):
    roman_to_decimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for c in s[::-1]:  # Iterate through the string in reverse order
        value = roman_to_decimal[c]
        if value >= prev_value:
            total += value
        else:
            total -= value
        prev_value = value

    return total



print(solution('IX'))