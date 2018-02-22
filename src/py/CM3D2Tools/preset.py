import util

class preset_png:
    def __init__(self, file):
        self.png_size = util.read(file, util.type.int)
        self.png_data = util.read_bytes(file, self.png_size)

    def write_image(self, file):
        file.write(self.png_data)

class block_a:
    num = 0
    def __init__(self, file, type, ver):
        self.type = type
        self.serial = util.read(file, util.type.uint)
        self.value = util.read(file, util.type.int)
        if ver > 100:
            self.unknown1 = util.read(file, util.type.uint)
        else:
            self.unknown1 = 0
        self.unknown2 = util.read_list(file, 10, util.type.byte)
        self.max_value = util.read(file, util.type.int)
        self.min_value = util.read(file, util.type.int)

        block_a.num += 1
        print('num a: %d' % block_a.num)
        print('type: %08X' % self.type)
        print('serial: %08X' % self.serial)
        print('%d(%d, %d)' % (self.value, self.min_value, self.max_value))
        print('unknown 1: %08X' % self.unknown1)
        print(self.unknown2)
        print()

class block_b:
    num = 0
    def __init__(self, file, type, ver):
        self.type = type
        self.unknown1 = util.read_list(file, 12, util.type.byte)
        if ver > 100:
            self.unknown2 = util.read(file, util.type.uint)
        else:
            self.unknown2 = 0
        self.menu = util.read_str(file)
        self.menu_hash = util.read(file,util.type.uint)
        self.unknown3 = util.read_list(file, 9, util.type.byte)

        if self.menu != '':
            block_b.num += 1
            print('num b: %d' % block_b.num)
            print('type: %08X' % self.type)
            print('%s, %08X' % (self.menu, self.menu_hash))
            print()

def load_block_data(self, ver):
    type = util.read(file, util.type.uint)
    if type == 3:
        return block_b(file, type, ver)
    else:
        return block_a(file, type, ver)


class morph_data:
    def __init__(self, file):
        self.name = util.read_str(file)
        self.flag = util.read_str(file)
        self.ver = util.read(file, util.type.int)
        self.serial = util.read(file, util.type.int)
        self.ctxt = util.read_str(file)

        self.data = load_block_data(file, self.ver)

    def __str__(self):
        return '(%s,%s,%d,%s)' % (self.name, self.flag, self.serial, self.ctxt)

class morph_list(list):
    def __str__(self):
        s = ''
        for m in self:
            s += str(m) + ', '
        return '[ ' + s + ']'

class preset_archive:
    def __init__(self, file):
        self.ext = util.read_str(file)
        self.ver1 = util.read(file, util.type.int)
        self.type = util.read(file, util.type.int)
        self.image = preset_png(file)

        self.flag1 = util.read_str(file)
        self.ver2 = util.read(file, util.type.int)
        self.morph_num = util.read(file, util.type.int)

        self.morph_list = morph_list()
        for morph_idx in range(self.morph_num):
            self.morph_list.append(morph_data(file))

    def __str__(self):
        s = ''
        for m in vars(self):
            s += '%-12s: %s\n' % (m, self.__getattribute__(m))
        return s

file = open('D:\\GAME\\CM3D2\\1.51.1\\CM3D2\\Preset\\pre_朝日奈穂乃香_20170724141332.preset', 'rb')
arc = preset_archive(file)
#arc.image.write_image(open('preset.png', 'wb'))
file.close()
