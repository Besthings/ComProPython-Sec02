def format_strings(*args):
    Upper_strings = "" # สร้าง
    for arg in args:
        # แปลง arg เป็นตัวพิมพ์ใหญ่และเปลี่ยนช่องว่างเป็นขีดกลาง
        arg = arg.upper().replace(" ", "-")
        Upper_strings += arg  # ต่อสตริงเข้าด้วยกัน
    return Upper_strings

if __name__ == '__main__':
    result = format_strings("Hello", "world","this","is","a","test")
    print(result)  # Output: "HELLOWORLDTHISISATEST"

    result = format_strings("Python", "is", "fun")
    print(result)  # Output: "PYTHONISFUN"

    result = format_strings("Hello World")
    print(result)  # Output: "HELLO-WORLD"