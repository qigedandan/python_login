with open('price.txt', 'r') as f:
    lines = f.readlines()
goods = []
for line in lines:
    name, price, amount = line.split()
    goods.append({'name': name, 'price': int(price), 'amount': int(amount)})
print(goods)
all_price = 0
for good in goods:
    all_price += good['price'] * good['amount']
print(all_price)