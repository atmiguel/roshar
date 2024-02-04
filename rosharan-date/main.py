from dataclasses import dataclass
from functools import total_ordering
from typing import List, Mapping, Optional, Self


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


@total_ordering
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
            raise ValueError("year must be positive")

        if self.month < RosharanDate.MIN_MONTH:
            raise ValueError(f"month must be at least {RosharanDate.MIN_MONTH}")
        if self.month > RosharanDate.MAX_MONTH:
            raise ValueError(f"month must not exceed {RosharanDate.MAX_MONTH}")

        if self.week < RosharanDate.MIN_WEEK:
            raise ValueError(f"week must be at least {RosharanDate.MIN_WEEK}")
        if self.week > RosharanDate.MAX_WEEK:
            raise ValueError(f"week must not exceed {RosharanDate.MAX_WEEK}")

        if self.day < RosharanDate.MIN_DAY:
            raise ValueError(f"day must be at least {RosharanDate.MIN_DAY}")
        if self.day > RosharanDate.MAX_DAY:
            raise ValueError(f"day must not exceed {RosharanDate.MAX_DAY}")

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
            raise ValueError("expected name to start with month name")

        monthless_name = name[len(month_number.name):]
        for number in NUMBERS:
            if monthless_name.startswith(number.suffix):
                week_number = number
                break
        else:
            raise ValueError("expected name to have week suffix following month name")

        day_name = monthless_name[len(week_number.suffix):]
        for number in NUMBERS:
            if day_name == number.suffix:
                day_number = number
                break
        else:
            raise ValueError("expected name to end with day suffix")

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
        month_number = NUMBERS_BY_NAME.get(month_name)
        if month_number is None:
            raise ValueError("expected valid month name")

        week_number = NUMBERS_BY_NAME.get(week_name)
        if week_number is None:
            raise ValueError("expected valid week name")

        return cls(
            year=year,
            month=month_number.value,
            week=week_number.value,
            day=day,
        )

    def plus(
        self,
        *,
        days: Optional[int] = None,
        weeks: Optional[int] = None,
        months: Optional[int] = None,
        years: Optional[int] = None,
    ) -> Self:
        if all(v is None for v in (days, weeks, months, years)):
            raise ValueError("must specify at least one value")

        if days is None:
            days = 0
        elif days <= 0:
            raise ValueError("days must be positive")

        if weeks is None:
            weeks = 0
        elif weeks <= 0:
            raise ValueError("weeks must be positive")

        if months is None:
            months = 0
        elif months <= 0:
            raise ValueError("months must be positive")

        if years is None:
            years = 0
        elif years <= 0:
            raise ValueError("years must be positive")

        total_days = self.day + days
        new_day = (total_days - 1) % RosharanDate.MAX_DAY + 1

        carryover_weeks = (total_days - 1) // RosharanDate.MAX_DAY
        total_weeks = self.week + weeks + carryover_weeks
        new_week = (total_weeks - 1) % RosharanDate.MAX_WEEK + 1

        carryover_months = (total_weeks - 1) // RosharanDate.MAX_WEEK
        total_months = self.month + months + carryover_months
        new_month = (total_months - 1) % RosharanDate.MAX_MONTH + 1

        carryover_years = (total_months - 1) // RosharanDate.MAX_MONTH
        new_year = self.year + years + carryover_years

        return RosharanDate(
            year=new_year,
            month=new_month,
            week=new_week,
            day=new_day,
        )

    def minus(
        self,
        *,
        days: Optional[int] = None,
        weeks: Optional[int] = None,
        months: Optional[int] = None,
        years: Optional[int] = None,
    ) -> Self:
        if all(v is None for v in (days, weeks, months, years)):
            raise ValueError("must specify at least one value")

        if days is None:
            days = 0
        elif days <= 0:
            raise ValueError("days must be positive")

        if weeks is None:
            weeks = 0
        elif weeks <= 0:
            raise ValueError("weeks must be positive")

        if months is None:
            months = 0
        elif months <= 0:
            raise ValueError("months must be positive")

        if years is None:
            years = 0
        elif years <= 0:
            raise ValueError("years must be positive")

        total_days = self.day - days
        new_day = (total_days - 1) % RosharanDate.MAX_DAY + 1

        carryover_weeks = (total_days - 1) // RosharanDate.MAX_DAY
        total_weeks = self.week - weeks + carryover_weeks
        new_week = (total_weeks - 1) % RosharanDate.MAX_WEEK + 1

        carryover_months = (total_weeks - 1) // RosharanDate.MAX_WEEK
        total_months = self.month - months + carryover_months
        new_month = (total_months - 1) % RosharanDate.MAX_MONTH + 1

        carryover_years = (total_months - 1) // RosharanDate.MAX_MONTH
        new_year = self.year - years + carryover_years

        return RosharanDate(
            year=new_year,
            month=new_month,
            week=new_week,
            day=new_day,
        )

    def get_day_name(self) -> str:
        month_number = NUMBERS_BY_VALUE[self.month]
        week_number = NUMBERS_BY_VALUE[self.week]
        day_number = NUMBERS_BY_VALUE[self.day]

        return f"{month_number.name}{week_number.suffix}{day_number.suffix}"

    def __str__(self) -> str:
        return f"{self.year}.{self.month}.{self.week}.{self.day}"

    def __eq__(self, other: Self) -> bool:
        if self.year != other.year:
            return False

        if self.month != other.month:
            return False

        if self.week != other.week:
            return False

        if self.day != other.day:
            return False

        return True

    def __lt__(self, other: Self) -> bool:
        if self.year != other.year:
            return self.year < other.year

        if self.month != other.month:
            return self.month < other.month

        if self.week != other.week:
            return self.week < other.week

        return self.day < other.day
