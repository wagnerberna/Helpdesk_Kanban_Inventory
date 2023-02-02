import datetime


def format_time_delta(time_format):
    time_format = time_format - datetime.timedelta(
        microseconds=time_format.microseconds
    )
    total_seconds = time_format.seconds

    days = time_format.days
    print("days", days)
    print("total_seconds", total_seconds)

    total_seconds = total_seconds % (60 * 60 * 24)
    hours = total_seconds // (60 * 60)
    total_seconds = total_seconds % (60 * 60)
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    if days > 0:
        return f"{days} Dias {hours}h {minutes}m {seconds}s"
    else:
        return f"{hours}h {minutes}m {seconds}s"
