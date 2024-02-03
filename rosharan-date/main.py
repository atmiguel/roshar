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

    @staticmethod
    def _validate_date(
        *,
        year: int,
        month: int,
        week: int,
        day: int,
    ) -> None:
        if year <= 0:
            raise ValueError(f"Year must be positive, but was {year}")

        if month < RosharanDate.MIN_MONTH:
            raise ValueError(f"Month must be at least {RosharanDate.MIN_MONTH}, but was {month}")
        if month > RosharanDate.MAX_MONTH:
            raise ValueError(f"Month must not exceed {RosharanDate.MAX_MONTH}, but was {month}")

        if week < RosharanDate.MIN_WEEK:
            raise ValueError(f"Week must be at least {RosharanDate.MIN_WEEK}, but was {week}")
        if week > RosharanDate.MAX_WEEK:
            raise ValueError(f"Week must not exceed {RosharanDate.MAX_WEEK}, but was {week}")

        if day < RosharanDate.MIN_DAY:
            raise ValueError(f"Day must be at least {RosharanDate.MIN_DAY}, but was {day}")
        if day > RosharanDate.MAX_DAY:
            raise ValueError(f"Day must not exceed {RosharanDate.MAX_DAY}, but was {day}")

    def __init__(
        self,
        *,
        year: int,
        month: int,
        week: int,
        day: int,
    ) -> None:
        self.year = year
        self.month = month
        self.week = week
        self.day = day

        RosharanDate._validate_date(
            year=year,
            month=month,
            week=week,
            day=day,
        )


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