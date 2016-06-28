from pytz import timezone


def moscow_tz(date_val):
    moscow_tz = timezone("Europe/Moscow")
    return date_val.astimezone(moscow_tz)
