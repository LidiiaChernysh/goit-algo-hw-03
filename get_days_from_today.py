from datetime import datetime, timedelta, date


def get_days_from_today(date:str) -> int: #  date in format 'РРРР-ММ-ДД'
    today = datetime.today()
   
    try:
        # string to datetime
        parsed_date = datetime.strptime(date, "%Y.%m.%d")

        # calculate day numbers between dates
        difference = today.toordinal() - parsed_date.toordinal()

        return difference
    
    except ValueError:
        return f"Time data {date} does not match format 'YYYY.mm.dd'"

