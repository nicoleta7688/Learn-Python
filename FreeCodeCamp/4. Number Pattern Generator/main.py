def number_pattern(n):
    if not isinstance(n, int):
        return("Argument must be an integer value.")
    if n < 1:
        return("Argument must be an integer greater than 0.")
    
    number_string = []
    for num in range(1, n+1):
        number_string.append(str(num))
    
    return ' '.join(number_string)

print(number_pattern(12))
