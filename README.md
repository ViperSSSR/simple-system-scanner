# Simple System Scanner

一个轻量级的 Python 工具，用于扫描目录并清晰地展示文件和文件夹的基本信息（名称、类型、大小、修改时间）。

## 功能特性

- 扫描指定目录，识别文件和文件夹。
- 自动将文件大小转换为易读的单位（B, KB, MB, GB）。
- 以整洁的表格形式输出结果。
- 提供简单的配置选项（通过 `config.json`）。
- 可作为独立脚本运行，也可作为模块导入到其他项目中。

## 快速开始

### 前提条件
- 系统已安装 Python 3.6 或更高版本。

### 使用步骤
1. 将本项目下载到本地，或克隆仓库：
bash

git clone https://github.com/ViperSSSR/simple-system-scanner.git

2. 进入项目目录：
bash
cd simple-system-scanner
3. 运行主脚本：
bash
python scanner.py
默认会扫描当前目录。您也可以指定其他路径：
bash
python scanner.py /path/to/your/directory
### 作为模块使用
查看 `example_usage.py` 文件，了解如何在你自己的Python代码中导入和使用扫描功能。
## 项目结构
simple-system-scanner/
├── scanner.py          # 主工具脚本
├── config.json         # 配置文件
├── example_usage.py    # 使用示例
└── README.md           # 本文档
## 许可证
本项目基于 MIT 许可证开源。详情见 [LICENSE](LICENSE) 文件。

---

*这是我的第一个独立编程项目，一个用于了解文件系统的简单扫描工具。它标志着我的开发之旅从这里开始。*
