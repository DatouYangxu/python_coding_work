# 大一学生第一次操作数据库
# 作者：[你的名字]

# 1. 导入模块
import pymysql

# 2. 连接数据库
print("正在连接数据库...")
connection = pymysql.connect(
    host='localhost',      # 本地电脑
    user='root',           # 默认用户名
    password='123456',     # 你的密码
    database='mysql'       # 默认数据库
)
print("✅ 连接成功！")

# 3. 创建游标（可以理解为"操作手柄"）
cursor = connection.cursor()

# 4. 执行一个简单的查询
cursor.execute("SHOW DATABASES;")  # 查看有哪些数据库

# 5. 获取结果
databases = cursor.fetchall()
print("\n📁 电脑上的数据库列表：")
for db in databases:
    print(f"  - {db[0]}")

# 6. 关闭连接
cursor.close()
connection.close()
print("\n🎉 恭喜！你完成了第一次数据库操作！")