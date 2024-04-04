import os
import sys
from pathlib import Path


def main():
    print("开始构建...")
    print(
        '正在删除旧的 build, dist 文件夹及其子文件夹... 如果出现提示 "目标 dist\\static 是文件名?" 请输入 "D" 继续...',
    )

    # 删除旧的 build, dist 文件夹及其子文件夹
    for path in Path().glob("build"):
        path.rmdir()

    for path in Path().glob("dist"):
        path.rmdir()

    # 构建
    os.system("poetry run pyinstaller --onefile --hidden-import app app.py")

    # 复制 static 文件夹到 dist 文件夹
    os.system("xcopy /s /y static dist\\static")

    print("构建完成, 应用已输出到 dist 文件夹, 请使用管理员权限运行 app.exe")
