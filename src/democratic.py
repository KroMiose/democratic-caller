import ctypes
import json
from enum import Enum
from typing import List

from src.model import Stratagem

STRATAGEM_LIST: List[Stratagem]


with open("./static/stratagem.json", "r", encoding="utf-8") as f:  # noqa: PTH123
    data = json.loads(f.read())
    STRATAGEM_LIST = [
        Stratagem.gen_by_short_code(
            name=d["name"],
            name_zh=d["name_zh"],
            short_name_zh=d["short_name_zh"],
            short_code=d["short_code"],
            icon=d["icon"],
        )
        for d in data
    ]
