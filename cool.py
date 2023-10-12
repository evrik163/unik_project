from sqlalchemy import create_engine
import pandas as pd
import time

engine = create_engine('postgresql://postgres:123@localhost:5432/unik_db')


def to_sql():
    df = pd.read_csv('train.csv')
    df.columns = [c.lower() for c in df.columns]
    df.to_sql("final", engine)


def from_sql():
    df = pd.read_sql_query('select * from "dataset"', con=engine)
    df.to_csv('train.csv')


if __name__ == "__main__":
    to_sql()
    time.sleep(5)
    from_sql()
    print("Датасет загружен в базу данных!")

