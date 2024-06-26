from dataclasses import dataclass
from functools import total_ordering
from typing import Optional, Self, Mapping, Tuple, Any
from roshar.rosharan.constants import (
    DATE_VALUES_BY_DAY_NAME,
    DATE_VALUES_BY_WEEK_NAME,
)
from roshar.rosharan.number import (
    ROSHARAN_NUMBERS_BY_VALUE,
    ROSHARAN_NUMBERS_BY_VORIN_NAME,
)


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
    def from_day_name(
        cls,
        *,
        day_name: str,
        year: int,
    ) -> Self:
        date_values = DATE_VALUES_BY_DAY_NAME.get(day_name)
        if date_values is None:
            raise ValueError("invalid day name")

        month, week, day = date_values

        return cls(
            year=year,
            month=month,
            week=week,
            day=day,
        )

    @classmethod
    def from_week_name(
        cls,
        *,
        day: int,
        week_name: str,
        year: int,
    ) -> Self:
        date_values = DATE_VALUES_BY_WEEK_NAME.get(week_name)
        if date_values is None:
            raise ValueError("invalid week name")

        month, week = date_values

        return cls(
            year=year,
            month=month,
            week=week,
            day=day,
        )

    @classmethod
    def from_month_name(
        cls,
        *,
        day: int,
        month_name: str,
        week: int,
        year: int,
    ) -> Self:
        month_number = ROSHARAN_NUMBERS_BY_VORIN_NAME.get(month_name)
        if month_number is None:
            raise ValueError("invalid month name")

        return cls(
            year=year,
            month=month_number.value,
            week=week,
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

    def get_month_name(self) -> str:
        month_number = ROSHARAN_NUMBERS_BY_VALUE[self.month]
        return month_number.vorin_name

    def get_week_name(self) -> str:
        match (self.month, self.week):
            case (1, 2):
                # Found in TWoK Chapter 4
                return "Jesnan"
            case (10, 6):
                # Found in TWoK Chapter 8
                return "Ishash"

        week_number = ROSHARAN_NUMBERS_BY_VALUE[self.week]
        return f"{self.get_month_name()}{week_number.suffix}"

    def get_day_name(self) -> str:
        day_number = ROSHARAN_NUMBERS_BY_VALUE[self.day]
        return f"{self.get_week_name()}{day_number.suffix}"

    def __str__(self) -> str:
        return f"{self.year}.{self.month}.{self.week}.{self.day}"

    def __eq__(self, other: Self) -> bool:
        return (
            self.year == other.year and
            self.month == other.month and
            self.week == other.week and
            self.day == other.day
        )

    def __lt__(self, other: Self) -> bool:
        if self.year != other.year:
            return self.year < other.year

        if self.month != other.month:
            return self.month < other.month

        if self.week != other.week:
            return self.week < other.week

        return self.day < other.day

    @staticmethod
    def list_all_day_names() -> Mapping[str, Tuple[int, int, int]]:
        all_day_names = {}

        for month in range(RosharanDate.MIN_MONTH, RosharanDate.MAX_MONTH + 1):
            for week in range(RosharanDate.MIN_WEEK, RosharanDate.MAX_WEEK + 1):
                for day in range(RosharanDate.MIN_DAY, RosharanDate.MAX_DAY + 1):
                    date = RosharanDate(
                        year=1,
                        month=month,
                        week=week,
                        day=day,
                    )

                    all_day_names[date.get_day_name()] = (month, week, day)

        return all_day_names

    @staticmethod
    def list_all_week_names() -> Mapping[str, Tuple[int, int]]:
        all_week_names = {}

        for month in range(RosharanDate.MIN_MONTH, RosharanDate.MAX_MONTH + 1):
            for week in range(RosharanDate.MIN_WEEK, RosharanDate.MAX_WEEK + 1):
                date = RosharanDate(
                    year=1,
                    month=month,
                    week=week,
                    day=1,
                )

                all_week_names[date.get_week_name()] = (month, week)

        return all_week_names

    @staticmethod
    def list_all_month_names() -> Mapping[str, int]:
        all_month_names = {}

        for month in range(RosharanDate.MIN_MONTH, RosharanDate.MAX_MONTH + 1):
            date = RosharanDate(
                year=1,
                month=month,
                week=1,
                day=1,
            )

            all_month_names[date.get_month_name()] = month

        return all_month_names


def _print_mapping(mapping: Mapping[str, Any], /) -> None:
    print("{")
    for key, value in mapping.items():
        print(f"    \"{key}\": {value},")
    print("}")


if __name__ == "__main__":
    _print_mapping(RosharanDate.list_all_day_names())
    _print_mapping(RosharanDate.list_all_week_names())
    # TODO: Kakatach fits the pattern, but Kaktach is in Book 1: Chapter 66 epigraph
