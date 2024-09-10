def divide(a,b):
    try:
        result = a / b
    except ZeroDivisionError:
        return"Exception: "
    except ValueError:
        return"Error"
    except Exception:
        return"Exception: "
    else:
        return result
    
a,b = map(int, input().split())
print(divide(a,b))
print("End of program")