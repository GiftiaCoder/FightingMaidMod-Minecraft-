import struct
import enum

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

class type(enum.Enum):
    char = 'char'
    byte = 'byte'
    short = 'short'
    ushort = 'ushort'
    int = 'int'
    uint = 'uint'
    long = 'long'
    ulong = 'ulong'
    float = 'float'
    double = 'double'

data_type_size_map = { type.char:1, type.byte:1, type.short:2, type.ushort:2, type.int:4, type.uint:4, type.long:8, type.ulong:8, type.float:4, type.double:8 }
data_type_name_map = { type.char:'b', type.byte:'B', type.short:'h', type.ushort:'H', type.int:'i', type.uint:'I', type.long:'q', type.ulong:'Q', type.float:'f', type.double:'d' }

def read(file, type):
    bytes = file.read(data_type_size_map[type])
    #print(bytes)
    return struct.unpack('<' + data_type_name_map[type], bytes)[0]

def read_list(file, size, type):
    float_array = []
    for i in range(size):
        float_array.append(read(file, type))
    return float_array

class list_map(dict):
    def add(self, key, item):
        list = self.get(key)
        if list == None:
            list = []
            self.__setitem__(self, key, list)
        list.append(item)
