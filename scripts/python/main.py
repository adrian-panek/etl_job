from extract import *
from load import *
from validation import check_if_data_is_valid

import numpy as np
import pandas as pd

print("Creating the dataframe")
timeframe = generate_dataframe()
data = get_data()
dataframe = create_dataframe(data, timeframe)
print("Dataframe created")


dataframe['date'] = pd.to_datetime(dataframe['date'])

print("Validating data in dataframe")
if check_if_data_is_valid(dataframe):
    print("Data is correct")

print("Creating DB engine")
engine = connect_to_db()
print("Created DB engine")

print("Inserting data to database")
insert_data(dataframe, engine)
print("data has been inserted successfully")

