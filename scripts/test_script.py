import bpy
import numpy as np
import tqdm


class Creator:
    def __init__(self):
        self.del_defaul_obj()
        self.n_loop = 18
        self.cube_scale = 3.0
        self.cube_distance = 30


    def __call__(self):
        for n2 in tqdm.tqdm(range(self.n_loop)):
            for n1 in tqdm.tqdm(range(self.n_loop)):
                location, size, rotation = self.calc_params(n1, n2)
                bpy.ops.mesh.primitive_cube_add(location=location, size=size, rotation=rotation)

        self.__save()


    def calc_params(self, n1: int, n2: int) -> "tuple, int, tuple":
        r = self.cube_distance
        theta = (n1 * 10)/ 180 * np.pi
        phi = (n2 * 10)/ 180 * np.pi

        x = r * np.sin(theta) * np.cos(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(theta)

        location = (x, z, y)
        size = self.cube_scale
        rotation = (phi, 0.0, -theta)
        return location, size, rotation


    @staticmethod
    def del_defaul_obj():
        objs = [ob for ob in bpy.context.scene.objects if ob.type in ('CAMERA', 'MESH')]
        bpy.ops.object.delete({"selected_objects": objs})


    @staticmethod
    def __save(savename='generated.blend'):
        bpy.ops.wm.save_mainfile(filepath=f'blender/{savename}')


    @staticmethod
    def baking(arg_savefilename = 'test'):
        bakeimage=bpy.data.images.new(name=arg_savefilename, width=1024, height=1024, alpha=True)
        bakeimage.filepath_raw = arg_savefilename + '.png'
        bakeimage.file_format = 'PNG'
        bakeimage.save()


if(__name__=='__main__'):
    Creator()()