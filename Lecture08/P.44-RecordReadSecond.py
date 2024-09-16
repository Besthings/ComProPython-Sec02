import struct

# Define the format string
record_format = 'i20sif'
record_size = struct.calcsize(record_format)

# Open the binary file for reading
with open("records.bin", "rb") as file:
    # Skip the first record
    file.seek(record_size)
    # Read the second record
    data = file.read(record_size)
    # Unpack the data back into a tuple
    record = struct.unpack(record_format, data)
    # Decode the string field and remove trailing null bytes
    record = (record[0], record[1].decode().strip('\x00'), record[2], record[3])

    print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, GPA: {record[3]:.2f}")
