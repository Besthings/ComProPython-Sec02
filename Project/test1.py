import struct
import os
import pandas as pd

# Record structure definition without expiry_date
record_format = 'i20sfi20s'  # i=record_id, 20s=name, f=price, i=quantity, 20s=category
record_size = struct.calcsize(record_format)

# ANSI escape codes for colored output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def add_menu_option():
    while True:
        print(f"{Colors.HEADER}\n{'-' * 30}\nChoose Option\n{'-' * 30}{Colors.ENDC}")
        print("1. Add New Menu Item")
        print("2. Back")
        print(f"{Colors.HEADER}{'-' * 30}{Colors.ENDC}")

        sub_choice = input("Please select an option (1-2): ")

        if sub_choice == '1':
            try:
                record_id = int(input("Enter ID: "))
                name = input("Enter Name: ")
                price = float(input("Enter Price: "))
                quantity = int(input("Enter Quantity: "))
                category = input("Enter Category: ")
                add_record('products.bin', record_id, name, price, quantity, category)
                print(f"{Colors.OKGREEN}\nRecord added successfully.{Colors.ENDC}")
            except ValueError:
                print(f"{Colors.FAIL}\nInvalid input. Please try again.{Colors.ENDC}")
        elif sub_choice == '2':
            print(f"{Colors.OKBLUE}\nReturning to main menu...{Colors.ENDC}")
            break
        else:
            print(f"{Colors.FAIL}\nInvalid option. Please select again.{Colors.ENDC}")


def search_record_option():
    while True:
        print(f"{Colors.HEADER}\n{'-' * 30}\nChoose Option\n{'-' * 30}{Colors.ENDC}")
        print("1. Search Record")
        print("2. Back")
        print(f"{Colors.HEADER}{'-' * 30}{Colors.ENDC}")

        sub_choice = input("Please select an option (1-2): ")

        if sub_choice == '1':
            search_id = input("Enter the ID to search (or type 'back' to go back): ")
            if search_id.lower() == 'back':
                break
            try:
                search_id = int(search_id)
                result = find_record('products.bin', search_id)
                if result:
                    print(f"{Colors.OKGREEN}\nRecord found: ID: {result[0]}, Name: {result[1].decode('utf-8').strip()}, "
                          f"Price: {result[2]}, Quantity: {result[3]}, "
                          f"Category: {result[4].decode('utf-8').strip()}{Colors.ENDC}")
                else:
                    print(f"{Colors.FAIL}\nNo record found with the given ID.{Colors.ENDC}")
            except ValueError:
                print(f"{Colors.FAIL}\nInvalid input. Please try again.{Colors.ENDC}")
        elif sub_choice == '2':
            print(f"{Colors.OKBLUE}\nReturning to main menu...{Colors.ENDC}")
            break
        else:
            print(f"{Colors.FAIL}\nInvalid option. Please select again.{Colors.ENDC}")


def update_record_option():
    while True:
        print(f"{Colors.HEADER}\n{'-' * 30}\nChoose Option\n{'-' * 30}{Colors.ENDC}")
        print("1. Update Record")
        print("2. Back")
        print(f"{Colors.HEADER}{'-' * 30}{Colors.ENDC}")

        sub_choice = input("Please select an option (1-2): ")

        if sub_choice == '1':
            search_id = input("Enter the ID to update (or type 'back' to go back): ")
            if search_id.lower() == 'back':
                break
            try:
                search_id = int(search_id)
                record = find_record('products.bin', search_id)
                if record:
                    # Sub-menu for choosing which field to update
                    while True:
                        print(f"{Colors.HEADER}\n{'-' * 30}\nUpdating record with ID: {search_id}\nChoose field to update:{Colors.ENDC}")
                        print("1. Update Name")
                        print("2. Update Price")
                        print("3. Update Quantity")
                        print("4. Update Category")
                        print("5. Update All Fields")
                        print("6. Cancel")
                        print(f"{Colors.HEADER}{'-' * 30}{Colors.ENDC}")

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
                            print(f"{Colors.WARNING}\nCancelling update...{Colors.ENDC}")
                            break
                        else:
                            print(f"{Colors.FAIL}\nInvalid option. Please select again.{Colors.ENDC}")
                            continue
                        
                        # Perform the update
                        update_record('products.bin', search_id, new_name, new_price, new_quantity, new_category)
                        print(f"{Colors.OKGREEN}\nRecord updated successfully.{Colors.ENDC}")
                        break
                else:
                    print(f"{Colors.FAIL}\nNo record found to update.{Colors.ENDC}")
            except ValueError:
                print(f"{Colors.FAIL}\nInvalid input. Please try again.{Colors.ENDC}")
        elif sub_choice == '2':
            print(f"{Colors.OKBLUE}\nReturning to main menu...{Colors.ENDC}")
            break
        else:
            print(f"{Colors.FAIL}\nInvalid option. Please select again.{Colors.ENDC}")


def delete_record_option():
    while True:
        print(f"{Colors.HEADER}\n{'-' * 30}\nChoose Option\n{'-' * 30}{Colors.ENDC}")
        print("1. Delete Record")
        print("2. Back")
        print(f"{Colors.HEADER}{'-' * 30}{Colors.ENDC}")

        sub_choice = input("Please select an option (1-2): ")

        if sub_choice == '1':
            search_id = input("Enter the ID to delete (or type 'back' to go back): ")
            if search_id.lower() == 'back':
                break
            try:
                search_id = int(search_id)
                if find_record('products.bin', search_id):
                    delete_record('products.bin', search_id)
                    print(f"{Colors.OKGREEN}\nRecord deleted successfully.{Colors.ENDC}")
                else:
                    print(f"{Colors.FAIL}\nNo record found to delete.{Colors.ENDC}")
            except ValueError:
                print(f"{Colors.FAIL}\nInvalid ID. Please try again.{Colors.ENDC}")
        elif sub_choice == '2':
            print(f"{Colors.OKBLUE}\nReturning to main menu...{Colors.ENDC}")
            break
        else:
            print(f"{Colors.FAIL}\nInvalid option. Please select again.{Colors.ENDC}")


def generate_report_option():
    while True:
        print(f"{Colors.HEADER}\n{'-' * 30}\nChoose Option\n{'-' * 30}{Colors.ENDC}")
        print("1. Generate Report")
        print("2. Back")
        print(f"{Colors.HEADER}{'-' * 30}{Colors.ENDC}")

        sub_choice = input("Please select an option (1-2): ")

        if sub_choice == '1':
            generate_report('products.bin')
        elif sub_choice == '2':
            print(f"{Colors.OKBLUE}\nReturning to main menu...{Colors.ENDC}")
            break
        else:
            print(f"{Colors.FAIL}\nInvalid option. Please select again.{Colors.ENDC}")


def generate_report(file_name):
    try:
        records = []
        with open(file_name, 'rb') as f:
            while True:
                record_bytes = f.read(record_size)
                if not record_bytes:
                    break
                record = struct.unpack(record_format, record_bytes)
                cleaned_record = (
                    record[0],  # ID
                    record[1].decode('utf-8').rstrip('\x00').strip(),  # Name
                    record[4].decode('utf-8').rstrip('\x00').strip(),  # Category
                    record[2],  # Price
                    record[3]   # Quantity
                )
                records.append(cleaned_record)

        if records:
            # Create a pandas DataFrame
            df = pd.DataFrame(records, columns=['ID', 'Name', 'Category', 'Price', 'Quantity'])

            # Save the DataFrame to a CSV file
            df.to_csv('report.csv', index=False, encoding='utf-8')

            print(f"{Colors.OKGREEN}\nReport generated successfully in 'report.csv'.{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}\nNo records found to generate report.{Colors.ENDC}")

    except FileNotFoundError:
        print(f"{Colors.FAIL}\nThe file {file_name} does not exist.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}\nAn error occurred: {str(e)}{Colors.ENDC}")



def main_menu():
    while True:
        print(f"{Colors.HEADER}\n{'-' * 30}\nMain Menu\n{'-' * 30}{Colors.ENDC}")
        print("1. Add New Item")
        print("2. Read Records")  # Removed the sub-menu for read records
        print("3. Search Record")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Generate Report")
        print("7. Exit")
        print(f"{Colors.HEADER}{'-' * 30}{Colors.ENDC}")

        choice = input("Please select an option (1-7): ")

        if choice == '1':
            add_menu_option()
        elif choice == '2':
            read_records('products.bin')  # Directly call the read_records function
        elif choice == '3':
            search_record_option()
        elif choice == '4':
            update_record_option()
        elif choice == '5':
            delete_record_option()
        elif choice == '6':
            generate_report_option()
        elif choice == '7':
            print(f"{Colors.OKBLUE}\nExiting the program...{Colors.ENDC}")
            break
        else:
            print(f"{Colors.FAIL}\nInvalid option. Please select again.{Colors.ENDC}")



# Example functions to add, read, search, update, and delete records
def add_record(file_name, record_id, name, price, quantity, category):
    with open(file_name, 'ab') as f:
        f.write(struct.pack(record_format, record_id, name.encode('utf-8'), price, quantity, category.encode('utf-8')))


def read_records(file_name):
    if os.path.exists(file_name):
        records = []
        
        with open(file_name, 'rb') as f:
            while True:
                record_bytes = f.read(record_size)
                if not record_bytes:
                    break
                record = struct.unpack(record_format, record_bytes)
                cleaned_record = (
                    record[0],  # ID
                    record[1].decode('utf-8').rstrip('\x00').strip(),  # Name
                    record[2],  # Price
                    record[3],  # Quantity
                    record[4].decode('utf-8').rstrip('\x00').strip()  # Category
                )
                records.append(cleaned_record)

        if records:
            # Create a pandas DataFrame
            df = pd.DataFrame(records, columns=['ID', 'Name', 'Price', 'Quantity', 'Category'])

            # Group by Category
            grouped = df.groupby('Category')

            total_inventory_value = 0
            total_inventory_quantity = 0

            for category, group in grouped:
                category_total_value = (group['Price'] * group['Quantity']).sum()
                category_total_quantity = group['Quantity'].sum()
                total_inventory_value += category_total_value
                total_inventory_quantity += category_total_quantity
                
                print(f"{Colors.OKGREEN}\nหมวดหมู่: {category}{Colors.ENDC}")
                print(f"{Colors.HEADER}{'-' * 60}{Colors.ENDC}")
                print(f"ID    Name                         Price         Quantity")
                print(f"{Colors.HEADER}{'-' * 60}{Colors.ENDC}")

                for _, row in group.iterrows():
                    print(f"{row['ID']:<5} {row['Name']:<25} {row['Price']:>7} {row['Quantity']:>10}")

                print(f"{Colors.HEADER}{'-' * 60}{Colors.ENDC}")
                print(f"รวมหมวดหมู่ {category} -> ราคารวม: {category_total_value:.2f}, จำนวนรวม: {category_total_quantity}")
                print(f"{Colors.OKGREEN}{'=' * 60}{Colors.ENDC}")

            # Print overall totals
            print(f"{Colors.HEADER}\nสรุปรวมทั้งหมด{Colors.ENDC}")
            print(f"{Colors.HEADER}{'-' * 60}{Colors.ENDC}")
            print(f"ราคารวมทั้งหมด: {total_inventory_value:.2f}")
            print(f"จำนวนรวมทั้งหมด: {total_inventory_quantity}")
            print(f"{Colors.HEADER}{'-' * 60}{Colors.ENDC}")

        else:
            print(f"{Colors.FAIL}\nNo records found.{Colors.ENDC}")
    else:
        print(f"{Colors.FAIL}\nFile not found: {file_name}.{Colors.ENDC}")



def find_record(file_name, record_id):
    with open(file_name, 'rb') as f:
        while True:
            record_bytes = f.read(record_size)
            if not record_bytes:
                break
            record = struct.unpack(record_format, record_bytes)
            if record[0] == record_id:
                return record
    return None


def update_record(file_name, record_id, new_name, new_price, new_quantity, new_category):
    records = []
    updated = False
    with open(file_name, 'rb') as f:
        while True:
            record_bytes = f.read(record_size)
            if not record_bytes:
                break
            record = struct.unpack(record_format, record_bytes)
            if record[0] == record_id:
                record = (record_id, new_name.encode('utf-8'), new_price, new_quantity, new_category.encode('utf-8'))
                updated = True
            records.append(record)

    if updated:
        with open(file_name, 'wb') as f:
            for record in records:
                f.write(struct.pack(record_format, *record))


def delete_record(file_name, record_id):
    records = []
    with open(file_name, 'rb') as f:
        while True:
            record_bytes = f.read(record_size)
            if not record_bytes:
                break
            record = struct.unpack(record_format, record_bytes)
            if record[0] != record_id:
                records.append(record)

    with open(file_name, 'wb') as f:
        for record in records:
            f.write(struct.pack(record_format, *record))

if __name__ == "__main__":
    if os.path.exists('products.bin'):
        os.remove('products.bin')
        print(f"{Colors.WARNING}Deleted 'products.bin' file.")

        # เพิ่มข้อมูลเริ่มต้นลงในไฟล์ products.bin
        add_record('products.bin', 1, "Pad kaprao", 60, 2, "Thai cuisine")
        add_record('products.bin', 2, "Pad Thai", 60, 2, "Thai cuisine")
        add_record('products.bin', 3, "Sushi", 90, 12, "Japanese cuisine")
        add_record('products.bin', 4, "Udon", 160, 4, "Japanese cuisine")
        add_record('products.bin', 5, "Carbonara", 199, 1, "Italian cuisine")
        add_record('products.bin', 6, "Lasagna", 369, 2, "Italian cuisine")
        add_record('products.bin', 7, "Fried Rice", 229, 2, "Chinese cuisine")
        add_record('products.bin', 8, "Peking Duck", 669, 2, "Chinese cuisine")
        
        print("Add Simple of Record.")
        main_menu()
