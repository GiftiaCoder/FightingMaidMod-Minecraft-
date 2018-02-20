import util

def load_preset(file, preset):
    preset['ext'] = util.read_str(file)
    preset['ver'] = util.read(file, util.type.int)
    preset['type'] = type = util.read(file, util.type.int)
    preset['png_size'] = png_size = util.read(file, util.type.int)
    preset['png_data'] = util.read_bytes(file, png_size)
    preset['morph_list_flag'] = util.read_str(file)
    preset['ver2'] = util.read(file, util.type.int)
    preset['morph_count'] = morph_count = util.read(file, util.type.int)

    #loop section
    preset['flag1'] = util.read_str(file)
    preset['flag2'] = util.read_str(file)
    preset['ver3'] = util.read(file, util.type.int)
    preset['serial_num1'] = serial_num = util.read(file, util.type.int)
    preset['flag3'] = util.read_str(file)

    #block type1
    preset['block_type'] = util.read(file, util.type.int)
    preset['block_unknown_data'] = util.read(file, util.type.int)
    preset['block_value1'] = util.read(file, util.type.int)

    pass

preset = {}

file = open('D:\\GAME\\CM3D2\\1.51.1\\CM3D2\\Preset\\1_junshin.preset', 'rb')
load_preset(file, preset)
file.close()

print(preset)
