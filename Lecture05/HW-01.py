def format_strings(*args):
    for arg in args:
        upper_char = arg.upper() 
        return upper_char

if __name__ == '__main__':
    result = format_strings("Hello""world""this""is""a""test")
    print(result)  # Output: "HELLOWORLDTHISISATEST"

    result = format_strings("Python""is""fun")
    print(result)  # Output: "PYTHONISFUN"
