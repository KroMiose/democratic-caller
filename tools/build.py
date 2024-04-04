import os
import shutil
from pathlib import Path


def main():
    print("开始构建...")
    print(
        '正在删除旧的 build, dist 文件夹及其子文件夹... 如果出现提示 "目标 dist\\static 是文件名?" 请输入 "D" 继续...',
    )

    # 递归删除旧的 build 和 dist 文件夹及其子文件夹
    for folder in ("build", "dist"):
        folder_path = Path(folder)

        if folder_path.is_dir():
            shutil.rmtree(folder_path)

    # 构建
    os.system("poetry run pyinstaller --onefile --hidden-import app app.py")

    # 复制 static 文件夹到 dist 文件夹
    os.system("xcopy /s /y static dist\\static")

    print("构建完成, 应用已输出到 dist 文件夹, 请使用管理员权限运行 app.exe")
