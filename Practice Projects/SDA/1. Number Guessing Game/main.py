import random
import re

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def choose_level(available_levels: dict[str, str]) -> int:
    select_lvl = True

    while(select_lvl):
        print("\nChoose a level for game:")

        for level, description in available_levels.items():
            print(f"{level} - {description}")

        game_level = input('Type 1, 2 or 3, based of level you want: ')
        if not re.fullmatch(r'[1-3]', game_level):
            print(f"{YELLOW}Invalid option.{RESET} Available options are: 1, 2 or 3")
        else:
            print(f"\n{available_levels[game_level]}")
            select_lvl = False

    return int(game_level)

def validate_nr(user_choice: str, max_value: int) -> bool:
    if re.fullmatch(r"[0-9]+", user_choice) and int(user_choice) <= max_value:
        return True
    
    print(f"{YELLOW}The input must be an integer number between 0 and {max_value}!{RESET}")
    return False

def main():

    lost_games = 0
    won_games = 0

    available_levels = {
        '1': f"Easy: Try to guess the number between {GREEN}0{RESET} and {GREEN}100{RESET}",
        "2": f"Moderate: Try to guess the number between {GREEN}0{RESET} and {GREEN}100{RESET} in {GREEN}5{RESET} attempts",
        "3": f"Hard: Try to guess the number between {GREEN}0{RESET} and {GREEN}1000{RESET} in {GREEN}10{RESET} attempts"
    }

    while(True):
        game_lvl = choose_level(available_levels)

        match game_lvl:
            case 1:
                max_value = 100
                limit = None
            case 2: 
                max_value = 100
                limit = 5
            case 3:
                max_value = 1000
                limit = 10

        correct_nr = random.randrange(0, max_value+1)
        # print(correct_nr)

        attempts = 1
        try_again = True

        while (try_again):

            user_choice = input('\nInput: ')

            if not validate_nr(user_choice, max_value):
                continue

            user_choice = int(user_choice)

            print(f"Nr of attempts: {attempts}")
            if user_choice == correct_nr:
                print(f"{GREEN}Congratulations!!!{RESET}")
                print(f"The correct number is: {correct_nr}")
                won_games += 1
                try_again = False
            else:
                if user_choice < correct_nr:
                    print("The guess is too low")
                elif user_choice > correct_nr:
                    print("The guess is too high")

                if limit is not None:
                    if attempts >= limit:
                        try_again = False
                        print(f"{RED}Game Over.{RESET} Maximum attempts reached. The correct nr. was: {correct_nr}")
                        lost_games += 1
                        break
                attempts += 1

        print("\n---------------------------------------------------")
        print(f"Total nr. of games played: {lost_games + won_games}")
        print(f"Lost games: {lost_games}")
        print(f"Won games: {won_games}")
        print("---------------------------------------------------")


if __name__ == '__main__':
    main()


