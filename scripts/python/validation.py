from datetime import datetime
import pandas as pd

def check_if_data_is_valid(data):
    if data.empty:
        raise Exception("No market price for the last 4 days")
        return False

    if data.isnull().values.any():
        raise Exception("Null values in dataframe")
        return False

    timestamps = data["date"]
    for timestamp in timestamps:
        if timestamp >= datetime.now():
            raise Exception("At least one date is not past!")
            return False

    return True
    