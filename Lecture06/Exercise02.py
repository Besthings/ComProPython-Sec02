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
    for item in inventory:
        item_value = item[1] * item[2]  # คำนวณมูลค่าของผลไม้แต่ละชนิด
        total += item_value
        print(f"{item[0]} value: ${item_value:.2f}")
    print(f"Total inventory value: ${total:.2f}")

def find_most_expensive(inventory):
    name_item = None
    Highest_price = 0
    for item in inventory:
        if item[2] > Highest_price:
            Highest_price = item[2]
            name_item = item
    print(f"The Highest Price is {name_item[0]} : {Highest_price} $")

def add_item(inventory, item_name, quantify_sold, price):
    for item in inventory:
        if item[0] == item_name or inventory:
            item[1] += quantify_sold
            item[2] += price
            return
        
    inventory.append([item_name, quantify_sold, price])
    
    

# update_inventory(inventory, "Banana", 20)
# print(inventory)
print(inventory)
add_item(inventory, "orange", 5, 0.85)
print(inventory)