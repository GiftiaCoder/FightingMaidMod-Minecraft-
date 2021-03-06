import util
from util import type
from util import list_map

class bone:
    def read_name(self, file):
        self.name = util.read_str(file)
        unknown = util.read(file, type.byte)

    def read_parent(self, file):
        self.parent_idx = util.read(file, type.int)

    def read_rotation_data(self, file):
        self.rotation_coord = util.read_list(file, 3, type.float)
        self.rotation_axis = util.read_list(file, 3, type.float)
        self.rotation_angle = util.read(file, type.float)

class local_bone:
    def read_name(self, file):
        self.name = util.read_str(file)

    def read_transform_matrix(self, file):
        self.transform_matrix = util.read_list(file, 4 * 4, type.float)

class vertex:
    def read_coord(self, file):
        self.coord = util.read_list(file, 3, type.float)
        self.normal = util.read_list(file, 3, type.float)
        self.uv = util.read_list(file, 2, type.float)

    def read_bone_weight(self, file):
        self.bone_list = util.read_list(file, 4, type.ushort)
        self.weight_list = util.read_list(file, 4, type.float)

class mesh:
    def read_mesh_data(self, file):
        self.face_num = int(util.read(file, type.int) / 3)
        self.face_list = []
        for face_idx in range(self.face_num):
            self.face_list.append(util.read_list(file, 3, type.ushort))

class material:
    class tex:
        def __init__(self, mat_type, file):
            self.mat_type = mat_type
            self.name = util.read_str(file)
            self.type = util.read_str(file)
            if self.type == 'tex2d':
                self.name2 = util.read_str(file)
                self.path = util.read_str(file)
                self.color = util.read_list(file, 4, type.float)

    class col:
        def __init__(self, mat_type, file):
            self.mat_type = mat_type
            self.name = util.read_str(file)
            self.color = util.read_list(file, 4, type.float)

    class f:
        def __init__(self, mat_type, file):
            self.mat_type = mat_type
            self.name = util.read_str(file)
            self.data = util.read(file, type.float)

    def read_material_data(self, file):
        self.name = util.read_str(file)
        self.type1 = util.read_str(file)
        self.type2 = util.read_str(file)
        self.mat_list = []
        while True:
            type = util.read_str(file)
            if type == 'tex':
                self.mat_list.append(material.tex(type, file))
            elif type == 'col':
                self.mat_list.append(material.col(type, file))
            elif type == 'f':
                self.mat_list.append(material.f(type, file))
            else:
                break
        return self

class morph:
    class morph_vertex:
        def __init__(self, file):
            self.vertex_idx = util.read(file, type.ushort)
            self.coord = util.read_list(file, 3, type.float)
            self.normal = util.read_list(file, 3, type.float)

    def read_morph_data(self, file):
        self.name = util.read_str(file)
        #print(self.name)
        self.morph_vertex_count = util.read(file, type.int)
        self.morph_vertex_list = []
        for morph_vertex_idx in range(self.morph_vertex_count):
            self.morph_vertex_list.append(morph.morph_vertex(file))
        return self

class model_archive:
    def __init__(self, file):
        self.ext = util.read_str(file)
        self.ver = util.read(file, type.int)
        self.name = util.read_str(file)
        self.root_bone = util.read_str(file)

        self.bone_count = util.read(file, type.int)
        self.bone_list = []
        for bone_idx in range(self.bone_count):
            self.bone_list.append(bone())
            self.bone_list[bone_idx].read_name(file)
        for bone_idx in range(self.bone_count):
            self.bone_list[bone_idx].read_parent(file)
        for bone_idx in range(self.bone_count):
            self.bone_list[bone_idx].read_rotation_data(file)

        self.vertex_count = util.read(file, type.int)
        self.mesh_count = util.read(file, type.int)
        self.local_bone_count = util.read(file, type.int)

        self.local_bone_list = []
        for local_bone_idx in range(self.local_bone_count):
            self.local_bone_list.append(local_bone())
            self.local_bone_list[local_bone_idx].read_name(file)
        for local_bone_idx in range(self.local_bone_count):
            self.local_bone_list[local_bone_idx].read_transform_matrix(file)

        self.vertex_list = []
        for vertex_idx in range(self.vertex_count):
            self.vertex_list.append(vertex())
            self.vertex_list[vertex_idx].read_coord(file)

        self.read_unknown_data(file)

        for vertex_idx in range(self.vertex_count):
            self.vertex_list[vertex_idx].read_bone_weight(file)

        self.mesh_list = []
        for mesh_idx in range(self.mesh_count):
            self.mesh_list.append(mesh())
            self.mesh_list[mesh_idx].read_mesh_data(file)

        self.material_count = util.read(file, type.int)
        self.material_list = []
        for material_idx in range(self.material_count):
            self.material_list.append(material().read_material_data(file))

        self.morph_list = []
        while True:
            flag = util.read_str(file)
            if flag == 'morph':
                self.morph_list.append(morph().read_morph_data(file))
            else:
                break

    def read_unknown_data(self, file):
        unknown_data_count = util.read(file, type.int)
        for unknown_data_idx in range(unknown_data_count):
            unknwon_data = util.read_list(file, 4, type.float)

    def morph_model(self, morph_config_map):
        final_vertex_list = self.vertex_list.copy()
        for morph_data in self.morph_list:
            val = 0
            if morph_config_map.__contains__(morph_data.name):
                val = morph_config_map[morph_data.name][0] / morph_config_map[morph_data.name][2]
            else:
                print('cannot find preset data %s' % (morph_data.name))

            for morph_vertex in morph_data.morph_vertex_list:
                for i in range(3):
                    final_vertex_list[morph_vertex.vertex_idx].coord[i] += morph_vertex.coord[i] * val
                    final_vertex_list[morph_vertex.vertex_idx].normal[i] += morph_vertex.normal[i] * val
        return final_vertex_list

    def generate_model(self, file, morph_config_map):
        final_vertex_list = self.morph_model(morph_config_map)

        util.write(file, '%i\n' % (self.vertex_count))
        for vertex_data in final_vertex_list:
            util.write(file, '%f %f %f %f %f %f\n'%
                       (vertex_data.coord[0], vertex_data.coord[1], vertex_data.coord[2],
                       vertex_data.normal[0], vertex_data.normal[1], vertex_data.normal[2]))
        util.write(file, '%i\n' % (self.mesh_count))
        for mesh_data in self.mesh_list:
            util.write(file, '%i\n' % (mesh_data.face_num))
            for face_data in mesh_data.face_list:
                util.write(file, '%i %i %i\n' % (face_data[0], face_data[1], face_data[2]))

    def generate_bone_archive(self, file):
        util.write(file, '%i\n' % self.bone_count)
        for bone_data in self.bone_list:
            parent_bone_name = 'null'
            if bone_data.parent_idx != -1:
                parent_bone_name = self.bone_list[bone_data.parent_idx].name
            util.write(file, '%s\n%s\n%f %f %f %f %f %f %f\n' %
                       (bone_data.name, parent_bone_name,
                        bone_data.rotation_coord[0], bone_data.rotation_coord[1], bone_data.rotation_coord[2],
                        bone_data.rotation_axis[0], bone_data.rotation_axis[1], bone_data.rotation_axis[2],
                        bone_data.rotation_angle))

    def print_child_bone(self, name, bone_name_map, parent_list, prefix, local_bone_name_set):
        print(prefix + name)
        for parent in parent_list:
            if local_bone_name_set.__contains__(parent):
                print('\033[0;31;40m', end='')

            if bone_name_map.__contains__(parent):
                self.print_child_bone(parent, bone_name_map, bone_name_map[parent], prefix + '  | ', local_bone_name_set)
            else:
                print(prefix + '  | ' + parent)

            if local_bone_name_set.__contains__(parent):
                print('\033[0m', end='')

    def print_bone_tree(self):
        bone_name_map = list_map()
        for bone_data in self.bone_list:
            if bone_data.parent_idx != -1:
                bone_name_map.add(self.bone_list[bone_data.parent_idx].name, bone_data.name)
            else:
                bone_name_map.add('(null)', bone_data.name)
        local_name_set = set()
        for local_bone in self.local_bone_list:
            local_name_set.add(local_bone.name)
        self.print_child_bone('(null)', bone_name_map, bone_name_map['(null)'], '', local_name_set)

    def create_parent_map(self):
        parent_map = {}
        for bone_data in self.bone_list:
            if bone_data.parent_idx != -1:
                parent_map[bone_data.name] = self.bone_list[bone_data.parent_idx].name
        return parent_map

    def create_local_bone_name_map(self):
        bone_map = {}
        for local_bone in self.local_bone_list:
            bone_map[local_bone.name] = local_bone
        return bone_map

    def get_transform_matrix(self, local_bone, matrix, parent_map, bone_map):
        util.multiply_matrix(matrix, local_bone.transform_matrix)
        if parent_map.__contains__(local_bone.name):
            self.get_transform_matrix(bone_map[parent_map[local_bone.name]], matrix, parent_map, bone_map)

    def write(self, file, morph_config_map):
        #for bone_data in self.local_bone_list:
        #    print(bone_data.name)
        #bone
        type.str.write(file, 'bone')
        type.int.write(file, self.local_bone_count)
        for bone_data in self.local_bone_list:
            type.str.write(file, bone_data.name)

            transform_matrix = util.identity_matrix()
            print(transform_matrix)
            self.get_transform_matrix(bone_data, transform_matrix, self.create_parent_map(), self.create_local_bone_name_map())
            print(transform_matrix)
            type.float.write_list(file, transform_matrix)

            #type.float.write_list(file, bone_data.transform_matrix)
        #vertex
        type.str.write(file, 'vertex')
        type.int.write(file, self.vertex_count)
        for vertex in self.morph_model(morph_config_map):
        #for vertex in self.vertex_list:
            type.float.write_list(file, vertex.coord)
            type.float.write_list(file, vertex.normal)
            type.float.write_list(file, vertex.uv)
            type.int.write_list(file, vertex.bone_list)
            type.float.write_list(file, vertex.weight_list)
        #mesh
        type.str.write(file, 'mesh')
        type.int.write(file, self.mesh_count)
        for mesh in self.mesh_list:
            type.int.write(file, mesh.face_num)
            for face in mesh.face_list:
                type.int.write_list(file, face)