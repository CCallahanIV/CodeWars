def persistence(n):
    count = 0

    while len(str(n)) > 1:
        result = 1
        n_string = str(n)
        for digit in n_string:
            result *= int(digit)
        n = result

        count += 1

    return count
