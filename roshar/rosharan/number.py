from enum import Enum
from typing import Mapping


class RosharanNumber(Enum):
    def __new__(cls, *args):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, vorin_name: str, suffix: str) -> None:
        self.vorin_name = vorin_name
        self.suffix = suffix

    # From https://stormlightarchive.fandom.com/wiki/Calendar:
    JES = "Jes", "es"
    NAN = "Nan", "an"
    CHACH = "Chach", "ach"
    VEV = "Vev", "ev"
    PALAH = "Palah", "ah"
    SHASH = "Shash", "ash"
    BETAB = "Betab", "ab"
    KAK = "Kak", "ak"
    TANAT = "Tanat", "at"
    ISHI = "Ishi", "ish"


ROSHARAN_NUMBERS_BY_VALUE: Mapping[int, RosharanNumber] = {
    number.value: number
    for number in RosharanNumber
}

ROSHARAN_NUMBERS_BY_VORIN_NAME: Mapping[str, RosharanNumber] = {
    number.vorin_name: number
    for number in RosharanNumber
}
