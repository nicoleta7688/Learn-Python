numbers = [3, 8, 12, 5, 7, 20, 11, 16]

#O listă even_numbers, care conține doar numerele pare.
even_numbers = [n for n in numbers if n%2 == 0]

#O listă large_numbers, care conține numerele mai mari decât 10, fiecare înmulțit cu 2.
large_numbers = [n * 2 for n in numbers if n > 10]

#Un set unique_squares, care conține pătratele numerelor din listă mai mari sau egale cu 10.
unique_squares = {n**2 for n in numbers if n >= 10}

print(even_numbers)
print(large_numbers)
print(unique_squares)
