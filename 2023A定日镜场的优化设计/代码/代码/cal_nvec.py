import numpy as np

def cal_nvec(tower_x, tower_y, tower_z, mir_x, mir_y, mir_z, alps, gams):
    """
    nvec_xyz 定日镜的法向量
    tower_xyz 吸收塔的坐标
    mir_xyz 定日镜的坐标
    alps 太阳高度角
    gams 太阳方位角
    """
    inline = np.array([-np.cos(alps)*np.sin(gams), -np.cos(alps)*np.cos(gams), -np.sin(alps)])
    outline = np.array([(mir_x-tower_x)/((mir_x-tower_x)**2+(mir_y-tower_y)**2+(mir_z-tower_z)**2),
                       (mir_y-tower_y)/((mir_x-tower_x)**2+(mir_y-tower_y)**2+(mir_z-tower_z)**2),
                       (mir_z-tower_z)/((mir_x-tower_x)**2+(mir_y-tower_y)**2+(mir_z-tower_z)**2)])
    nvec = (inline + outline) / 2
    nvec_x = nvec[0]
    nvec_y = nvec[1]
    nvec_z = nvec[2]
    return nvec_x, nvec_y, nvec_z
