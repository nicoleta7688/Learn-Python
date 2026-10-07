def wrapper(f):
    def fun(l):
        for i, nr in enumerate(l):
            nr_len = len(nr)
            if nr_len == 11:
                nr = nr [1:]
            elif nr_len == 12:
                nr = nr [2:]
            elif nr_len == 13:
                nr = nr [3:]
            l[i] = '+91 ' + nr[0:5] + ' ' + nr[5:]
        return f(l)
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 




'''
Let's dive into decorators! You are given N mobile numbers. Sort them in ascending order then print them in the standard format shown below:
+91 xxxxx xxxxx

The given mobile numbers may have +91, 91 or 0 written before the actual 10 digit number. Alternatively, there may not be any prefix at all.

Input Format:
The first line of input contains an integer N, the number of mobile phone numbers.
N lines follow each containing a mobile number.

Output Format:
Print N mobile numbers on separate lines in the required format.

Sample Input:
3
07895462130
919875641230
9195969878

Sample Output:
+91 78954 62130
+91 91959 69878
+91 98756 41230

Concept:
Like most other programming languages, Python has the concept of closures. Extending these closures gives us decorators, which are an invaluable asset. You can learn about decorators in 12 easy steps here.
To solve the above question, make a list of the mobile numbers and pass it to a function that sorts the array in ascending order. Make a decorator that standardizes the mobile numbers and apply it to the function.
'''