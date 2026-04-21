# 在VS Code中新建test_mysql.py
import pymysql

# 尝试连接
try:
    # 用最简单的配置
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',  # 你设置的密码
        database='mysql'    # 用默认的mysql数据库
    )
    print("✅ 连接成功！")
    
    # 关闭连接
    connection.close()
    
except Exception as e:
    print(f"❌ 连接失败：{e}")
    print("\n可能的原因：")
    print("1. MySQL服务没启动")
    print("2. 密码不对")
    print("3. 没安装pymysql")
    