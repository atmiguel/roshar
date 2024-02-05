from dataclasses import dataclass
from typing import List, Mapping


@dataclass(frozen=True, kw_only=True)
class RosharanNumber:
    name: str
    suffix: str
    value: int


ROSHARAN_NUMBERS: List[RosharanNumber] = [
    RosharanNumber(
        name=name,
        suffix=suffix,
        value=index + 1,
    )
    # From https://stormlightarchive.fandom.com/wiki/Calendar:
    for index, (name, suffix) in enumerate([
        ("Jes", "es"),
        ("Nan", "an"),
        ("Chach", "ach"),
        ("Vev", "ev"),
        ("Palah", "ah"),
        ("Shash", "ash"),
        ("Betab", "ab"),
        ("Kak", "ak"),
        ("Tanat", "at"),
        ("Ishi", "ish"),
    ])
]

ROSHARAN_NUMBERS_BY_VALUE: Mapping[int, RosharanNumber] = {
    number.value: number
    for number in ROSHARAN_NUMBERS
}

ROSHARAN_NUMBERS_BY_NAME: Mapping[str, RosharanNumber] = {
    number.name: number
    for number in ROSHARAN_NUMBERS
}
