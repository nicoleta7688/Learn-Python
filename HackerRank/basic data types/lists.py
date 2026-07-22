if __name__ == '__main__':
    N = int(input())
    
    commands = []
    for i in range(N):
        commands.append(str(input()))

    cmd_list = []
    user_list = []

    for command in commands:
        str_cmd = ""
        cmd_list = command.split()
        len_cmd = len(cmd_list)
        dont_exec = False

        if(len_cmd == 1):
            if (cmd_list[0] != 'print'):
                str_cmd = f"user_list.{cmd_list[0]}()"
            else:
                print(user_list)
        elif(len_cmd == 2):
            str_cmd = f"user_list.{cmd_list[0]}({cmd_list[1]})"
        elif(len_cmd == 3):
            str_cmd = f"user_list.{cmd_list[0]}({cmd_list[1]},{cmd_list[2]})"
        else:
            dont_exec = True

        if not dont_exec:
            exec(str_cmd)
        else:
            print("No such cmd")



# O soluție foarte dinamică ar fi:
# user_list = []
# for _ in range(N):
#     cmd = input().split()
#     method = getattr(user_list, cmd[0])
#     args = list(map(int, cmd[1:]))
#     method(*args)


"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example
: Append  to the list, .
: Append  to the list, .
: Insert  at index , .
: Print the array.
Output:
[1, 3, 2]
Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

"""