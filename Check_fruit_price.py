#inputting the data
products = [
    {'name': 'orange', 'price': 20},
    {'name': 'apple', 'price': 8},
    {'name': 'banana', 'price': 10},
    {'name': 'kiwi', 'price': 30}
]

#calculating the length
n = len(products)


#checkiing the fruits whose price is more than 10
for i in range(n):
    if products[i]['price'] > 10:
        print(products[i]['name'])
