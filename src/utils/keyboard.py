import ctypes
import random
import time

KEYEVENTF_KEYDOWN = 0x0000
KEYEVENTF_KEYUP = 0x0002


def key_down(key: int):
    ctypes.windll.user32.keybd_event(key, 0, KEYEVENTF_KEYDOWN, 0)


def key_up(key: int):
    ctypes.windll.user32.keybd_event(key, 0, KEYEVENTF_KEYUP, 0)


def simulate_key(key: int, delay: float = random.uniform(0.02, 0.05)):
    key_down(key)
    time.sleep(0.02)
    key_up(key)
    time.sleep(delay)
