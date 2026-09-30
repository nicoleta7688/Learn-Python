# Complete the solve function below.
def solve(s):
    
    list_of_str = list(s)
    
    if list_of_str[0].isalpha():
        list_of_str[0] = list_of_str[0].capitalize()
    
    prev_c = ''
    
    for index, c in enumerate(list_of_str):
        if prev_c == ' ':
            if c.isalpha():
                list_of_str[index] = c.capitalize()
        prev_c = c
            
    final_str = ''.join(list_of_str)
    
    return final_str



'''
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
Given a full name, your task is to capitalize the name appropriately.

Input Format:
A single line of input containing the full name, S.

Constraints:
0 < len(S) < 1000
The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format: Print the capitalized string, S.

Sample Input: chris alan
Sample Output: Chris Alan
'''