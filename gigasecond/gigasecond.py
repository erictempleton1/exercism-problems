from datetime import date, timedelta

def add_gigasecond(start_date):
    d = date(start_date).timetuple()
    tdelta_sec = timedelta(days=d[7]).total_seconds()
    
    # convert 1000000000 secs to years, month, and days
    # add to start date

    