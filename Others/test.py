# if __name__ == '__test_':
def name_funct(e):
    return e[0]

records = []

# records = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])

# 1. sortez lista dupa nume
# records.sort(key = name_funct)
# Use lamba function
records.sort(key = lambda e: e[0])


# 2. Create a set of grades
grades = set()

for name, grade in records:
    grades.add(grade)

# 3. Convert to list and sort
grades_list = sorted(grades)

# 4. Find the second lowes grade
second_lowest_grade = grades_list[1]

# 4. Print all names with this grade
for name, grade in records:
    if grade == second_lowest_grade:
        print(name)