from dataclasses import dataclass
from typing import Self, Mapping, List


@dataclass(frozen=True, kw_only=True)
class RosharanMonth:
    name: str
    suffix: str


# From https://stormlightarchive.fandom.com/wiki/Calendar:
MONTHS: List[RosharanMonth] = [
    RosharanMonth(name="Jes", suffix="es"),
    RosharanMonth(name="Nan", suffix="an"),
    RosharanMonth(name="Chach", suffix="ach"),
    RosharanMonth(name="Vev", suffix="ev"),
    RosharanMonth(name="Palah", suffix="ah"),
    RosharanMonth(name="Shash", suffix="ash"),
    RosharanMonth(name="Betab", suffix="ab"),
    RosharanMonth(name="Kak", suffix="ak"),
    RosharanMonth(name="Tanat", suffix="at"),
    RosharanMonth(name="Ishi", suffix="ish"),
]

MONTHS_BY_NUMBER: Mapping[int, RosharanMonth] = {
    index + 1: month
    for index, month in enumerate(MONTHS)
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
        # From https://stormlightarchive.fandom.com/wiki/Calendar:
        # #     Name    Suffix
        # 1     Jes     es
        # 2     Nan     an
        # 3     Chach   ach
        # 4     Vev     ev
        # 5     Palah   ah
        # 6     Shash   ash
        # 7     Betab   ab
        # 8     Kak     ak
        # 9     Tanat   at
        # 10    Ishi    ish

        # todo
        # get what the name starts with
        # chop it and do it again, but with suffixes
        # chop it and do it again, but with suffixes
        pass

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


if __name__ == "__main__":
    date = RosharanDate(
        year=1171,
        month=2,
        week=3,
        day=4,
    )

    print(date)

    date = RosharanDate(
        year=1171,
        month=11,
        week=3,
        day=4,
    )
