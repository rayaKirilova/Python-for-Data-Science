def repeat_string(text:str, count:int) -> str:
    return text * count

input_text = input()
input_counter = int(input())
print(repeat_string(input_text, input_counter))