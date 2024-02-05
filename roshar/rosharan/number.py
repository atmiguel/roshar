from enum import Enum
from typing import Mapping


class RosharanNumber(Enum):
    def __new__(cls, *args):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, suffix):
        self.suffix = suffix

    # From https://stormlightarchive.fandom.com/wiki/Calendar:
    Jes = "es"
    Nan = "an"
    Chach = "ach"
    Vev = "ev"
    Palah = "ah"
    Shash = "ash"
    Betab = "ab"
    Kak = "ak"
    Tanat = "at"
    Ishi = "ish"


ROSHARAN_NUMBERS_BY_VALUE: Mapping[int, RosharanNumber] = {
    number.value: number
    for number in RosharanNumber
}

ROSHARAN_NUMBERS_BY_NAME: Mapping[str, RosharanNumber] = {
    number.name: number
    for number in RosharanNumber
}
