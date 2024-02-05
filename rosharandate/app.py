import streamlit as st

from rosharandate.rosharan_date import RosharanDate
from typing import Optional


# From https://roshar.17thshard.com/#/en-US/events/kaladin-joins-bridge-four:
# 1173.7.9.3 - Kaladin joins Bridge Four
DEFAULT_DATE = RosharanDate(1173, 7, 9, 3)


def create_integer_input(
    *,
    default: int,
    label: str,
    max: Optional[int] = None,
    min: Optional[int] = None,
) -> int:
    return st.number_input(
        label=label,
        max_value=max,
        min_value=min,
        step=1,
        value=default,
    )


def get_input_date() -> RosharanDate:
    columns = st.columns(4)

    with columns[0]:
        year = create_integer_input(
            default=DEFAULT_DATE.year,
            label="Year",
        )

    with columns[1]:
        month = create_integer_input(
            default=DEFAULT_DATE.month,
            label="Month",
            max=RosharanDate.MAX_MONTH,
            min=RosharanDate.MIN_MONTH,
        )

    with columns[2]:
        week = create_integer_input(
            default=DEFAULT_DATE.week,
            label="Week",
            max=RosharanDate.MAX_WEEK,
            min=RosharanDate.MIN_WEEK,
        )

        week_name = st.selectbox(
            "Week Name",
            ("Shash", "Palah"),
        )
        print(week_name)

    with columns[3]:
        day = create_integer_input(
            default=DEFAULT_DATE.day,
            label="Day",
            max=RosharanDate.MAX_DAY,
            min=RosharanDate.MIN_DAY,
        )

    return RosharanDate(
        year=year,
        month=month,
        week=week,
        day=day,
    )


if __name__ == "__main__":
    st.title("Rosharan Date")

    input_date = get_input_date()
    print(input_date)
