# 1st way - not good because 2 for are not allowed
# for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
#     nr = 0
#     for x in range(1, 2 * i): nr += (x if x <= i else 2 * i - x) * (10**(x-1))
#     print(nr)


#2nd way - not good because str is not allowed
# for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
#     list_nr = list(range(1, i)) + list(range(i, 0, -1))
#     print(int(''.join(map(str, list_nr))))


#3rd way
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    list_nr = list(range(1, i)) + list(range(i, 0, -1)); print(sum(map(lambda p: p[1] * 10**p[0], zip(range(len(list_nr) - 1, -1, -1), list_nr))))


#Problem Setter's code:
# for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
#     print((10**i//9)**2)

'''
You are given a positive integer N.
Your task is to print a palindromic triangle of size N.

For example, a palindromic triangle of size 5 is:
1
121
12321
1234321
123454321

You can't take more than two lines. The first line (a for-statement) is already written for you.
You have to complete the code using exactly one print statement.

Note:
Using anything related to strings will give a score of 0.
Using more than one for-statement will give a score of 0.

Input Format:
A single line of input containing the integer N.

Constraints:
0 < N < 10

Output Format:
Print the palindromic triangle of size N as explained above.

Sample Input:
5

Sample Output:
1
121
12321
1234321
123454321
'''