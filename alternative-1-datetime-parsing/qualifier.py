import datetime
import re

def parse_iso8601(timestamp: str) -> datetime.datetime:
    split = re.split("T", timestamp)
    date = split[0]
    try:
        time = split[1]
    except IndexError:
        # sets time at midnight 00:00:00 if time is not given
        time = '00:00:00'

    if not len(re.split("-", date)) == 3:
        raise(ValueError('Invalid Date Format'))

    if (len(re.split(":", time))) == 1:
        # sets hh:ss at 00:00 if not specified (hours, seconds)
        time += ':00:00'
    if (len(re.split(":", time))) == 2:
        # sets ss at 00 if not specified (seconds)
        time += ':00'
    if (len(re.split("-", date))) == 1:
        date += "-00-00"
    if (len(re.split("-", date))) == 2:
        date += "-00"

    date = re.split("-", date)
    time = re.split(":", time)

    print(date[0], date[1], date[2], time[0], time[1], time[2])

    if not len(date[1]) == 2:
        raise(ValueError('Month value must be 4 digits long'))

    if not len(date[2]) == 2:
        raise(ValueError('Day value must be 2 digits long'))

    y, m, d = int(date[0]), int(date[1]), int(date[2])
    H, M, S = int(time[0]), int(time[1]), int(time[2])

    datetime_object = datetime.datetime(y, m, d, H, M, S)
    return datetime_object
