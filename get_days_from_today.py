from datetime import datetime, timedelta, date


def get_days_from_today(date:str) -> int: 

    """
    Calculates the number of days between a given date and the current date.

    Parameters:
        date (str): date in 'YYYY-MM-DD' format

    Returns:
        int: number of days from a given date to the current one
    
    Raises:
        ValueError: if data does not match format 'YYYY-mm-dd'
    """
    today = datetime.today()
   
    try:
        # string to datetime
        parsed_date = datetime.strptime(date, "%Y-%m-%d")

        # calculate day numbers between dates
        difference = today.toordinal() - parsed_date.toordinal()

        return difference
    
    except ValueError:
        return f"Time data {date} does not match format 'YYYY-mm-dd'"


print(get_days_from_today('2024-12-25'))

