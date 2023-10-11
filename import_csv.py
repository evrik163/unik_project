from sqlalchemy import create_engine
import pandas as pd
import numpy as np



def start():
    df = pd.read_csv('merged.csv')
    df.columns = [c.lower() for c in df.columns] # PostgreSQL doesn't like capitals or spaces
    engine = create_engine('postgresql://postgres:123@localhost:5432/unik_db')
    df.to_sql("my_table_name", engine)


start()
