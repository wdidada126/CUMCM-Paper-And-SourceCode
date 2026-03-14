import numpy as np
import pandas as pd
from cal_DNI import cal_DNI
from cal_alps_gams import cal_alps_gams
from cal_dhr import cal_dhr
from cal_eta import cal_eta
from cal_nvec import cal_nvec

def main1():
    """
    第一题：定日镜场基础计算
    """
    print("初始化参数...")
    
    # 初始化参数
    mir_data = pd.read_excel('附件.xlsx', header=None)
    mir_data = mir_data.values
    [m, n] = mir_data.shape
    height = 4 * np.ones((m, 1))
    mir_loc = np.hstack([mir_data, height])
    mir_sta = np.zeros((m, 2))
    longitude_E = np.deg2rad(98.5)
    latitude_N = np.deg2rad(39.4)
    tower = [0, 0, 80]
    time = [9, 10.5, 12, 13.5, 15]
    mir_size = [6, 6]
    
    print("初始化结束")
    
    # 计算太阳高度角和太阳方位角
    D = [-59, -28, 0, 31, 61, 92, 122, 153, 184, 214, 245, 275]
    phi = latitude_N
    ST = time
    alps = np.zeros((12, 5))
    gams = np.zeros((12, 5))
    
    for i in range(12):
        for j in range(5):
            alps[i, j], gams[i, j] = cal_alps_gams(D[i], phi, ST[j])
    
    gams[:, 3] = 2*np.pi - gams[:, 3]
    gams[:, 4] = 2*np.pi - gams[:, 4]
    gams = np.real(gams)
    
    print("太阳方位角与高度角计算完成")
    
    # 计算DNI法向直接辐射辐照度
    DNI = np.zeros_like(alps)
    for i in range(12):
        for j in range(5):
            DNI[i, j] = cal_DNI(alps[i, j])
    
    print("DNI计算完成")
    
    # 计算dhr
    [mir_row, mir_col] = mir_loc.shape
    DHR = cal_dhr(mir_loc, mir_row, 0, 0, 80)
    
    print("dhr计算完成")
    
    # 计算平面镜法向量
    nvec_x = np.zeros((mir_row, 12, 5))
    nvec_y = np.zeros((mir_row, 12, 5))
    nvec_z = np.zeros((mir_row, 12, 5))
    
    for i in range(mir_row):
        for j in range(12):
            for k in range(5):
                nvec_x[i, j, k], nvec_y[i, j, k], nvec_z[i, j, k] = cal_nvec(
                    0, 0, 80, mir_loc[i, 0], mir_loc[i, 1], mir_loc[i, 2], alps[j, k], gams[j, k]
                )
                total = np.sqrt(nvec_x[i, j, k]**2 + nvec_y[i, j, k]**2 + nvec_z[i, j, k]**2)
                nvec_x[i, j, k] = nvec_x[i, j, k] / total
    
    nvec_x = np.real(nvec_x)
    nvec_y = np.real(nvec_y)
    nvec_z = np.real(nvec_z)
    
    print("平面镜法向量计算结束")
    
    # 计算余弦效率
    eta_cos = np.zeros((mir_row, 12, 5))
    for i in range(mir_row):
        for j in range(12):
            for k in range(5):
                inline = [-np.cos(alps[j, k])*np.sin(gams[j, k]),
                         -np.cos(alps[j, k])*np.cos(gams[j, k]),
                         -np.sin(alps[j, k])]
                eta_cos[i, j, k] = abs(np.dot([nvec_x[i, j, k], nvec_y[i, j, k], nvec_z[i, j, k]], inline))
    
    eta_cos_ave = np.sum(eta_cos, axis=(0, 2)) / (5 * mir_row)
    
    print("余弦效率计算完成")
    
    # 简化版：假设没有遮挡损失
    eta_sb_ave = np.zeros(12)
    eta_trunc_ave = np.ones(12)
    
    # 计算光学效率
    eta_time = np.zeros((mir_row, 12, 5))
    div_num = 1
    
    for i in range(mir_row):
        for j in range(12):
            for k in range(5):
                shadow_loss = 0
                miss_loss = 0
                total_loss = 1
                eta_time[i, j, k] = cal_eta(shadow_loss, miss_loss, total_loss, DHR[i], eta_cos[i, j, k], div_num)
    
    eta_ave_data = np.sum(eta_time, axis=(0, 2)) / (5 * mir_row)
    
    print("效率计算完成")
    
    # 单位面积镜面平均输出热功率
    E = np.zeros((12, 5))
    for i in range(12):
        for j in range(5):
            E[i, j] = DNI[i, j] * eta_ave_data[j] * (1 - eta_sb_ave[i])
    
    E_ave = np.sum(E, axis=1) / 5
    
    print("计算完成")
    
    return alps, gams, DNI, eta_ave_data, E_ave

if __name__ == "__main__":
    alps, gams, DNI, eta_ave_data, E_ave = main1()
    print(f"太阳高度角范围: {np.rad2deg(alps.min()):.2f}° - {np.rad2deg(alps.max()):.2f}°")
    print(f"DNI范围: {DNI.min():.2f} - {DNI.max():.2f} W/m²")
    print(f"平均光学效率: {eta_ave_data.mean():.4f}")
    print(f"平均输出热功率: {E_ave.mean():.2f} W/m²")
