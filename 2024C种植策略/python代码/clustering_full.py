#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2024C种植策略 - 聚类完整分析（简化版，不依赖sklearn）
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 设置matplotlib支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def load_data(file_path):
    """加载数据"""
    return pd.read_excel(file_path)

def normalize_data(X):
    """标准化数据"""
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    return (X - mean) / std

def kmeans_clustering(X, n_clusters=3, max_iters=100, random_state=42):
    """简单的K-means聚类实现（不依赖sklearn）"""
    np.random.seed(random_state)
    
    n_samples = X.shape[0]
    
    # 随机初始化质心
    indices = np.random.choice(n_samples, n_clusters, replace=False)
    centroids = X[indices].copy()
    
    for _ in range(max_iters):
        # 计算每个样本到质心的距离
        distances = np.zeros((n_samples, n_clusters))
        for i in range(n_clusters):
            distances[:, i] = np.linalg.norm(X - centroids[i], axis=1)
        
        # 分配每个样本到最近的质心
        labels = np.argmin(distances, axis=1)
        
        # 更新质心
        new_centroids = np.zeros_like(centroids)
        for i in range(n_clusters):
            cluster_points = X[labels == i]
            if len(cluster_points) > 0:
                new_centroids[i] = np.mean(cluster_points, axis=0)
            else:
                new_centroids[i] = centroids[i]
        
        # 检查收敛
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    
    return labels, centroids

def perform_clustering(df):
    """执行聚类分析"""
    features = ['种植成本/(元/亩)', '销售量/斤', '平均售价']
    
    if not all(feat in df.columns for feat in features):
        print(f"警告: 缺少必要的列。当前列: {list(df.columns)}")
        return None
    
    X = df[features].copy()
    X = X.dropna()
    
    # 标准化数据
    X_normalized = normalize_data(X.values)
    
    # 执行聚类
    labels, centroids = kmeans_clustering(X_normalized, n_clusters=3)
    
    df_clustered = df.loc[X.index].copy()
    df_clustered['Cluster'] = labels
    
    return df_clustered, labels, centroids, X.values

def plot_3d_clustering(df, output_path='clustering_3d.png'):
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
    
    print("=" * 60)
    print("2024C种植策略 - 聚类分析")
    print("=" * 60)
    
    print("\n加载数据...")
    df = load_data(file_path)
    
    print(f"数据行数: {len(df)}")
    print(f"数据列名: {list(df.columns)}")
    
    print("\n执行聚类分析...")
    result = perform_clustering(df)
    
    if result is None:
        print("聚类分析失败！")
        return
    
    df_clustered, labels, centroids, X_original = result
    
    print("\n绘制三维聚类图...")
    plot_3d_clustering(df_clustered)
    
    print("\n保存结果...")
    save_results(df_clustered)
    
    print_statistics(df_clustered)
    
    print("\n" + "=" * 60)
    print("聚类分析完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()
