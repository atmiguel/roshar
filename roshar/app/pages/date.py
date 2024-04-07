import streamlit as st

from roshar.rosharan.date import RosharanDate
from typing import Optional


# From https://roshar.17thshard.com/#/en-US/events/kaladin-joins-bridge-four:
# 1173.7.9.3 - Kaladin joins Bridge Four
INITIAL_DATE = RosharanDate(1173, 7, 9, 3)


def display_integer_input(
    *,
    default: int,
    key: Optional[str] = None,
    label: str,
    max: Optional[int] = None,
    min: Optional[int] = None,
) -> int:
    return st.number_input(
        key=key,
        label=label,
        max_value=max,
        min_value=min,
        step=1,
        value=default,
    )


def display_date_input(*, INITIAL_DATE: RosharanDate) -> RosharanDate:
    columns = st.columns(4)

    with columns[0]:
        year = display_integer_input(
            default=INITIAL_DATE.year,
            label="Year",
        )

    with columns[1]:
        month = display_integer_input(
            default=INITIAL_DATE.month,
            label="Month",
            max=RosharanDate.MAX_MONTH,
            min=RosharanDate.MIN_MONTH,
        )

    with columns[2]:
        # TODO: on change that pairs inputs together
        week = display_integer_input(
            default=INITIAL_DATE.week,
            label="Week",
            max=RosharanDate.MAX_WEEK,
            min=RosharanDate.MIN_WEEK,
        )

        # # TODO: on change that pairs inputs together
        # st.selectbox(
        #     label="Week Name",
        #     options=[number.name for number in RosharanNumber],
        #     index=week - 1,
        # )

    with columns[3]:
        day = display_integer_input(
            default=INITIAL_DATE.day,
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


def display_year_input(*, key: str) -> int:
    return display_integer_input(
        default=INITIAL_DATE.year,
        key=key,
        label="Year",
    )


def display_week_input(*, key: str) -> int:
    return display_integer_input(
        default=INITIAL_DATE.week,
        key=key,
        label="Week",
        max=RosharanDate.MAX_WEEK,
        min=RosharanDate.MIN_WEEK,
    )


def display_day_input(*, key: str) -> int:
    return display_integer_input(
        default=INITIAL_DATE.day,
        key=key,
        label="Day",
        max=RosharanDate.MAX_DAY,
        min=RosharanDate.MIN_DAY,
    )


def display_day_name_input() -> RosharanDate:
    columns = st.columns(2)

    with columns[0]:
        year = display_year_input(key="day_name_year")

    with columns[1]:
        day_names = list(RosharanDate.list_all_day_names().keys())
        day_name = st.selectbox(
            index=day_names.index(INITIAL_DATE.get_day_name()),
            label="Day Name",
            options=day_names,
        )

    return RosharanDate.from_day_name(
        day_name=day_name,
        year=year,
    )


def display_week_name_input() -> RosharanDate:
    columns = st.columns(3)

    with columns[0]:
        year = display_year_input(key="week_name_year")

    with columns[1]:
        week_names = list(RosharanDate.list_all_week_names().keys())
        week_name = st.selectbox(
            label="Week Name",
            options=week_names,
            index=week_names.index(INITIAL_DATE.get_week_name()),
        )

    with columns[2]:
        day = display_day_input(key="week_name_day")

    return RosharanDate.from_week_name(
        day=day,
        week_name=week_name,
        year=year,
    )


def display_month_name_input() -> RosharanDate:
    columns = st.columns(4)

    with columns[0]:
        year = display_year_input(key="month_name_year")

    with columns[1]:
        month_names = list(RosharanDate.list_all_month_names().keys())
        month_name = st.selectbox(
            label="Month Name",
            options=month_names,
            index=month_names.index(INITIAL_DATE.get_month_name()),
        )

    with columns[2]:
        week = display_week_input(key="month_name_week")

    with columns[3]:
        day = display_day_input(key="month_name_day")

    return RosharanDate.from_month_name(
        day=day,
        week=week,
        month_name=month_name,
        year=year,
    )


if __name__ == "__main__":
    st.title("Rosharan Date")

    # TODO(adrian@gradient.ai, 04/05/2024): make a selector to choose how dates will be entered
    period_name = st.selectbox(
        label="Name",
        options=["Day", "Week", "Month"],
    )

    match period_name:
        case "Day":
            date = display_day_name_input()
        case "Week":
            date = display_week_name_input()
        case "Month":
            date = display_month_name_input()
        case _:
            raise Exception(f"period_name unexpected: {period_name}")

    st.divider()

    date_id_columns = st.columns(2)
    with date_id_columns[0]:
        st.subheader("Date ID")
    with date_id_columns[1]:
        st.subheader(str(date))

    st.divider()

    date_names_columns = st.columns(3)
    with date_names_columns[0]:
        st.subheader("Month Name")
        st.write(date.get_month_name())

    with date_names_columns[1]:
        st.subheader("Week Name")
        st.write(date.get_week_name())

    with date_names_columns[2]:
        st.subheader("Day Name")
        st.write(date.get_day_name())
