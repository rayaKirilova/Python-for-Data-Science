deposit_amount = float(input())
term_of_deposit = int(input())
annual_interest_rate = float(input())

accumulated_interest = deposit_amount * (annual_interest_rate / 100)
interest_per_month = accumulated_interest / 12
amount = deposit_amount + term_of_deposit * interest_per_month

print(amount)