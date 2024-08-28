def analyze_purchases(purchases: list) -> dict:
    customer_dict = {}
    product_count = {}

    for customer_id, product_category, product_name in purchases:
        if customer_id not in customer_dict:
            customer_dict[customer_id] = {}
        
        if product_category not in customer_dict[customer_id]:
            customer_dict[customer_id][product_category] = {}
        
        if product_category not in product_count:
            product_count[product_category] = {}

        if product_name in customer_dict[customer_id][product_category]:
            customer_dict[customer_id][product_category][product_name] += 1
        else:
            customer_dict[customer_id][product_category][product_name] = 1
        
        if product_name in product_count[product_category]:
            product_count[product_category][product_name] += 1
        else:
            product_count[product_category][product_name] = 1

    result = {}

    for customer_id in customer_dict:
        result[customer_id] = {}
        for category in customer_dict[customer_id]:
            repeated_purchases = sum(count for count in customer_dict[customer_id][category].values() if count > 1)
            if repeated_purchases > 0:
                result[customer_id][category] = repeated_purchases

    most_frequent = {}
    for category in product_count:
        # Sort products first by frequency (descending) and then alphabetically
        sorted_products = sorted(product_count[category].items(), key=lambda x: (-x[1], x[0]))
        most_frequent[category] = sorted_products[0][0]  # Get the product with highest frequency

    result["most_frequent"] = most_frequent

    return result

purchases = [
    ("cust1", "electronics", "laptop"),
    ("cust2", "groceries", "apple"),
    ("cust1", "electronics", "laptop"),
    ("cust1", "electronics", "mouse"),
    ("cust2", "groceries", "apple"),
    ("cust2", "groceries", "banana"),
    ("cust3", "groceries", "banana"),
    ("cust3", "groceries", "apple"),
    ("cust3", "electronics", "camera"),
]

print(analyze_purchases(purchases))
# Expect output:
# {
# "cust1": {
# "electronics": 2
# },
# "cust2": {
# "groceries": 2
# },
# "cust3": {},
# "most_frequent": {
# "electronics": "laptop",
# "groceries": "apple"
# }
# }