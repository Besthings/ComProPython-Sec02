import struct

# Open the binary file for reading
with open("records.bin", "rb") as file:
    # Read the binary data from the file
    data = file.read(struct.calcsize('i20sif'))
    # Unpack the data back into a tuple
    record = struct.unpack('i20sif', data)
    # Decode the string field and remove trailing null bytes
    record = (record[0], record[1].decode().strip('\x00'), record[2], record[3])
    print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, GPA: {record[3]}")
