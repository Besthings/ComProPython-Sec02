inventory = [["Apple", 50, 0.75],
             ["Banana", 100, 0.50],
             ["Orange", 75, 0.85]
]

def update_inventory(inventory, item_name, quantify_sold):
    for item in inventory:
        if item_name == item[0]:
            item[1] = item[1] - quantify_sold

def calculate_total_value(inventory):
    total = 0
    for values in inventory:
        apple = values[0:1] * values[0:2]
        total = total + apple
        print(total)



update_inventory(inventory, "Banana", 20)
print(inventory)

calculate_total_value(inventory)