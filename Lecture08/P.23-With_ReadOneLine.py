with open("example.txt", "r") as file:
    line = file.readline()
    while line:
        print(line)
        line = file.readline()