#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
大一学生Python 3.10环境配置脚本
针对官方原版Python 3.10
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复乱码的测试脚本
"""

import sys
import io

# 强制设置标准输出编码为UTF-8
if sys.stdout.encoding != 'UTF-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='ignore')

if sys.stderr.encoding != 'UTF-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='ignore')

# 设置系统编码
sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None

print("=" * 50)
print("🎉 编码测试开始")
print("=" * 50)

# 测试各种字符
test_chars = [
    "✅ 英文字符: Hello World",
    "✅ 中文字符: 你好世界",
    "✅ 特殊符号: 🐍✨🎯🚀",
    "✅ 数学符号: ∑ ∫ ± ∞",
    "✅ 表情符号: 😀 🎉 💻 📚"
]

for line in test_chars:
    print(line)

print("=" * 50)
print("📊 系统编码信息:")
print(f"   文件系统编码: {sys.getfilesystemencoding()}")
print(f"   标准输出编码: {sys.stdout.encoding}")
print(f"   默认编码: {sys.getdefaultencoding()}")
print(f"   平台: {sys.platform}")
print("=" * 50)
import subprocess
import sys
import os
import time

def run_pip_command(pkg_desc, pip_args):
    """运行pip命令"""
    print(f"\n📦 {pkg_desc}")
    print(f"   命令: pip {pip_args}")
    print("   " + "-" * 40)
    
    try:
        # 使用当前Python的pip
        cmd = [sys.executable, "-m", "pip"] + pip_args.split()
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        if result.returncode == 0:
            print("   ✅ 安装成功")
            # 显示简要信息
            for line in result.stdout.split('\n'):
                if any(keyword in line.lower() for keyword in ['success', 'installed', 'already', 'version']):
                    if line.strip():
                        print(f"      {line}")
            return True
        else:
            print("   ❌ 安装失败")
            if result.stderr:
                print(f"      错误: {result.stderr[:200]}")
            return False
            
    except Exception as e:
        print(f"   ❌ 异常: {str(e)[:100]}")
        return False

def main():
    print("=" * 60)
    print("🎯 Python 3.10 学习环境配置")
    print("=" * 60)
    
    print(f"\n📊 当前Python信息:")
    print(f"    版本: {sys.version}")
    print(f"    路径: {sys.executable}")
    
    if "anaconda" in sys.executable.lower():
        print("\n⚠️  警告：检测到Anaconda环境")
        print("    建议使用官方Python 3.10，是否继续？(y/n)")
        if input().strip().lower() != 'y':
            return
    
    print("\n📋 将安装以下组件:")
    print("    1. Jupyter Notebook（交互式编程）")
    print("    2. NumPy、Pandas（数据处理）")
    print("    3. Matplotlib（绘图）")
    print("    4. VS Code工具包")
    
    print("\n⏱️  预计时间: 5-10分钟（取决于网速）")
    print("=" * 60)
    
    confirm = input("\n是否开始安装？(y/n): ").strip().lower()
    if confirm != 'y':
        print("安装已取消")
        return
    
    # 安装步骤
    steps = [
        ("升级pip", "install --upgrade pip"),
        ("Jupyter核心", "install jupyter notebook ipykernel"),
        ("数据处理", "install numpy pandas"),
        ("科学计算", "install scipy scikit-learn"),
        ("数据可视化", "install matplotlib seaborn"),
        ("开发工具", "install pylance black autopep8"),
        ("Jupyter内核注册", f"-m ipykernel install --user --name=python{sys.version_info.major}{sys.version_info.minor} --display-name=\"Python {sys.version_info.major}.{sys.version_info.minor}\"")
    ]
    
    success_count = 0
    for desc, args in steps:
        if "ipykernel install" in args:
            # 特殊处理内核注册
            print(f"\n🔧 {desc}")
            cmd = [sys.executable] + args.split()
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print("   ✅ 内核注册成功")
                success_count += 1
            else:
                print("   ❌ 内核注册失败")
        else:
            if run_pip_command(desc, args):
                success_count += 1
        time.sleep(1)
    
    # 配置报告
    print("\n" + "=" * 60)
    print("📊 配置完成报告")
    print("=" * 60)
    print(f"✅ 成功步骤: {success_count}/{len(steps)}")
    
    if success_count >= len(steps) - 1:  # 允许一个失败
        print("\n🎉 环境配置成功！")
        print("\n💡 下一步操作：")
        print("1. 重启 VS Code")
        print("2. 按 Ctrl+Shift+P")
        print("3. 输入: Python: Select Interpreter")
        print(f"4. 选择: Python {sys.version_info.major}.{sys.version_info.minor} 版本")
        print("5. 创建新文件 test.ipynb 或 test.py")
        print("6. 测试运行")
        
        print("\n📁 示例代码位置:")
        print("   桌面或D盘创建文件夹: my_python_code")
        print("   在VS Code中打开此文件夹")
    else:
        print("\n⚠️  部分组件安装失败")
        print("\n建议：")
        print("1. 检查网络连接")
        print("2. 以管理员身份运行VS Code")
        print("3. 手动安装: pip install jupyter")
    
    print("=" * 60)
    input("\n按回车键退出...")

if __name__ == "__main__":
    main()