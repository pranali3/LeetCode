from datetime import datetime, timedelta


def split_datetime_range(start_date: datetime, end_date: datetime, interval_duration: timedelta):
    current_date = start_date
    while current_date < end_date:
        yield current_date
        current_date += interval_duration


if __name__ == "__main__":
    # Example usage:
    start_datetime = datetime(2022, 1, 1, 12, 0, 0)
    end_datetime = datetime(2022, 1, 5, 12, 0, 0)
    interval_duration = timedelta(days=1)
    # intervals = list(split_datetime_range(start_datetime, end_datetime, interval_duration))
    print(split_datetime_range(start_datetime, end_datetime, interval_duration))

    # for interval in intervals:
    #     print(interval)
