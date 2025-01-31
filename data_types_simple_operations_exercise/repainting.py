nylon_amount = int(input())
paint_amount = int(input())
liters_thinner = int(input())
work_hours = int(input())

amount_for_materials = ((nylon_amount +2) * 1.5) + ((paint_amount + paint_amount * 0.1)* 14.5) + (liters_thinner * 5) + 0.4
amount_for_work = (amount_for_materials * 0.3) * work_hours
total_amount = amount_for_materials + amount_for_work

print(total_amount)
