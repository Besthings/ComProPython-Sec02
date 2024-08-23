def analyze_purchases(purchases: list) -> dict:
    pass

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