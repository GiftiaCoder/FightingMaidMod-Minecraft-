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
            self.__setitem__(self, key, list)
        list.append(item)
