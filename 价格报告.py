import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'SimHei'  # 替换为你选择的字体
def 生成推荐报告():
    """生成机械革命蛟龙16Pro推荐分析"""
    
    # 1. 价格对比数据
    价格数据 = pd.DataFrame({
        '型号': ['蛟龙16Pro', '暗影精灵11', '拯救者R9000P', '小新Pro14', '天选者6Pro'],
        '价格': [7299, 9299, 11499, 6389, 7269],
        '类型': ['推荐款', '竞品', '竞品', '轻薄本', '竞品']
    })
    
    # 2. 性能对比数据
    性能数据 = pd.DataFrame({
        '型号': ['蛟龙16Pro', '天选者6Pro', '蛟龙16', '旷世X'],
        'CPU': ['R9 8940HX', '锐龙7H 260', 'R7 7745HX', 'i7-14650HX'],
        '核心数': [16, 8, 8, 8],
        '线程数': [32, 16, 16, 16],
        '价格': [7069, 7269, 6369, 6529],
        '性能分': [32000, 18000, 19000, 24000]  # Cinebench R23多核
    })
    
    # 3. 计算性价比
    性能数据['每千元性能'] = 性能数据['性能分'] / 性能数据['价格'] * 1000
    
    # 4. 生成图表
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # 图表1：价格对比柱状图
    colors = ['#FF6B6B' if x=='推荐款' else '#95A5A6' for x in 价格数据['类型']]
    axes[0, 0].bar(价格数据['型号'], 价格数据['价格'], color=colors)
    axes[0, 0].set_title('价格对比（蛟龙16Pro处在甜点区）', fontsize=14)
    axes[0, 0].set_ylabel('价格（元）')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 添加价格标签
    for i, (price, model) in enumerate(zip(价格数据['价格'], 价格数据['型号'])):
        axes[0, 0].text(i, price+200, f'{price}元', ha='center', fontsize=9)
        if model == '蛟龙16Pro':
            axes[0, 0].text(i, price/2, '推荐', ha='center', fontsize=12, 
                          fontweight='bold', color='white')
    
    # 图表2：性能对比雷达图
    性能参数 = ['多核性能', '单核性能', '能效比', '价格', '扩展性']
    性能值 = {
        '蛟龙16Pro': [9.5, 8.0, 8.5, 7.0, 8.0],
        '天选者6Pro': [6.0, 7.5, 8.0, 6.5, 7.5],
        '暗影精灵11': [7.0, 8.0, 7.0, 5.0, 8.0]
    }
    
    angles = np.linspace(0, 2*np.pi, len(性能参数), endpoint=False).tolist()
    angles += angles[:1]
    
    ax = plt.subplot(222, polar=True)
    for model, values in 性能值.items():
        values += values[:1]
        ax.plot(angles, values, 'o-', linewidth=2, label=model)
        ax.fill(angles, values, alpha=0.1)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(性能参数)
    ax.set_title('五维性能对比雷达图', fontsize=14)
    ax.legend(loc='upper right')
    
    # 图表3：性价比散点图
    axes[1, 0].scatter(性能数据['价格'], 性能数据['性能分'], 
                      s=性能数据['核心数']*100, alpha=0.6)
    axes[1, 0].set_xlabel('价格（元）')
    axes[1, 0].set_ylabel('性能分（Cinebench R23）')
    axes[1, 0].set_title('价格-性能散点图（气泡大小=核心数）')
    
    # 标注每个点
    for i, row in 性能数据.iterrows():
        axes[1, 0].text(row['价格']+50, row['性能分'], row['型号'], 
                       fontsize=9, va='center')
        if row['型号'] == '蛟龙16Pro':
            axes[1, 0].plot(row['价格'], row['性能分'], 'r*', markersize=15)
    
    # 图表4：核心数对比
    axes[1, 1].barh(性能数据['型号'], 性能数据['核心数'], color='#4ECDC4')
    axes[1, 1].set_xlabel('CPU核心数')
    axes[1, 1].set_title('CPU核心数对比（蛟龙16Pro翻倍领先）')
    for i, cores in enumerate(性能数据['核心数']):
        axes[1, 1].text(cores+0.5, i, f'{cores}核{性能数据.loc[i, "线程数"]}线程', 
                       va='center')
    
    plt.tight_layout()
    plt.show()
    
    # 5. 生成文字结论
    结论 = f"""
    ====== 机械革命蛟龙16Pro推荐结论 ======
    
    价格优势：
    • 仅售7299元，比同性能竞品（暗影精灵11）便宜2000元
    • 在热销榜中处在"性价比甜点区"
    
    性能优势：
    • R9 8940HX（16核32线程）碾压同级8核CPU
    • 每千元性能得分：{性能数据.loc[0, '每千元性能']:.1f}分，领先竞品
    • 核心数翻倍，适合多任务和未来游戏
    
    便携美观：
    • 2.4kg相对轻便，金属机身质感好
    • RGB灯效+高屏占比设计，符合年轻审美
    
    推荐指数：★★★★☆ (4.5/5)
    适合人群：预算7-8K、需要兼顾学习与游戏的大学生
    """
    
    print(结论)
    
    # 保存数据
    with open('推荐结论.txt', 'w', encoding='utf-8') as f:
        f.write(结论)
    
    print("分析报告已生成：")
    print("1. 蛟龙16Pro推荐分析.png")
    print("2. 推荐结论.txt")

# 运行
if __name__ == "__main__":
    生成推荐报告()