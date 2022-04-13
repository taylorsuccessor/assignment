from datetime import datetime

def seconds_to_humain(seconds: int) -> str:

    """
    Converts 0 <= Seconds <= 86399 to humain hour
    :param seconds: int
    :return: str: 12-hour clock format 0 = 12 AM and 86399 = 11:59 PM
    """
    humain_time: str = datetime.fromtimestamp(seconds).strftime("%I:%M %p")
    return humain_time.lstrip('0').replace(':00', '')

def time_range_humanize(open_hour: int, close_hour: int) -> str:
    """
    concat the humanized open and closed  Hour
    :param open_hour: int
    :param close_hour: int
    :return: str: 1 - 5 PM
    """
    return seconds_to_humain(open_hour) + " - " + seconds_to_humain(close_hour)


def prepare_day_open(day_hours: list[(int, int)]) -> str:
    """
    convert list of open hours to string and connect them by(, )
    :param day_hours: list[(int, int)]
    :return: str: full day opening hours humanized
    """
    return ', '.join([
        time_range_humanize(open, close) for open, close in day_hours
    ]) if len(day_hours) else 'Closed'

def humanize_opening_hours(week_info_dict: dict[str, tuple]) -> str:
    """
    take all the week info and retrun text of opening Hours
    :param week_info_dict: dict[str, tuple]
    :return str: text
    """
    return "\n".join([
        day_name.capitalize() + ": " + prepare_day_open(day_hours)
        for day_name, day_hours in week_info_dict.items()
    ])
