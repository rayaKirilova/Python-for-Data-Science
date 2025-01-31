length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

aquarium_volume = length * width * height
volume_liters = aquarium_volume / 1000
required_liters = volume_liters * (1 - percentage / 100)

print(round(required_liters, 2))