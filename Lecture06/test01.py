def add_item(inventory, item_name, quantity, price):
    # Check if the item already exists in the inventory
    for item in inventory:
        if item[0] == item_name:
            item[1] += quantity
            return
    
    # If the item does not exist, add it to the inventory
    inventory.append([item_name, quantity, price])

# Example usage
update_inventory(inventory, "Banana", 20)
print("Inventory after update:")
print(inventory)

add_item(inventory, "Eggs", 30, 0.25)
print("Inventory after adding eggs:")
print(inventory)

calculate_total_value(inventory)
find_most_expensive(inventory)