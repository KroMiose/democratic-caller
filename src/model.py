import time
from enum import Enum
from hashlib import md5
from typing import List, Optional, Union

from pydantic import BaseModel

from src.logger import logger
from src.utils.keyboard import key_down, key_up, simulate_key

# class Key(Enum):
#     ArrowLeft = "left"
#     ArrowRight = "right"
#     ArrowUp = "up"
#     ArrowDown = "down"
#     W = "w"
#     A = "a"
#     S = "s"
#     D = "d"
#     CTRL = "ctrl"

class Key(Enum):
    ArrowLeft = 0x25
    ArrowRight = 0x27
    ArrowUp = 0x26
    ArrowDown = 0x28
    W = 0x57
    A = 0x41
    S = 0x53
    D = 0x44
    CTRL = 0x11


class Stratagem(BaseModel):
    id: str
    name: str
    name_zh: str
    icon: str
    short_name_zh: str
    short_code: str
    spell_seq: List[Union[int, str]]

    def get_spell_seq(self) -> List[Key]:
        return [Key(value) for value in self.spell_seq]

    @classmethod
    def gen_by_short_code(
        cls,
        name: str,
        name_zh: str,
        short_name_zh: str,
        short_code: str,
        icon: str,
    ):
        _seq: List[Union[int, str]] = []
        for ch in short_code:
            assert ch.lower() in [
                "w",
                "a",
                "s",
                "d",
            ], f"`{name_zh}` 使用了不支持的按键: {ch}"
            _seq.append(Key[ch.upper()].value)
        _id = md5(name.encode()).hexdigest()
        return cls(
            id=_id,
            name=name,
            name_zh=name_zh,
            short_name_zh=short_name_zh,
            short_code=short_code,
            spell_seq=_seq,
            icon=icon,
        )

    def call(self):
        logger.info(f"Calling {self.name_zh}")
        key_down(Key.CTRL.value)
        time.sleep(0.02)
        for key in self.get_spell_seq():
            simulate_key(key.value)
            # deep_simulate_key(key.value)
        time.sleep(0.02)
        key_up(Key.CTRL.value)
