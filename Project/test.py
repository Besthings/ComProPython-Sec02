import struct
import os

# กำหนดโครงสร้างข้อมูล
record_format = 'i20sfi10s10s'  # i=record_id, 20s=name, f=price, i=quantity, 10s=category, 10s=expiry_date
record_size = struct.calcsize(record_format)

def add_record(file_name, record_id, name, price, quantity, category, expiry_date):
    name = name.ljust(20)[:20].encode('utf-8')
    category = category.ljust(10)[:10].encode('utf-8')
    expiry_date = expiry_date.ljust(10)[:10].encode('utf-8')
    
    with open(file_name, 'ab') as f:
        packed_data = struct.pack(record_format, record_id, name, price, quantity, category, expiry_date)
        f.write(packed_data)

def read_records(file_name):
    if not os.path.exists(file_name):
        print("ไฟล์ไม่พบ กรุณาเพิ่มข้อมูลก่อน.")
        return
    
    with open(file_name, 'rb') as f:
        while chunk := f.read(record_size):
            if len(chunk) == record_size:
                try:
                    record = struct.unpack(record_format, chunk)
                    print(f"ID: {record[0]}, Name: {record[1].decode('utf-8').strip()}, "
                          f"Price: {record[2]}, Quantity: {record[3]}, "
                          f"Category: {record[4].decode('utf-8').strip()}, "
                          f"Expiry: {record[5].decode('utf-8').strip()}")
                except UnicodeDecodeError as e:
                    print(f"ข้อผิดพลาดในการถอดรหัสข้อมูล: {e}")
            else:
                print(f"พบข้อมูลที่มีขนาดไม่ถูกต้อง: {len(chunk)} ไบต์, ต้องการ {record_size} ไบต์")

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

def update_record(file_name, search_id, new_name, new_price, new_quantity, new_category, new_expiry_date):
    if not os.path.exists(file_name):
        print("ไฟล์ไม่พบ กรุณาเพิ่มข้อมูลก่อน.")
        return
    
    records = []
    new_name = new_name.ljust(20)[:20].encode('utf-8')
    new_category = new_category.ljust(10)[:10].encode('utf-8')
    new_expiry_date = new_expiry_date.ljust(10)[:10].encode('utf-8')
    
    with open(file_name, 'rb') as f:
        while chunk := f.read(record_size):
            if len(chunk) == record_size:
                try:
                    record = struct.unpack(record_format, chunk)
                    if record[0] == search_id:
                        record = (search_id, new_name, new_price, new_quantity, new_category, new_expiry_date)
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
    if not os.path.exists(file_name):
        print("ไฟล์ไม่พบ กรุณาเพิ่มข้อมูลก่อน.")
        return
    
    with open(file_name, 'rb') as f, open(output_file, 'w', encoding='utf-8') as out:
        out.write("ID,Name,Price,Quantity,Category,Expiry Date\n")
        while chunk := f.read(record_size):
            if len(chunk) == record_size:
                try:
                    record = struct.unpack(record_format, chunk)
                    out.write(f"{record[0]},{record[1].decode('utf-8').strip()}," 
                              f"{record[2]},{record[3]},{record[4].decode('utf-8').strip()}," 
                              f"{record[5].decode('utf-8').strip()}\n")
                except UnicodeDecodeError as e:
                    print(f"ข้อผิดพลาดในการถอดรหัสข้อมูล: {e}")

def menu():
    while True:
        print("\n--- เมนูหลัก ---")
        print("1. เพิ่มข้อมูลใหม่")
        print("2. แสดงข้อมูลทั้งหมด")
        print("3. ค้นหาข้อมูล")
        print("4. อัปเดตข้อมูล")
        print("5. ลบข้อมูล")
        print("6. สร้างรายงาน")
        print("7. ปิดโปรแกรม")
        
        choice = input("เลือกเมนู (1-7): ")
        
        if choice == '1':
            try:
                record_id = int(input("ID: "))
                name = input("ชื่ออาหาร: ")
                price = float(input("ราคา: "))
                quantity = int(input("จำนวน: "))
                category = input("ประเภท: ")
                expiry_date = input("วันหมดอายุ (YYYY-MM-DD): ")
                add_record('products.bin', record_id, name, price, quantity, category, expiry_date)
                print("เพิ่มข้อมูลเรียบร้อยแล้ว.")
            except ValueError:
                print("ข้อมูลที่ป้อนไม่ถูกต้อง กรุณาลองใหม่.")
        elif choice == '2':
            read_records('products.bin')
        elif choice == '3':
            try:
                search_id = int(input("ป้อนรหัสที่ต้องการค้นหา: "))
                result = find_record('products.bin', search_id)
                if result:
                    print(f"พบข้อมูล: ID: {result[0]}, Name: {result[1].decode('utf-8').strip()}, "
                          f"Price: {result[2]}, Quantity: {result[3]}, "
                          f"Category: {result[4].decode('utf-8').strip()}, "
                          f"Expiry: {result[5].decode('utf-8').strip()}")
                else:
                    print("ไม่พบข้อมูล")
            except ValueError:
                print("รหัสที่ป้อนไม่ถูกต้อง กรุณาลองใหม่.")
        elif choice == '4':
            try:
                search_id = int(input("ป้อนรหัสที่ต้องการอัปเดต: "))
                if find_record('products.bin', search_id):
                    new_name = input("ชื่อใหม่: ")
                    new_price = float(input("ราคาใหม่: "))
                    new_quantity = int(input("จำนวนใหม่: "))
                    new_category = input("ประเภทใหม่: ")
                    new_expiry_date = input("วันหมดอายุใหม่ (YYYY-MM-DD): ")
                    update_record('products.bin', search_id, new_name, new_price, new_quantity, new_category, new_expiry_date)
                    print("อัปเดตข้อมูลเรียบร้อยแล้ว.")
                else:
                    print("ไม่พบข้อมูลที่ต้องการอัปเดต")
            except ValueError:
                print("ข้อมูลที่ป้อนไม่ถูกต้อง กรุณาลองใหม่.")
        elif choice == '5':
            try:
                search_id = int(input("ป้อนรหัสที่ต้องการลบ: "))
                if find_record('products.bin', search_id):
                    delete_record('products.bin', search_id)
                    print("ลบข้อมูลเรียบร้อยแล้ว.")
                else:
                    print("ไม่พบข้อมูลที่ต้องการลบ")
            except ValueError:
                print("รหัสที่ป้อนไม่ถูกต้อง กรุณาลองใหม่.")
        elif choice == '6':
            generate_report('products.bin', 'report.csv')
            print("รายงานถูกสร้างในไฟล์ report.csv")
        elif choice == '7':
            print("ปิดโปรแกรม...")
            break
        else:
            print("เลือกเมนูไม่ถูกต้อง กรุณาเลือกใหม่.")

if __name__ == "__main__":
    if os.path.exists('products.bin'):
        os.remove('products.bin')
        print("ลบไฟล์ products.bin เก่าเรียบร้อยแล้ว.")
    
    menu()
