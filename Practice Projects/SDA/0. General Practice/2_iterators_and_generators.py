numbers = [4, 7, 10, 13, 16, 19, 22]


def generate_even_numbers(numbers):
    for n in numbers:
        if n%2 ==0 :
            yield n

#1st method
# generator = generate_even_numbers(numbers)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))  #StopIteration error will raise

#2nd method:
for nr in generate_even_numbers(numbers):
    print(nr)