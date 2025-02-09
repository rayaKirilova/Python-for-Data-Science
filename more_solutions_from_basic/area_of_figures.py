from math import pi

figure = input()
figure_area = 0

if figure == 'square':
    square_side = float(input())
    figure_area = square_side * square_side
elif figure == 'triangle':
    triangle_side = float(input())
    triangle_height = float(input())
    figure_area = (triangle_side * triangle_height) / 2
elif figure == 'rectangle':
    rectangle_side_a = float(input())
    rectangle_side_b = float(input())
    figure_area = rectangle_side_a * rectangle_side_b
elif figure == 'circle':
    radius = float(input())
    figure_area = pi * radius * radius

print(f'{figure_area:.3f}')