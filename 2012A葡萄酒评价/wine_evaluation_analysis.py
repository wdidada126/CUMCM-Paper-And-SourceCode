import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def wine_evaluation_normality_test():
    """
    葡萄酒评价问题1：判断两组评酒员评分是否服从正态分布
    """
    print("Problem 1: Wine Evaluation - Normality Test")
    print("=" * 60)
    
    # 示例数据（需要从实际数据文件加载）
    # red1, red2: 两组红葡萄酒评分
    # white1, white2: 两组白葡萄酒评分
    
    # 生成示例数据
    np.random.seed(42)
    red1 = np.random.normal(75, 5, 10)
    red2 = np.random.normal(74, 5, 10)
    white1 = np.random.normal(76, 5, 10)
    white2 = np.random.normal(75, 5, 10)
    
    # 计算总分
    r1 = np.sum(red1)
    r2 = np.sum(red2)
    w1 = np.sum(white1)
    w2 = np.sum(white2)
    
    print(f"Red wine group 1 total score: {r1:.2f}")
    print(f"Red wine group 2 total score: {r2:.2f}")
    print(f"White wine group 1 total score: {w1:.2f}")
    print(f"White wine group 2 total score: {w2:.2f}")
    
    # 正态性检验
    def test_normality(data, name):
        stat, p_value = stats.shapiro(data)
        print(f"\n{name}:")
        print(f"  Shapiro-Wilk test statistic: {stat:.4f}")
        print(f"  p-value: {p_value:.4f}")
        if p_value > 0.05:
            print(f"  Result: Data appears to be normally distributed (p > 0.05)")
        else:
            print(f"  Result: Data does not appear to be normally distributed (p <= 0.05)")
        
        # 绘制Q-Q图
        plt.figure(figsize=(10, 6))
        stats.probplot(data, dist="norm", plot=plt)
        plt.title(f'Q-Q Plot for {name}')
        plt.grid(True)
        plt.savefig(f'{name.replace(" ", "_")}_qq_plot.png')
        plt.close()
    
    # 对四组数据进行正态性检验
    test_normality(red1, "Red Wine Group 1")
    test_normality(red2, "Red Wine Group 2")
    test_normality(white1, "White Wine Group 1")
    test_normality(white2, "White Wine Group 2")
    
    print("\nQ-Q plots saved as PNG files")

if __name__ == "__main__":
    wine_evaluation_normality_test()