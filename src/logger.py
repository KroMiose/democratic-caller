import time

from miose_toolkit_logger import logger

# 设置日志等级
logger.set_log_level("DEBUG")

# 设置日志格式
logger.set_log_format(
    "<g>{time:MM-DD HH:mm:ss}</g> "
    "[<lvl>{level}</lvl>] "
    "<c><u>{name}</u></c> | "
    "<c>{function}:{line}</c> | "
    "{message}",
)

# 设置日志输出到文件 (with_console=True 表示同时输出到控制台)
logger.set_log_output(f"logs/{time.strftime('%Y-%m-%d')}.log", with_console=True)
