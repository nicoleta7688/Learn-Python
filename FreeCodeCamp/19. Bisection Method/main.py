def square_root_bisection(nr, tolerance = 1e-7, max_iterations = 1000):
    if nr < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif nr == 0 or nr == 1:
        print(f"The square root of {nr} is {nr}")
        return nr

    low = 0
    high = 1 if nr < 1 else nr

    iterations = 0

    while(iterations < max_iterations):
        middle_value = (low + high) / 2

        if nr == middle_value**2 or abs(high - low) <= tolerance:
            print(f'The square root of {nr} is approximately {middle_value}')
            return middle_value
        elif nr < middle_value**2:
            high = middle_value
        else:
            low = middle_value

        iterations += 1

    else:
        print(f"Failed to converge within {max_iterations} iterations")
        return None