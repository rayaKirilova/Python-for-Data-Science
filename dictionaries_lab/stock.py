products = input().split()
search_products = input().split()
stock = {}

for index in range(0, len(products), 2):
    key = products[index]
    value = int(products[index +1])
    stock[key] = value

for current_product in search_products:
    if current_product in stock.keys():
        product_quantity = stock[current_product]
        print(f'We have {product_quantity} of {current_product} left')
    else:
        print(f'Sorry, we don\'t have {current_product}')