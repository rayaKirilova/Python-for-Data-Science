def get_characters(first_char: str, second_char: str):
    character_list = []
    for i in range(ord(first_letter) + 1, ord(second_letter)):
        list_element = chr(i)
        character_list.append(list_element)

    return ' '.join(character_list)

first_letter = input()
second_letter = input()

print(get_characters(first_letter, second_letter))