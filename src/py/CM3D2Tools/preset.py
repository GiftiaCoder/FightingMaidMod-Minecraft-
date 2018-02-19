import util

preset_type_name = { 0:'c', 1:'b', 2:'c/b'}

def load_preset(file, preset):
    preset['ext'] = util.read_str(file)
    preset['ver'] = util.read_int(file)
    preset['type'] = type = util.read_int(file)
    preset['type_name'] = preset_type_name[type]
    preset['png_size'] = png_size = util.read_int(file)
    preset['png_data'] = util.read_bytes(file, png_size)
    preset['morph_list_flag'] = util.read_str(file)
    pass

preset = {}

file = open('D:\\GAME\\CM3D2\\1.51.1\\CM3D2\\Preset\\1_junshin.preset', 'rb')
load_preset(file, preset)
file.close()

print(preset)
