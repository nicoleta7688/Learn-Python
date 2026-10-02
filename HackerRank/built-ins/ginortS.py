txt = input()

lower_cases = []
upper_cases = []
odd_digit = []
even_digit = []

for c in txt:
    if c.isdigit():
        if int(c) % 2 == 0:
            even_digit.append(c)
        else:
            odd_digit.append(c)
    elif c.isupper():
        upper_cases.append(c)
    else:
        lower_cases.append(c)

final_arr = [lower_cases, upper_cases, odd_digit, even_digit]
final_txt = ""

for a in final_arr:
    a.sort()
    final_txt  += "".join(a)

print(final_txt)

'''
You are given a string S.
S contains alphanumeric characters only.

Your task is to sort the string S in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

Input Format:
A single line of input contains the string S.

Constraints:
0 < len(S) < 1000

Output Format:
Output the sorted string S.

Sample Input:
Sorting1234

Sample Output:
ginortS1324
'''