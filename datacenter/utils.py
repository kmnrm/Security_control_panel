import datetime

def format_duration(duration):
    duration_in_seconds = duration.total_seconds()
    hours = int(duration_in_seconds // 3600)
    minutes = int((duration_in_seconds % 3600) // 60)
    if hours > 0:
        duration_format = '{}h {}min'.format(hours, minutes)
    else:
        duration_format = '{} min'.format(minutes)
    return duration_format


def chop_microseconds(delta):
    return delta - datetime.timedelta(microseconds=delta.microseconds)
