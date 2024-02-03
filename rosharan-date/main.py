from dataclasses import dataclass
from typing import Self, Mapping, List


@dataclass(frozen=True, kw_only=True)
class RosharanNumber:
    name: str
    suffix: str
    value: int


NUMBERS: List[RosharanNumber] = [
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

NUMBERS_BY_VALUE: Mapping[int, RosharanNumber] = {
    number.value: number
    for number in NUMBERS
}
NUMBERS_BY_NAME: Mapping[str, RosharanNumber] = {
    number.name: number
    for number in NUMBERS
}
NUMBERS_BY_SUFFIX: Mapping[str, RosharanNumber] = {
    number.suffix: number
    for number in NUMBERS
}


@dataclass(frozen=True)
class RosharanDate:
    year: int
    month: int
    week: int
    day: int

    MIN_MONTH = 1
    MAX_MONTH = 10

    MIN_WEEK = 1
    MAX_WEEK = 10

    MIN_DAY = 1
    MAX_DAY = 5

    def __post_init__(self) -> None:
        if self.year <= 0:
            raise ValueError(f"Year must be positive, but was {self.year}")

        if self.month < RosharanDate.MIN_MONTH:
            raise ValueError(f"Month must be at least {RosharanDate.MIN_MONTH}, but was {self.month}")
        if self.month > RosharanDate.MAX_MONTH:
            raise ValueError(f"Month must not exceed {RosharanDate.MAX_MONTH}, but was {self.month}")

        if self.week < RosharanDate.MIN_WEEK:
            raise ValueError(f"Week must be at least {RosharanDate.MIN_WEEK}, but was {self.week}")
        if self.week > RosharanDate.MAX_WEEK:
            raise ValueError(f"Week must not exceed {RosharanDate.MAX_WEEK}, but was {self.week}")

        if self.day < RosharanDate.MIN_DAY:
            raise ValueError(f"Day must be at least {RosharanDate.MIN_DAY}, but was {self.day}")
        if self.day > RosharanDate.MAX_DAY:
            raise ValueError(f"Day must not exceed {RosharanDate.MAX_DAY}, but was {self.day}")

    @classmethod
    def from_name(
        cls,
        *,
        name: str,
        year: int,
    ) -> Self:
        for number in NUMBERS:
            if name.startswith(number.name):
                month_number = number
                break
        else:
            raise ValueError(f"Expected name to start with month name, but was {name}")

        monthless_name = name[len(month_number.name):]
        for number in NUMBERS:
            if monthless_name.startswith(number.suffix):
                week_number = number
                break
        else:
            raise ValueError(f"Expected name to contain valid week suffix, but was {name}")

        day_name = monthless_name[len(week_number.suffix):]
        for number in NUMBERS:
            if day_name == number.suffix:
                day_number = number
                break
        else:
            raise ValueError(f"Expected name to contain valid day suffix, but was {name}")

        return cls(
            year=year,
            month=month_number.value,
            week=week_number.value,
            day=day_number.value,
        )

    @classmethod
    def from_names(
        cls,
        *,
        day: int,
        month_name: str,
        week_name: str,
        year: int,
    ) -> Self:
        pass

    def __str__(self) -> str:
        return f"{self.year}.{self.month}.{self.week}.{self.day}"

    # todo: eq, comparators
    # todo: different format printers


if __name__ == "__main__":
    date = RosharanDate.from_name(
        name="Chachanan",
        year=1171,
    )
    date2 = RosharanDate.from_name(
        name="Jesachev",
        year=1171,
    )
    # todo: figure out kaktach (should be kakatach)
    # date3 = RosharanDate.from_name(
    #     name="Kaktach",
    #     year=1171,
    # )

    print(date)
    print(date2)
