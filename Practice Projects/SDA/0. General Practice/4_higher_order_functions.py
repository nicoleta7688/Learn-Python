numbers = [3, 8, 12, 5, 7, 20, 11, 16]

# Folosește lambda pentru a crea o funcție multiply care primește două numere și returnează produsul lor.
# lambda a, b: a * b


# Folosește map() și lambda pentru a crea o listă cu pătratele tuturor numerelor.
l1 = list(map(lambda nr: nr**2, numbers))

# Folosește filter() și lambda pentru a obține doar numerele mai mari decât 10.
l2 = list(filter(lambda nr: nr > 10, numbers))


# Folosește map() și filter() împreună pentru a obține pătratele numerelor pare.
l3 = list(map(lambda nr: nr**2 ,filter(lambda nr: nr%2 == 0, numbers)))
# same as l3:
l4 = [nr**2 for nr in numbers if nr % 2 == 0]

print(l1)
print(l2)
print(l3)