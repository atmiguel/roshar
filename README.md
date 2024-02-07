# Roshar 

## Get Started

Run setup script:
```bash
bash setup.sh
```

To start streamlit app:
```bash
poetry shell
streamlit run roshar/app/index.py
```

## RosharanDate

### Constructor

```python
RosharanDate(
    year=1171,
    month=6,
    week=5,
    day=1,
)

# or shorthand
RosharanDate(1171, 6, 5, 1)

# or using day name
RosharanDate.from_day_name(
    year=1171,
    day_name="Shashahes",
)

# or using week name
RosharanDate.from_week_name(
    year=1171,
    week_name="Shashah",
    day=1,
)

# or using month name
RosharanDate.from_month_name(
    year=1171,
    month_name="Shash",
    week=5,
    day=1,
)
```

### Difference

```python
date = RosharanDate(1171, 6, 5, 1)

one_day_later = date.plus(days=1)
two_weeks_later = date.plus(weeks=2)
three_months_later = date.plus(months=3)
four_years_later = date.plus(years=4)

some_time_later = date.plus(
    days=1000,
    weeks=11,
    months=9,
    years=27,
)

one_day_prior = date.minus(days=1)
two_weeks_prior = date.minus(weeks=2)
three_months_prior = date.minus(months=3)
four_years_prior = date.minus(years=4)

some_time_prior = date.minus(
    days=1000,
    weeks=11,
    months=9,
    years=27,
)
```

### Names

```python
date = RosharanDate(1171, 6, 5, 1)

print(date) # 1171.6.5.1
print(date.get_month_name()) # Shash
print(date.get_week_name()) # Shashah
print(date.get_day_name()) # Shashahes
```

### Comparable

```python
date1 = RosharanDate(1171, 6, 5, 1)
date2 = RosharanDate(1171, 6, 5, 2)

print(date1 == date2) # False
print(date1 < date2) # True
print(date1 > date2) # False
```

## Sources

https://stormlightarchive.fandom.com/wiki/Calendar
