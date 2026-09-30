# def minion_game(string):
#     vowels = 'AEIOUaeiou'

#     stuart_list = [] # Stuart - consonants
#     kevin_list = []  # Kevin - vowels

#     for start_index, c in enumerate(string):
#         current_word = string[start_index:]

#         # print("cuvantul curent: " + current_word)
#         for nr, ch in enumerate(current_word):
#             created_word = current_word[:nr + 1]
#             # print(created_word)

#             if vowels.find(c) == -1:
#                 stuart_list.append(created_word)
#             else:
#                 kevin_list.append(created_word)

#     # print("Stuart: ")
#     # print(stuart_list)
#     # print("Kevin")
#     # print(kevin_list)

#     stuart_points = len(stuart_list)
#     kevin_points = len(kevin_list)

#     if stuart_points > kevin_points:
#         print(f"Stuart {stuart_points}")
#     elif stuart_points < kevin_points:
#         print(f"Kevin {kevin_points}")
#     else:
#         print("Draw")


def minion_game(string):
    vowels = 'AEIOUaeiou'

    stuart_points = 0 # Stuart - consonants
    kevin_points = 0  # Kevin - vowels
    len_str = len(string)

    for start_index, c in enumerate(string):
        # current_word = string[start_index:]
        len_current_word = len_str - start_index

        if vowels.find(c) == -1:
            stuart_points += len_current_word
        else:
            kevin_points += len_current_word


    if stuart_points > kevin_points:
        print(f"Stuart {stuart_points}")
    elif stuart_points < kevin_points:
        print(f"Kevin {kevin_points}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)


'''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules:
Both players are given the same string, S.
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring:
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
Your task is to determine the winner of the game and their score.

Function Description:
Complete the minion_game in the editor below.
minion_game has the following parameters: string string: the string to analyze
Prints: string: the winner's name and score, separated by a space on one line, or Draw if there is no winner

Input Format:
A single line of input containing the string S.
Note: The string S will contain only uppercase letters: [A - Z].

Constraints:
0 <= len(S) <= 10^6

Sample Input: BANANA
Sample Output: Stuart 12
Note: Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.
'''