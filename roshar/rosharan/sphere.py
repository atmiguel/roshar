from enum import Enum
from typing import Mapping

# Each sphere has a:
# - gem size: chip, mark, broam
# - gem type: diamond, garnet, etc.

# Each gem type is associated with a different tier:
# - cheapest, less weight, etc


# From https://coppermind.net/wiki/Spheres#Value
class RosharanGemSize(Enum):
    def __new__(cls, *args):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, weight: int) -> None:
        self.weight = weight

    CHIP = 1
    MARK = 5
    BROAM = 20


# From https://coppermind.net/wiki/Spheres#Value
class RosharanGemTier(Enum):
    CHEAPEST = 1
    LESS_WEIGHT = 2
    MIDDLE_WEIGHT = 3
    PRIME_PAIR = 4
    HIGHEST = 5


# From https://coppermind.net/wiki/Spheres#Value
class RosharanGemType(Enum):
    def __new__(cls, *args):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, tier: RosharanGemTier) -> None:
        self.tier = tier

    Amethyst = RosharanGemTier.PRIME_PAIR
    Diamond = RosharanGemTier.CHEAPEST
    Emerald = RosharanGemTier.HIGHEST
    Garnet = RosharanGemTier.LESS_WEIGHT
    Heliodor = RosharanGemTier.LESS_WEIGHT
    Ruby = RosharanGemTier.MIDDLE_WEIGHT
    Sapphire = RosharanGemTier.PRIME_PAIR
    Smokestone = RosharanGemTier.MIDDLE_WEIGHT
    Topaz = RosharanGemTier.LESS_WEIGHT
    Zircon = RosharanGemTier.MIDDLE_WEIGHT


class RosharanSphere(Enum):
    def __new__(cls, *args):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, suffix):
        self.suffix = suffix

    # From https://coppermind.net/wiki/Spheres#Value
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
