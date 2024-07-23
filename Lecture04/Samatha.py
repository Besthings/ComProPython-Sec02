keep_going = "y"

while keep_going == "y":
    wholesale = float(input("Enter the itesm's wholesale cost: "))
    retail_price = wholesale * 2.5
    print(f"Retail Price: ${retail_price:.2f}")

    keep_going = (input("Do you have another items?  (Enter y for yes): " ))