@REM 删除旧的 build, dist 文件夹及其子文件夹
rd /s /q build
rd /s /q dist

@REM 构建
poetry run pyinstaller --onefile --hidden-import app app.py

@REM 复制 static 文件夹到 dist 文件夹
xcopy /s /y static dist\static
