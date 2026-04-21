import sys
import platform

print("=" * 50)
print("🐍 Python环境诊断报告")
print("=" * 50)

# 1. Python版本
print(f"Python版本: {sys.version}")
print(f"版本号: {platform.python_version()}")

# 2. 版本检查
version_tuple = sys.version_info
print(f"\n版本详情: {version_tuple}")
print(f"主版本: {version_tuple.major}")
print(f"次版本: {version_tuple.minor}")
print(f"微版本: {version_tuple.micro}")

# 3. 检查是否符合要求
if version_tuple.major == 3 and version_tuple.minor >= 8:
    print("\n✅ Python版本符合要求 (>= 3.8)")
else:
    print(f"\n❌ Python版本过低: {platform.python_version()}")
    print("需要升级到Python 3.8或更高版本")

# 4. 检查Jupyter相关包
print("\n" + "=" * 50)
print("📦 检查Jupyter相关包")
print("=" * 50)

required_packages = ['ipykernel', 'jupyter', 'notebook']
for package in required_packages:
    try:
        __import__(package)
        print(f"✅ {package}: 已安装")
    except ImportError:
        print(f"❌ {package}: 未安装")

print("\n" + "=" * 50)
print("💡 建议操作:")
if version_tuple.minor < 8:
    print("1. 升级Python到3.8+版本")
    print("2. 或创建新conda环境")
print("3. 安装缺少的包: pip install ipykernel jupyter notebook")
print("=" * 50)