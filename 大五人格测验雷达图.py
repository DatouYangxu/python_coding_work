import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 大五人格维度数据
dimensions = ['神经质', '外倾性', '开放性', '宜人性', '责任心']
scores = [2.75, 3.08, 3.83, 3.83, 3.33]

# 为了雷达图闭合，重复第一个值
angles = np.linspace(0, 2 * np.pi, len(dimensions), endpoint=False).tolist()
scores.append(scores[0])
dimensions.append(dimensions[0])
angles.append(angles[0])

# 创建雷达图
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# 绘制雷达图
ax.plot(angles, scores, 'o-', linewidth=2, color='steelblue', markersize=8)
ax.fill(angles, scores, alpha=0.25, color='steelblue')

# 设置刻度标签
ax.set_xticks(angles[:-1])
ax.set_xticklabels(dimensions[:-1], fontsize=12)

# 设置y轴标签和范围
ax.set_ylim(0, 5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(['1', '2', '3', '4', '5'], fontsize=10)
ax.grid(True)

# 添加标题
plt.title('大五人格测验结果雷达图', size=16, pad=20)

plt.tight_layout()
plt.show()