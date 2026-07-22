full_dot = '●'
empty_dot = '○'

def create_character(character_name, strength, intelligence, charisma):
    if not isinstance(character_name, str):
        return "The character name should be a string"
    elif character_name == "":
        return "The character should have a name"
    elif len(character_name) > 10:
        return "The character name is too long"
    elif character_name.find(" ") != -1:
        return "The character name should not contain spaces"

    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"

    sum_stats = strength + intelligence + charisma

    if sum_stats != 7:
        return 'The character should start with 7 points'

    result = character_name + "\n" + "STR " + full_dot*strength + empty_dot*(10 - strength) + "\n" + "INT " + full_dot*intelligence + empty_dot*(10 - intelligence) + "\n" + "CHA " + full_dot*charisma + empty_dot*(10 - charisma)

    return result


print (create_character('ren', 4, 2, 1))
