columns = int(input("Enter columns: "))

for i in range(1, 101, 1):
    print(i, "",end="")

    if i % columns ==0:
        print()