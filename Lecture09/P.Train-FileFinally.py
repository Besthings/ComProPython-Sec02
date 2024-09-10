filename = input("Enter a filename: ")
try:
    infile = open(filename, 'r')
    infile.close()
except IOError:
    print("An error occurred trying to read ", end="")
    print("the file", filename,)
else:
    contents = infile.read()
finally:
    print(contents)

print("End of program")