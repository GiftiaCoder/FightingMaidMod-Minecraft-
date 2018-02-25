import util
from util import type

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
        print(self.name)
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

file = open('D:\\DEV\\CM3D2\\ARC\\model\\model\\model\\body\\seieki\\spe_body0.model', 'rb')

arc = model_archive(file)

#print(arc.root_bone)
#for local_bone_idx in range(arc.local_bone_count):
#    print('local bone name: ' + arc.local_bone_list[local_bone_idx].name)

file.close()
