def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        return
    sequence = [0, 1]

    if n < 2:
        return sequence[n]

    for _ in range(2, n + 1):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence[-1]

print(fibonacci(15))
