import datetime

def is_valid_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except:
        return False
    return True
