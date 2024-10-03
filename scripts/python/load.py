from sqlalchemy import create_engine
import os

import pandas as pd
import numpy as np

db_pass = os.environ['DB_PASS']

def connect_to_db():
    engine = create_engine(f'postgresql://etl_user:{db_pass}@postgres-db:5432/etl_job')
    return engine

def insert_data(dataframe, engine):
    dataframe.to_sql(name="market_data", con=engine, if_exists="append")