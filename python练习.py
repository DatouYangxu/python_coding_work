# import urllib.request as req
# url='http://localhost/index.htm'
# webpage=req.urlopen(url)
# webdata=webpage.read()
# # print(webdata.decode('utf-8'))
# webdata=webdata.decode('utf-8')
# for i in range(2016,2019):
#     index=webdata.find('%s年录取分数统计'%(i))
#     href=webdata[index-133:index-97]
#     href="https://www.nudt.edu.cn/bkzs/xxgk/lqfs/"+href 
#     print("%s年录取分数情况网址是%s"%(i,href))
# n=input('请输入：',)
# print("n=",n)
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.linspace(0,10,50)
# y=np.sin(x)
# z=np.cos(x)
# # plt.axis([-2,12,0,12])
# plt.plot(x,y,x,z)
# plt.show()
import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据
x = np.linspace(0, 10, 30)
y_sin = np.sin(x)
y_cos = np.cos(x)
categories = ['A', 'B', 'C', 'D']
values = [15, 22, 34, 19]
sizes = [30, 100, 200, 60]  # 用于散点图的大小
colors = ['red', 'green', 'blue', 'yellow']

# 创建2x2的子图画布
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# 子图1: 使用fmt格式字符串的线图
axs[0, 0].plot(x, y_sin, 'c--', label='sin(x)')  # 青色虚线
axs[0, 0].plot(x, y_cos, 'r^:', label='cos(x)')   # 红色三角标记的虚线
axs[0, 0].set_title('使用fmt格式字符串')
axs[0, 0].legend()
axs[0, 0].grid(True)

# 子图2: 使用关键字参数的散点图 (scatter)
axs[0, 1].scatter(x, y_sin, s=sizes, c=colors, alpha=0.6, edgecolors='black')
axs[0, 1].set_title('使用关键字参数的散点图')

# 子图3: 柱状图 (bar)
axs[1, 0].bar(categories, values, color=['skyblue', 'lightgreen', 'lightcoral', 'gold'])
axs[1, 0].set_title('柱状图')
axs[1, 0].set_ylabel('数值')

# 子图4: 饼图 (pie)
axs[1, 1].pie(values, labels=categories, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'lightcoral', 'gold'])
axs[1, 1].set_title('饼图')

# 调整布局并显示
plt.tight_layout()
plt.show()