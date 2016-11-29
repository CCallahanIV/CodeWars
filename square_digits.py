def square_digits(num):
    result = ""
    num = str(num)
    for digit in num:
        result += str(int(digit)**2)

    return int(result)

print(square_digits(9119))
