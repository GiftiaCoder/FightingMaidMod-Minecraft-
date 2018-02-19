import struct

def read_str(file, total_b = ''):
    for i in range(9):
        b_str = format(struct.unpack('<B', file.read(1))[0], '08b')
        total_b = b_str[1:] + total_b
        if b_str[0] == '0':
            break
    return file.read(int(total_b, 2)).decode('utf-8')

def read_int(file):
    return struct.unpack('<i', file.read(4))[0]

def read_ushort(file):
    return struct.unpack('<H', file.read(2))[0]

def read_float(file):
    return struct.unpack('<f', file.read(4))[0]

def read_byte(file):
    return struct.unpack('<B', file.read(1))[0]

def read_array(file, size, func):
    float_array = []
    for i in range(size):
        float_array.append(func(file))
    return float_array

def read_bytes(file, size):
    return file.read(size)