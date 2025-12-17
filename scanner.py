#!/usr/bin/env python3
"""
simple-system-scanner
A lightweight tool to list file information in a specified directory.
"""

import os
import sys
import time
from pathlib import Path

def format_size(size_bytes):
    """将字节数转换为可读的单位（KB, MB, GB）。"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"

def get_file_info(directory_path="."):
    """
    扫描目录并返回文件信息列表。
    
    Args:
        directory_path (str): 要扫描的目录路径，默认为当前目录。
    
    Returns:
        list: 包含文件信息的字典列表。
    """
    path = Path(directory_path)
    if not path.exists() or not path.is_dir():
        print(f"错误：路径 '{directory_path}' 不存在或不是一个目录。")
        return []

    file_info_list = []
    for item in path.iterdir():
        stat = item.stat()
        file_type = "目录" if item.is_dir() else "文件"
        file_info = {
            "name": item.name,
            "type": file_type,
            "size": format_size(stat.st_size) if item.is_file() else "--",
            "modified": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat.st_mtime))
        }
        file_info_list.append(file_info)
    
    return file_info_list

def print_table(file_info_list):
    """以表格形式打印文件信息。"""
    if not file_info_list:
        print("未找到任何文件或目录。")
        return
    
    print(f"{'名称':<30} {'类型':<10} {'大小':<15} {'修改时间':<20}")
    print("-" * 80)
    for info in file_info_list:
        print(f"{info['name']:<30} {info['type']:<10} {info['size']:<15} {info['modified']:<20}")

def main():
    """主函数，处理命令行参数并执行扫描。"""
    print("=== 简易系统文件扫描器 ===\n")
    
    # 支持命令行参数指定目录，默认当前目录
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    
    print(f"正在扫描目录: {os.path.abspath(target_dir)}\n")
    
    files = get_file_info(target_dir)
    print_table(files)
    
    print(f"\n扫描完成，共找到 {len(files)} 个项目。")

if __name__ == "__main__":
    main()
