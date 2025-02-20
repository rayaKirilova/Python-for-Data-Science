def smallest_of_three_nums(first_num, second_num, third_num) -> int:
    return min(first_num, second_num, third_num)

input_first_num = int(input())
input_second_num = int(input())
input_third_num = int(input())
print(smallest_of_three_nums(input_first_num, input_second_num, input_third_num))
