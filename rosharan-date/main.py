from dataclasses import dataclass


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


if __name__ == "__main__":
    date = RosharanDate(
        year=1171,
        month=2,
        week=3,
        day=4,
    )

    print(date.year)

    date = RosharanDate(
        year=1171,
        month=11,
        week=3,
        day=4,
    )
