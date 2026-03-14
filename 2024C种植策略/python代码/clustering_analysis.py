#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2024C种植策略 - 聚类分析模块
"""

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Ellipse
import numpy as np

# 设置matplotlib支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

def load_data(file_path):
    """加载数据"""
    return pd.read_excel(file_path)

def perform_clustering(df):
    """执行聚类分析"""
    features = ['种植成本/(元/亩)', '销售量/斤', '平均售价']
    
    if not all(feat in df.columns for feat in features):
        print(f"警告: 缺少必要的列。当前列: {list(df.columns)}")
        return None
    
    X = df[features].copy()
    
    # 处理缺失值
    X = X.dropna()
    
    # 标准化数据
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # K-means聚类
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X_scaled)
    
    df_clustered = df.loc[X.index].copy()
    df_clustered['Cluster'] = kmeans.labels_
    
    return df_clustered, kmeans, X_scaled

def plot_3d_clustering(df, kmeans, X_scaled, output_path='clustering_3d.png'):
    """绘制三维聚类图"""
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    colors = ['red', 'green', 'blue']
    labels = ['Cluster 0', 'Cluster 1', 'Cluster 2']
    
    for i in range(3):
        cluster_data = df[df['Cluster'] == i]
        ax.scatter(
            cluster_data['种植成本/(元/亩)'], 
            cluster_data['销售量/斤'], 
            cluster_data['平均售价'], 
            c=colors[i], 
            label=labels[i],
            s=50,
            alpha=0.7
        )
    
    # 绘制聚类中心
    centers = kmeans.cluster_centers_
    for i in range(3):
        ax.scatter(centers[i, 0], centers[i, 1], centers[i, 2], 
                  c='yellow', marker='*', s=200, edgecolors='black', linewidths=2)
    
    ax.set_xlabel('种植成本 (元/亩)')
    ax.set_ylabel('销售量 (斤)')
    ax.set_zlabel('平均售价')
    ax.set_title('三维聚类分析')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"三维聚类图已保存: {output_path}")
    plt.close()

def save_results(df, output_path='clustering_results.xlsx'):
    """保存聚类结果"""
    df.to_excel(output_path, index=False)
    print(f"聚类结果已保存: {output_path}")

def print_statistics(df):
    """打印统计信息"""
    print("\n" + "=" * 60)
    print("聚类分析统计信息")
    print("=" * 60)
    
    for cluster in sorted(df['Cluster'].unique()):
        cluster_data = df[df['Cluster'] == cluster]
        print(f"\n聚类 {cluster} (数量: {len(cluster_data)}):")
        print(f"  平均种植成本: {cluster_data['种植成本/(元/亩)'].mean():.2f} 元/亩")
        print(f"  平均销售量: {cluster_data['销售量/斤'].mean():.2f} 斤")
        print(f"  平均售价: {cluster_data['平均售价'].mean():.2f} 元/斤")

def main():
    """主函数"""
    file_path = '聚类.xls'
    
    print("加载数据...")
    df = load_data(file_path)
    
    print("执行聚类分析...")
    result = perform_clustering(df)
    
    if result is None:
        print("聚类分析失败！")
        return
    
    df_clustered, kmeans, X_scaled = result
    
    print("绘制三维聚类图...")
    plot_3d_clustering(df_clustered, kmeans, X_scaled)
    
    print("保存结果...")
    save_results(df_clustered)
    
    print_statistics(df_clustered)
    
    print("\n聚类分析完成！")

if __name__ == "__main__":
    main()
