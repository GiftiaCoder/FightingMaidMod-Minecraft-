import util

class frame_sample:
    def __init__(self, file):
        self.time = util.read(file, util.type.float)
        self.coord = util.read_list(file, 3, util.type.float)

    def __str__(self):
        return '%f\t%f\t%f\t%f' % (self.time, self.coord[0], self.coord[1], self.coord[2])

class bone_transform_data:
    def __init__(self, bone_name, frame_map):
        self.bone_name = bone_name
        self.frame_map = frame_map

class anm_archive:
    def __init__(self, file):
        self.ext = util.read_str(file)
        self.ver = util.read(file, util.type.int)

        self.bone_transform_list = []

        bone_set = set()

        flag_a = util.read(file, util.type.byte)
        while True:
            bone_name = util.read_str(file)
            if bone_set.__contains__(bone_name):
                return

            bone_set.add(bone_name)

            frame_map = {}

            while True:
                flag_b = util.read(file, util.type.byte)
                if flag_b == 1:
                    break
                elif flag_b == 0:
                    return
                frame_map[flag_b] = frame_list = []
                #print(frame_map)
                frame_num = util.read(file, util.type.int)
                for frame_idx in range(frame_num):
                    sample = frame_sample(file)
                    frame_list.append(sample)

            self.bone_transform_list.append(bone_transform_data(bone_name, frame_map))

file = open('D:\\DEV\\CM3D2\\ARC\\motion\\motion\\_maid\\maid_stand01.anm', 'rb')
arc = anm_archive(file)
file.close()

out = open('..\\..\\..\\run\\maid_stand01.anm.txt', 'w')
for bone in arc.bone_transform_list:
    out.write(bone.bone_name + '\n')
    for k in bone.frame_map:
        out.write('\t' + str(k) + '\n')
        for sample in bone.frame_map[k]:
            out.write('\t\t' + str(sample) + '\n')

out.close()
