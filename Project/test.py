import struct
import os

# กำหนดโครงสร้างข้อมูลใหม่ โดยเอา expiry_date ออก
record_format = 'i20sfi20s'  # i=record_id, 20s=name, f=price, i=quantity, 20s=category
record_size = struct.calcsize(record_format)

def add_menu_option():
    while True:
        print("\n" + "-" * 30)
        print("Choose Option")
        print("-" * 30)
        print("1. Add New Menu Item")
        print("2. Back")
        print("-" * 30)
        
        sub_choice = input("Please select an option (1-2): ")
        
        if sub_choice == '1':
            try:
                record_id = int(input("Enter ID: "))
                name = input("Enter Name: ")
                price = float(input("Enter Price: "))
                quantity = int(input("Enter Quantity: "))
                category = input("Enter Category: ")
                add_record('products.bin', record_id, name, price, quantity, category)
                print("\nRecord added successfully.")
            except ValueError:
                print("\nInvalid input. Please try again.")
        elif sub_choice == '2':
            print("\nReturning to main menu...")
            break
        else:
            print("\nInvalid option. Please select again.")

def read_records_option():
    while True:
        print("\n" + "-" * 30)
        print("Choose Option")
        print("-" * 30)
        print("1. Show All Records")
        print("2. Back")
        print("-" * 30)
        
        sub_choice = input("Please select an option (1-2): ")
        
        if sub_choice == '1':
            read_records('products.bin')
        elif sub_choice == '2':
            print("\nReturning to main menu...")
            break
        else:
            print("\nInvalid option. Please select again.")

def search_record_option():
    while True:
        print("\n" + "-" * 30)
        print("Choose Option")
        print("-" * 30)
        print("1. Search Record")
        print("2. Back")
        print("-" * 30)

        sub_choice = input("Please select an option (1-2): ")

        if sub_choice == '1':
            try:
                search_id = input("Enter the ID to search (or type 'back' to go back): ")
                if search_id.lower() == 'back':
                    break
                search_id = int(search_id)
                result = find_record('products.bin', search_id)
                if result:
                    print(f"\nRecord found: ID: {result[0]}, Name: {result[1].decode('utf-8').strip()}, "
                          f"Price: {result[2]}, Quantity: {result[3]}, "
                          f"Category: {result[4].decode('utf-8').strip()}")
                else:
                    print("\nNo record found with the given ID.")
            except ValueError:
                print("\nInvalid input. Please try again.")
        elif sub_choice == '2':
            print("\nReturning to main menu...")
            break
        else:
            print("\nInvalid option. Please select again.")

def update_record_option():
    while True:
        print("\n" + "-" * 30)
        print("Choose Option")
        print("-" * 30)
        print("1. Update Record")
        print("2. Back")
        print("-" * 30)

        sub_choice = input("Please select an option (1-2): ")

        if sub_choice == '1':
            try:
                search_id = input("Enter the ID to update (or type 'back' to go back): ")
                if search_id.lower() == 'back':
                    break
                search_id = int(search_id)
                record = find_record('products.bin', search_id)
                if record:
                    # Sub-menu for choosing which field to update
                    while True:
                        print("\n" + "-" * 30)
                        print(f"Updating record with ID: {search_id}")
                        print("Choose field to update:")
                        print("1. Update Name")
                        print("2. Update Price")
                        print("3. Update Quantity")
                        print("4. Update Category")
                        print("5. Update All Fields")
                        print("6. Cancel")
                        print("-" * 30)

                        update_choice = input("Please select an option (1-6): ")

                        new_name = record[1].decode('utf-8').strip()
                        new_price = record[2]
                        new_quantity = record[3]
                        new_category = record[4].decode('utf-8').strip()

                        if update_choice == '1':
                            new_name = input("Enter new Name: ")
                        elif update_choice == '2':
                            new_price = float(input("Enter new Price: "))
                        elif update_choice == '3':
                            new_quantity = int(input("Enter new Quantity: "))
                        elif update_choice == '4':
                            new_category = input("Enter new Category: ")
                        elif update_choice == '5':
                            new_name = input("Enter new Name: ")
                            new_price = float(input("Enter new Price: "))
                            new_quantity = int(input("Enter new Quantity: "))
                            new_category = input("Enter new Category: ")
                        elif update_choice == '6':
                            print("\nCancelling update...")
                            break
                        else:
                            print("\nInvalid option. Please select again.")
                            continue
                        
                        # Perform the update
                        update_record('products.bin', search_id, new_name, new_price, new_quantity, new_category)
                        print("\nRecord updated successfully.")
                        break
                else:
                    print("\nNo record found to update.")
            except ValueError:
                print("\nInvalid input. Please try again.")
        elif sub_choice == '2':
            print("\nReturning to main menu...")
            break
        else:
            print("\nInvalid option. Please select again.")


def delete_record_option():
    while True:
        print("\n" + "-" * 30)
        print("Choose Option")
        print("-" * 30)
        print("1. Delete Record")
        print("2. Back")
        print("-" * 30)

        sub_choice = input("Please select an option (1-2): ")

        if sub_choice == '1':
            try:
                search_id = input("Enter the ID to delete (or type 'back' to go back): ")
                if search_id.lower() == 'back':
                    break
                search_id = int(search_id)
                if find_record('products.bin', search_id):
                    delete_record('products.bin', search_id)
                    print("\nRecord deleted successfully.")
                else:
                    print("\nNo record found to delete.")
            except ValueError:
                print("\nInvalid ID. Please try again.")
        elif sub_choice == '2':
            print("\nReturning to main menu...")
            break
        else:
            print("\nInvalid option. Please select again.")

def generate_report_option():
    while True:
        print("\n" + "-" * 30)
        print("Choose Option")
        print("-" * 30)
        print("1. Generate Report")
        print("2. Back")
        print("-" * 30)

        sub_choice = input("Please select an option (1-2): ")

        if sub_choice == '1':
            generate_report('products.bin', 'report.csv')
            print("\nReport generated as 'report.csv'.")
        elif sub_choice == '2':
            print("\nReturning to main menu...")
            break
        else:
            print("\nInvalid option. Please select again.")

def add_record(file_name, record_id, name, price, quantity, category):
    name = name.ljust(20)[:20].encode('utf-8')
    category = category.ljust(20)[:20].encode('utf-8')  # ปรับเป็น 20 ตัวอักษร
    with open(file_name, 'ab') as f:
        packed_data = struct.pack(record_format, record_id, name, price, quantity, category)
        f.write(packed_data)

def read_records(file_name):
    if not os.path.exists(file_name):
        print("ไฟล์ไม่พบ กรุณาเพิ่มข้อมูลก่อน.")
        return
    
    records_by_category = {}
    total_price = 0
    total_quantity = 0

    with open(file_name, 'rb') as f:
        while chunk := f.read(record_size):
            if len(chunk) == record_size:
                try:
                    record = struct.unpack(record_format, chunk)
                    category = record[4].decode('utf-8').strip()

                    # จัดเก็บข้อมูลแยกตามหมวดหมู่
                    if category not in records_by_category:
                        records_by_category[category] = []
                    records_by_category[category].append(record)

                except UnicodeDecodeError as e:
                    print(f"ข้อผิดพลาดในการถอดรหัสข้อมูล: {e}")
            else:
                print(f"พบข้อมูลที่มีขนาดไม่ถูกต้อง: {len(chunk)} ไบต์, ต้องการ {record_size} ไบต์")

    # แสดงข้อมูลแยกตามหมวดหมู่ และรวมราคาและจำนวน
    if records_by_category:
        for category, records in records_by_category.items():
            category_total_price = 0
            category_total_quantity = 0

            print(f"\nหมวดหมู่: {category}")
            print("-" * 60)
            print(f"{'ID':<5}{'Name':<25}{'Price':<10}{'Quantity':<10}")
            print("-" * 60)

            for record in records:
                category_total_price += record[2] * record[3]  # ราคารวมในหมวดหมู่ (Price * Quantity)
                category_total_quantity += record[3]  # จำนวนรวมในหมวดหมู่

                print(f"{record[0]:<5}{record[1].decode('utf-8').strip():<25}{record[2]:<10}{record[3]:<10}")

            print("-" * 60)
            print(f"รวมหมวดหมู่ {category} -> ราคารวม: {category_total_price:.2f}, จำนวนรวม: {category_total_quantity}")
            print("=" * 60)

            # รวมราคาและจำนวนทั้งหมดทุกหมวดหมู่
            total_price += category_total_price
            total_quantity += category_total_quantity

        # แสดงราคารวมและจำนวนรวมทั้งหมด
        print("\nสรุปรวมทั้งหมด")
        print("-" * 60)
        print(f"ราคารวมทั้งหมด: {total_price:.2f}")
        print(f"จำนวนรวมทั้งหมด: {total_quantity}")
        print("-" * 60)
    else:
        print("ไม่มีข้อมูลในไฟล์")


def find_record(file_name, search_id):
    if not os.path.exists(file_name):
        print("ไฟล์ไม่พบ กรุณาเพิ่มข้อมูลก่อน.")
        return None
    
    with open(file_name, 'rb') as f:
        while chunk := f.read(record_size):
            if len(chunk) == record_size:
                try:
                    record = struct.unpack(record_format, chunk)
                    if record[0] == search_id:
                        return record
                except UnicodeDecodeError:
                    continue
    return None

def update_record(file_name, search_id, new_name, new_price, new_quantity, new_category):
    if not os.path.exists(file_name):
        print("ไฟล์ไม่พบ กรุณาเพิ่มข้อมูลก่อน.")
        return
    
    records = []
    new_name = new_name.ljust(20)[:20].encode('utf-8')
    new_category = new_category.ljust(20)[:20].encode('utf-8')  # ปรับเป็น 20 ตัวอักษร
    
    with open(file_name, 'rb') as f:
        while chunk := f.read(record_size):
            if len(chunk) == record_size:
                try:
                    record = struct.unpack(record_format, chunk)
                    if record[0] == search_id:
                        record = (search_id, new_name, new_price, new_quantity, new_category)
                    records.append(record)
                except UnicodeDecodeError:
                    continue

    with open(file_name, 'wb') as f:
        for record in records:
            try:
                f.write(struct.pack(record_format, *record))
            except struct.error as e:
                print(f"ข้อผิดพลาดในการเขียนข้อมูล: {e}")

def delete_record(file_name, search_id):
    if not os.path.exists(file_name):
        print("ไฟล์ไม่พบ กรุณาเพิ่มข้อมูลก่อน.")
        return
    
    records = []
    with open(file_name, 'rb') as f:
        while chunk := f.read(record_size):
            if len(chunk) == record_size:
                try:
                    record = struct.unpack(record_format, chunk)
                    if record[0] != search_id:
                        records.append(record)
                except UnicodeDecodeError:
                    continue

    with open(file_name, 'wb') as f:
        for record in records:
            try:
                f.write(struct.pack(record_format, *record))
            except struct.error as e:
                print(f"ข้อผิดพลาดในการเขียนข้อมูล: {e}")


def generate_report(file_name, output_file):
    import pandas as pd
    if not os.path.exists(file_name):
        print("ไฟล์ไม่พบ กรุณาเพิ่มข้อมูลก่อน.")
        return
    
    records = []

    with open(file_name, 'rb') as f:
        while chunk := f.read(record_size):
            if len(chunk) == record_size:
                try:
                    record = struct.unpack(record_format, chunk)
                    records.append({
                        'ID': record[0],
                        'Name': record[1].decode('utf-8').strip(),
                        'Price': record[2],
                        'Quantity': record[3],
                        'Category': record[4].decode('utf-8').strip()
                    })
                except UnicodeDecodeError as e:
                    print(f"ข้อผิดพลาดในการถอดรหัสข้อมูล: {e}")

    # Convert the records list into a DataFrame
    df = pd.DataFrame(records)

    # Save the DataFrame to a CSV file with a nice format
    df.to_csv(output_file, index=False, encoding='utf-8')

    print(f"\nReport generated as '{output_file}' with formatted table.")

def menu():
    while True:
        print("\n" + "-" * 30)
        print("Main Menu")
        print("-" * 30)
        print("1. Add Menu")
        print("2. Read Records")
        print("3. Search Record")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Generate Report")
        print("7. Exit")
        print("-" * 30)
        
        choice = input("Please select an option (1-7): ")

        if choice == '1':
            add_menu_option()
        elif choice == '2':
            read_records_option()
        elif choice == '3':
            search_record_option()
        elif choice == '4':
            update_record_option()
        elif choice == '5':
            delete_record_option()
        elif choice == '6':
            generate_report_option()
        elif choice == '7':
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please select again.")


if __name__ == "__main__":
    if os.path.exists('products.bin'):
        os.remove('products.bin')
        print("ลบไฟล์ products.bin เก่าเรียบร้อยแล้ว.")

    # เพิ่มข้อมูลเริ่มต้นลงในไฟล์ products.bin
    add_record('products.bin', 1, "Pad kaprao", 60, 2, "Thai cuisine")
    add_record('products.bin', 2, "Pad Thai", 60, 2, "Thai cuisine")
    add_record('products.bin', 3, "Sushi", 90, 12, "Japanese cuisine")
    add_record('products.bin', 4, "Udon", 160, 4, "Japanese cuisine")
    add_record('products.bin', 5, "Carbonara", 199, 1, "Italian cuisine")
    add_record('products.bin', 6, "Lasagna", 369, 2, "Italian cuisine")
    add_record('products.bin', 7, "Fried Rice", 229, 2, "Chinese cuisine")
    add_record('products.bin', 8, "Peking Duck", 669, 2, "Chinese cuisine")
    
    print("ข้อมูลเริ่มต้นถูกเพิ่มเรียบร้อยแล้ว.")
    
    menu()
