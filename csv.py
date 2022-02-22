
'''
This program takes two csv files as input. In the fist file you have a list of shops/customers and their id.

shop_id,shop_name
2,shop_name_2

In the sencond csv files you have a list of orders placed by some of the shops/customers in the first list. 

order_id,shop_id,cost
1,1,100
2,2,200
3,2,200
4,2,200
5,5,500

This prgramm returns a csv-like output of all orders placed by the shops/customers.

2,shop_name_2,2,200
3,shop_name_2,2,200
4,shop_name_2,2,200

'''


from csv import DictReader
from collections import defaultdict

shops  = open('shops/customer.csv').read().split('\n')
orders = open('orders_by_shop/customer.csv')

shop_dict = defaultdict()

for shop in shops:
    number, name = shop.split(',')
    shop_dict[number] = name

orders = DictReader(orders)

print('order_id,shop_name,shop_id,cost') 
for order in orders:
    if shop_dict.get(order['shop_id'], False):
        print(order['order_id'] + ',' + shop_dict[order['shop_id']] + ',' + order['shop_id'] + ',' + order['cost'])
