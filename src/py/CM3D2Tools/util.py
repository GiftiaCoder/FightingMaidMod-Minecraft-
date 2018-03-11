import struct
import enum

def read_bytes(file, size):
    return file.read(size)

class type(enum.Enum):
    char = 'char', 1, 'b'
    byte = 'byte', 1, 'B'
    short = 'short', 2, 'h'
    ushort = 'ushort', 2, 'H'
    int = 'int', 4, 'i'
    uint = 'uint', 4, 'I'
    long = 'long', 8, 'q'
    ulong = 'ulong', 8, 'Q'
    float = 'float', 4, 'f'
    double = 'double', 8, 'd'
    str = 'string', -1, '\0'

    def write(self, file, data):
        if self != type.str:
            bytes = struct.pack('<' + self._value_[2], data)
            file.write(bytes)
        else:
            file.write(struct.pack('<' + type.int._value_[2], len(data)))
            file.write(data.encode('utf-8'))

    def write_list(self, file, list):
        for data in list:
            self.write(file, data)

    def read(self, file):
        if self != type.str:
            bytes = file.read(self._value_[1])
            return struct.unpack('<' + self._value_[2], bytes)[0]
        else:
            total_b = ''
            for i in range(9):
                b_str = format(struct.unpack('<B', file.read(1))[0], '08b')
                total_b = b_str[1:] + total_b
                if b_str[0] == '0':
                    break
            return file.read(int(total_b, 2)).decode('utf-8')

    def read_list(self, file, count):
        data_list = []
        for c in range(count):
            data_list.append(self.read(file))
        return data_list

def read(file, type):
    return type.read(file)

def read_list(file, size, type):
    return type.read_list(file, size)

def read_str(file):
    return type.str.read(file)

def write(file, str):
    file.write(bytes(str, 'utf-8'))

class list_map(dict):
    def add(self, key, item):
        list = self.get(key)
        if list == None:
            list = []
            self[key] = list
        list.append(item)

def identity_matrix():
    return [
        1.0, 0.0, 0.0, 0.0,
        0.0, 1.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0,
        0.0, 0.0, 0.0, 1.0,
    ]

def multiply_matrix(md, ms):
    m = []
    m.append(ms[0] * md[0] + ms[1] * md[4] + ms[2] * md[8] + ms[3] * md[12])
    m.append(ms[0] * md[1] + ms[1] * md[5] + ms[2] * md[9] + ms[3] * md[13])
    m.append(ms[0] * md[2] + ms[1] * md[6] + ms[2] * md[10] + ms[3] * md[14])
    m.append(ms[0] * md[3] + ms[1] * md[7] + ms[2] * md[11] + ms[3] * md[15])

    m.append(ms[4] * md[0] + ms[5] * md[4] + ms[6] * md[8] + ms[7] * md[12])
    m.append(ms[4] * md[1] + ms[5] * md[5] + ms[6] * md[9] + ms[7] * md[13])
    m.append(ms[4] * md[2] + ms[5] * md[6] + ms[6] * md[10] + ms[7] * md[14])
    m.append(ms[4] * md[3] + ms[5] * md[7] + ms[6] * md[11] + ms[7] * md[15])

    m.append(ms[8] * md[0] + ms[9] * md[4] + ms[10] * md[8] + ms[11] * md[12])
    m.append(ms[8] * md[1] + ms[9] * md[5] + ms[10] * md[9] + ms[11] * md[13])
    m.append(ms[8] * md[2] + ms[9] * md[6] + ms[10] * md[10] + ms[11] * md[14])
    m.append(ms[8] * md[3] + ms[9] * md[7] + ms[10] * md[11] + ms[11] * md[15])

    m.append(ms[12] * md[0] + ms[13] * md[4] + ms[14] * md[8] + ms[15] * md[12])
    m.append(ms[12] * md[1] + ms[13] * md[5] + ms[14] * md[9] + ms[15] * md[13])
    m.append(ms[12] * md[2] + ms[13] * md[6] + ms[14] * md[10] + ms[15] * md[14])
    m.append(ms[12] * md[3] + ms[13] * md[7] + ms[14] * md[11] + ms[15] * md[15])

    for i in range(16):
        md[i] = m[i]
