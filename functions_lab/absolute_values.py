def absolute_values(input_list_of_elements):
    result_list = []
    for element in input_list_of_elements:
        list_element = float(element)
        result_list.append(abs(list_element))
    return result_list

input_list = input().split()
print(absolute_values(input_list))