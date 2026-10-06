#simpler version:
# import re

# for _ in range(int(input())):
#     s = input()
    
#     try:
#         re.compile(s)
#     except re.error:
#         print("False")
#     else:
#         print("True")


#harder but compatible with hackerank:
import re

for _ in range(int(input())):
    s = input()
    
    try:
        # Reject possessive quantifiers introduced in Python 3.11
        if re.search(r'(?<!\\)(?:[*+?]|\{[^}]*\})\+', s):
            print("False")
        else:
            re.compile(s)
            print("True")

    except re.error:
        print("False")



'''
You are given a string S.
Your task is to find out whether S is a valid regex or not.

Input Format:
The first line contains integer T, the number of test cases.
The next T lines contains the string S.

Constraints:
0 < T < 100

Output Format:
Print "True" or "False" for each test case without quotes.

Sample Input:
2
.*\+
.*+

Sample Output:
True
False

Explanation:
.*\+ : Valid regex.
.*+: Has the error multiple repeat. Hence, it is invalid.
'''