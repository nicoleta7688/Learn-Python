numbers = [2, 3, 4, 5, 6, 7, 8]

cubes_generator = (n**3 for n in numbers if n%2 == 0)

for n in cubes_generator:
    print(n)