import datetime


def nowt() -> str:
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def nowd() -> str:
    return datetime.datetime.now().strftime('%Y-%m-%d')


def add_days(date_str: str,
             date_format: str = '%Y-%m-%d',
             delta: int = 1) -> str:
    d = datetime.datetime.strptime(date_str, date_format)
    return (d + datetime.timedelta(days=delta)).strftime(date_format)
