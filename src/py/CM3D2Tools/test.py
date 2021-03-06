
import preset
import model

preset_morph_config = preset.load_preset_morph_config('D:\\GAME\\CM3D2\\1.51.1\\CM3D2\\Preset\\10_hhs_chara1.preset')

#file = open('D:\\DEV\\CM3D2\\ARC\\model\\model\\model\\body\\seieki\\spe_body0.model', 'rb')
file = open('D:\\DEV\\CM3D2\\ARC\\model\\model\\model\\body\\seieki\\spe_body0.model', 'rb')

#arc = model.model_archive(file)
#file_out = open('..\\..\\..\\run\\spe_body0.model.bone.txt', 'wb')
#arc.generate_bone_archive(file_out)
#file_out.close()

arc = model.model_archive(file)
arc.print_bone_tree()
#file_out = open('..\\..\\..\\run\\face003.model.txt', 'wb')
file_out = open('..\\..\\..\\run\\spe_body0.model.model', 'wb')
arc.write(file_out, preset_morph_config)
file_out.close()

file.close()
