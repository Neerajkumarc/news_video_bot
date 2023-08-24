def getDate(timestamp):
    from datetime import datetime

    ts = timestamp / 1000  # Convert milliseconds to seconds
    date_obj = datetime.utcfromtimestamp(ts)
    formatted_date = date_obj.strftime('%Y-%m-%d %H:%M:%S')

    return formatted_date
