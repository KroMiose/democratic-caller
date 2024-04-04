# 导入需要的库
import random
import time
from ctypes import (
    POINTER,
    Structure,
    Union,
    byref,
    c_long,
    c_short,
    c_ulong,
    c_ushort,
    pointer,
    sizeof,
    windll,
)
import keyboard
import win32con

# 定义结构体和相关变量
PUL = POINTER(c_ulong)

class KeyBdInput(Structure):
    _fields_ = [
        ("wVk", c_ushort),
        ("wScan", c_ushort),
        ("dwFlags", c_ulong),
        ("time", c_ulong),
        ("dwExtraInfo", PUL),
    ]

class HardwareInput(Structure):
    _fields_ = [("uMsg", c_ulong), ("wParamL", c_short), ("wParamH", c_ushort)]

class MouseInput(Structure):
    _fields_ = [
        ("dx", c_long),
        ("dy", c_long),
        ("mouseData", c_ulong),
        ("dwFlags", c_ulong),
        ("time", c_ulong),
        ("dwExtraInfo", PUL),
    ]

class Input_I(Union):
    _fields_ = [("ki", KeyBdInput), ("mi", MouseInput), ("hi", HardwareInput)]

class Input(Structure):
    _fields_ = [("type", c_ulong), ("ii", Input_I)]

class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]

# 函数：按下按键
def key_down(key):
    FInputs = Input * 1
    extra = c_ulong(0)
    ii_ = Input_I()
    flag = 0x8
    ii_.ki = KeyBdInput(0, key, flag, 0, pointer(extra))
    InputBox = FInputs((1, ii_))
    windll.user32.SendInput(1, pointer(InputBox), sizeof(InputBox[0]))

# 函数：释放按键
def key_up(key):
    FInputs = Input * 1
    extra = c_ulong(0)
    ii_ = Input_I()
    flag = 0x8 | 0x2
    ii_.ki = KeyBdInput(0, key, flag, 0, pointer(extra))
    InputBox = FInputs((1, ii_))
    windll.user32.SendInput(1, pointer(InputBox), sizeof(InputBox[0]))

# 函数：模拟按键
def simulate_key(key, delay=random.uniform(0.02, 0.05)):
    key_down(key)
    time.sleep(0.02)
    key_up(key)
    time.sleep(delay)
