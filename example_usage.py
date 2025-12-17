#!/usr/bin/env python3
"""
示例：如何在自己的代码中使用 simple-system-scanner
"""
# 假设 scanner.py 在同一目录下
import scanner

print("示例：使用 scanner 模块扫描用户主目录\n")
# 获取用户主目录路径
import os
home_dir = os.path.expanduser("~")

# 调用工具函数
info_list = scanner.get_file_info(home_dir)

# 打印前5个结果
print(f"用户主目录 '{home_dir}' 中的前5项：")
for i, item in enumerate(info_list[:5]):
    if i < 5:  # 只显示前5个
        print(f"  {item['name']} ({item['type']}) - {item['size']}")

print("\n提示：查看 scanner.py 以了解所有可用功能。")
