'''
This program takes JSON lists of order statuses of a system. It checks whether this incomming placements and check wheater orders are valid and 
result in an feasible order. This means the order is not empty, negative (in quantity of a good) or canceled. There can be different orders in one
incomming file orderstatement not in cronological order.
Check example three. The last order update make the order empty. Hence the program will not consider it in it's output.
----------------------------
[
	{
		"event_id": 1,
		"order_id": 1,
		"item_id": 1,
		"count": 1,
		"return_count": 0,
		"status": "OK"
	},
	{
		"event_id": 2,
		"order_id": 1,
		"item_id": 1,
		"count": 1,
		"return_count": 0,
		"status": "CANCEL"
	}
]
----------------------------
[
	{
		"event_id": 2,
		"order_id": 1,
		"item_id": 1,
		"count": 2,
		"return_count": 1,
		"status": "OK"
	},
	{
		"event_id": 1,
		"order_id": 1,
		"item_id": 1,
		"count": 2,
		"return_count": 0,
		"status": "OK"
	}
]
----------------------------
[
	{
		"event_id": 2,
		"order_id": 2,
		"item_id": 1,
		"count": 3,
		"return_count": 1,
		"status": "OK"
	},
	{
		"event_id": 1,
		"order_id": 1,
		"item_id": 1,
		"count": 2,
		"return_count": 0,
		"status": "OK"
	},
	{
		"event_id": 3,
		"order_id": 3,
		"item_id": 1,
		"count": 2,
		"return_count": 2,
		"status": "OK"
	}
]
'''

from collections import defaultdict
import json


input_file = open('input.txt').read().replace('\n', '')
events     = json.loads(input_file)

orders = defaultdict()

for i in range(len(events)):

    current_order_id = events[i]['order_id']
    current_event_id = events[i]['event_id']
    current_status   = events[i]['status']
    current_count    = events[i]['count']
    current_recount  = events[i]['return_count']

    # create new order if it does not exist AND is not on canceled 
    if current_order_id not in orders.keys() and current_status != 'CANCEL' and current_count - current_recount > 0:
        orders[current_order_id] = (current_event_id,i)
    
    # update order IF it is a new update/event
    if orders[current_order_id][0] < current_event_id:
        orders[current_order_id] = (current_event_id,i)
        
        # Deleat it IF it was canceled
        if current_status == 'CANCEL' or current_count - current_recount <= 0:
            del orders[current_order_id]

orders_out = []

for final_order in orders:

    fin_evn   = events[orders[final_order][1]]
    quantitiy = fin_evn['count'] - fin_evn['return_count']

    orders_out.append({'id': fin_evn['order_id'], 'items': [{'count': quantitiy, 'id': fin_evn['item_id']}]})

#You need to have an output file exisisting in your current folder
open('output.txt', 'a').write(json.dumps(orders_out, indent=4))
