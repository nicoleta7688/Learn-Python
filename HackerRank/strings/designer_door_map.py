sizes = input().split(" ")
n = int(sizes[0])
m = int(sizes[1])

if n != 0 and m / n != 3:
    print("M should be 3 times N")

lines = n // 2

for num in range(1, lines+1):
    str = ".|." * (num * 2 - 1)
    print(str.center(m, '-'))

print('WELCOME'.center(m, '-'))

for num in range(lines, 0, -1 ):
    str = ".|." * (num * 2 - 1)
    print(str.center(m, '-'))

'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

Sample Designs:
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

    Input Format: 
A single line containing the space separated values of  and .

Constraints: 
5 < N < 101
15 < M < 303

Output Format: Output the design pattern.

Sample Input
9 27

Sample Output
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
'''