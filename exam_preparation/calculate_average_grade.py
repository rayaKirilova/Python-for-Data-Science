students_count = int(input())
sum_grade = 0

for _ in range(students_count):
    student_grade = float(input())
    sum_grade += student_grade

average_grade = sum_grade / students_count
print(f'{average_grade:.2f}')