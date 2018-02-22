import util

def load_model(model_path, model):
    file = open(model_path, 'rb')

    model['ext'] = util.read_str(file)
    model['ver'] = util.read_int(file)
    model['name'] = util.read_str(file)
    model['base_bone'] = util.read_str(file)

    model['bone_count'] = bone_count = util.read_int(file)
    model['bone_data'] = bone_data = []
    for bone_idx in range(bone_count):
        bone_data.append({})
        bone_data[bone_idx]['name'] = util.read_str(file)
        bone_data[bone_idx]['unknown'] = util.read_byte(file)
    for bone_idx in range(bone_count):
        bone_data[bone_idx]['parent_idx'] = parent_idx = util.read_int(file)
        if parent_idx != -1:
            bone_data[bone_idx]['parent_name'] = bone_data[parent_idx]['name']
        else:
            bone_data[bone_idx]['parent_name'] = None
    for bone_idx in range(bone_count):
        bone_data[bone_idx]['rotation_coord'] = util.read_array(file, 3, util.read_float)
        bone_data[bone_idx]['rotation_axis'] = util.read_array(file, 3, util.read_float)
        bone_data[bone_idx]['rotation_angle'] = util.read_float(file)

    model['vertex_num'] = vertex_num = util.read_int(file)
    model['mesh_count'] = mesh_count = util.read_int(file)
    model['local_bone_count'] = local_bone_count = util.read_int(file)

    model['local_bone_list'] = local_bone_list = []
    for local_bone_idx in range(local_bone_count):
        local_bone_list.append({})
        local_bone_list[local_bone_idx]['name'] = util.read_str(file)
    for local_bone_idx in range(local_bone_count):
        local_bone_list[local_bone_idx]['transform_matrix'] = util.read_array(file, 4 * 4, util.read_float)

    model['vertex_list'] = vertex_list = []
    for vertex_idx in range(vertex_num):
        vertex_list.append({})
        vertex_list[vertex_idx]['coord'] = util.read_array(file, 3, util.read_float)
        vertex_list[vertex_idx]['normal'] = util.read_array(file, 3, util.read_float)
        vertex_list[vertex_idx]['uv'] = util.read_array(file, 2, util.read_float)

    model['unknown_data_num'] = unknown_data_num = util.read_int(file)
    model['unknown_data_list'] = unknown_data_list = []
    for unknown_data_idx in range(unknown_data_num):
        unknown_data_list.append({})
        unknown_data_list[unknown_data_idx]['data'] = util.read_array(file, 4, util.read_float)

    for vertex_idx in range(vertex_num):
        vertex_list[vertex_idx]['weights'] = weight_data = {}
        weight_data['bone_idx'] = util.read_array(file, 4, util.read_ushort)
        weight_data['bone_weight'] = util.read_array(file, 4, util.read_float)

    model['mesh_list'] = mesh_list = []
    #print('mesh count: %d' % (mesh_count))
    for mesh_idx in range(mesh_count):
        mesh_list.append({})
        mesh_list[mesh_idx]['face_num'] = face_num = int(util.read_int(file) / 3)
        #print('mesh %d has %d faces' % (mesh_idx, face_num))
        mesh_list[mesh_idx]['face_list'] = face_list = []
        for face_idx in range(face_num):
            ary = util.read_array(file, 3, util.read_ushort)
            #print(ary)
            face_list.append(ary)

    model['material_count'] = material_count = util.read_int(file)
    model['material_data'] = material_data = []
    for material_idx in range(material_count):
        material_data.append({})
        material_data[material_idx]['name'] = util.read_str(file)
        #print('material name: %s' % material_data[material_idx]['name'])
        material_data[material_idx]['type1'] = util.read_str(file)
        #print('material type1: %s' % material_data[material_idx]['type1'])
        material_data[material_idx]['type2'] = util.read_str(file)
        #print('material type2: %s' % material_data[material_idx]['type2'])
        material_data[material_idx]['data'] = data = []
        while True:
            type = util.read_str(file)
            #print('type: %s' % type)
            if type == 'tex':
                data.append({})
                data[-1]['name'] = util.read_str(file)
                #print('name: %s' % (data[-1]['name']))
                data[-1]['type2'] = util.read_str(file)
                #print('type2: %s' % (data[-1]['type2']))
                if data[-1]['type2'] == 'tex2d':
                    data[-1]['name2'] = util.read_str(file)
                    data[-1]['path'] = util.read_str(file)
                    #print('path: %s' % (data[-1]['path']))
                    data[-1]['color'] = util.read_array(file, 4, util.read_float)
            elif type == 'col':
                data.append({})
                data[-1]['name'] = util.read_str(file)
                #print(data[-1]['name'])
                data[-1]['color'] = util.read_array(file, 4, util.read_float)
            elif type == 'f':
                data.append({})
                data[-1]['name'] = util.read_str(file)
                #print(data[-1]['name'])
                data[-1]['float'] = util.read_float(file)
            else:
                break

    model['morph_list'] = morph_list = []
    while True:
        flag = util.read_str(file)
        if flag == 'morph':
            morph_list.append({})
            morph_list[-1]['name'] = util.read_str(file)
            #print('morph name: %s' % (morph_list[-1]['name']))
            morph_list[-1]['vertex_num']  = morph_vertex_num = util.read_int(file)
            morph_list[-1]['vertex_data'] = morph_vertex_data = []
            for morph_vertex_idx in range(morph_vertex_num):
                morph_vertex_data.append({})
                morph_vertex_data[morph_vertex_idx]['vertex_idx'] = util.read_ushort(file)
                morph_vertex_data[morph_vertex_idx]['coord'] = util.read_array(file, 3, util.read_float)
                morph_vertex_data[morph_vertex_idx]['normal'] = util.read_array(file, 3, util.read_float)
        else:
            break

    file.close()

def build_model(model_archive, model):
    #TODO
    pass

def print_list(f, l, prefix = ''):
    for e in l:
        if type(e) == list:
            print_list(f, e, prefix + '\t')
        elif type(e) == dict:
            print_dict(f, e, prefix + '\t')
        else:
            f.write('%s%s\n' % (prefix, str(e)))

def print_dict(f, d, prefix = ''):
    for k in d:
        v = d[k]
        if type(v) == dict:
            f.write('%s%s:\n' % (prefix, k))
            print_dict(f, v, prefix + '\t')
        elif type(v) == list:
            f.write('%s%s:\n' % (prefix, k))
            print_list(f, v, prefix + '\t')
        else:
            f.write('%s%s: %s\n' % (prefix, str(k), str(v)))
            #print('%s%s: %s' % (prefix, str(k), str(v)))

def analyze_morph(model):
    file = open('morph.txt', 'w')
    for morph in model['morph_list']:
        file.write('%s, %d\n' % (morph['name'], morph['vertex_num']))
        for vertex in morph['vertex_data']:
            file.write(str(vertex) + '\n')
    file.close()

model_archive = {}
model = {}
load_model('D:\\DEV\\CM3D2\\ARC\\model\\model\\model\\body\\seieki\\spe_body0.model', model_archive)
build_model(model_archive, model)

analyze_morph(model_archive)

#print('----------------------------------------')
#print(model_archive['base_bone'])
#print('----------------------------------------')
#print(model_archive['local_bone_list'])
#print('----------------------------------------')
#print(model_archive['bone_data'])
#print('----------------------------------------')

#file = open('..\\..\\..\\run\\face005.model.txt', 'w')
#
#file.write(str(len(model_archive['vertex_list'])) + '\n')
#for vertex in model_archive['vertex_list']:
    #print(vertex)
#    coord = vertex['coord']
#    normal = vertex['normal']
#    file.write('%s %s %s %s %s %s\n' %
#               (str(coord[0]), str(coord[1]), str(coord[2]),
#                str(normal[0]), str(normal[1]), str(normal[2])))

#mesh_list = model_archive['mesh_list']
#file.write(str(len(mesh_list)) + '\n')
#for mesh_data in mesh_list:
#    file.write(str(len(mesh_data['face_list'])) + '\n')
#    for face_data in mesh_data['face_list']:
#        file.write('%d %d %d\n' % (face_data[0], face_data[1], face_data[2]))

#file.close()

#for f in model_archive['mesh_list']['face_list']:
#    print(f)

#file = open('model.arc', 'w')
#print_dict(file, model_archive)
#file.close()
