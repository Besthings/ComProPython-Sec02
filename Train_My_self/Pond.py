times = 4
store_negative = []
store_positive = []
store_zero = []
print("Enter the total number: 4")

def Enternums():
    count = 0
    while count < times:
        a = int(input(f"Enter number {count+1} : "))
        if a < 0:
            store_negative.append(a)
        elif a > 0:
            store_positive.append(a)
        elif a == 0:
            store_zero.append(a)
        count += 1

    print(f"Positive {store_positive} : {len(store_positive)}")
    print(f"Negative {store_negative} : {len(store_negative)}")
    print(f"Zero : {len(store_zero)}")
    
Enternums()