#! /usr/bin/env python3

import os
import pandas as pd
import sqlalchemy
import sqlalchemy.ext.declarative


user = "postgres"
password = "python"
# password = os.environ['PASSWORD']
host = "localhost"
port = 5432
db = "postgres"
url = 'postgresql://{}:{}@{}:{}/{}'
db_string = url.format(user, password, host, port, db)
db = sqlalchemy.create_engine(db_string)
base = sqlalchemy.ext.declarative.declarative_base()
inspector = sqlalchemy.inspect(db)


class Stock(base):
    __abstract__ = True
    date = sqlalchemy.Column(sqlalchemy.Date, primary_key=True)
    open = sqlalchemy.Column(sqlalchemy.Numeric)
    high = sqlalchemy.Column(sqlalchemy.Numeric)
    low = sqlalchemy.Column(sqlalchemy.Numeric)
    close = sqlalchemy.Column(sqlalchemy.Numeric)
    volume = sqlalchemy.Column(sqlalchemy.Integer)
    openint = sqlalchemy.Column(sqlalchemy.Integer)


class Apple(Stock):
    __tablename__ = "aapl"


class Google(Stock):
    __tablename__ = "goog"


def tableExists(inspector=None, tableName=None):
    """
    Returns true if this table exists in this database
    and false otherwise
    """
    return (tableName in inspector.get_table_names())


def csvToTable(fileName=None, tableName=None, db=None):
    """
    Put a CSV file into the db in this table
    """
    try:
        df_csv = pd.read_csv(fileName)
        df_csv.columns = [c.lower() for c in df_csv.columns]
        df_csv.to_sql(tableName, db)
        return True
    except:
        return False

    return


if __name__ == "__main__":

    tableDict = {"movies": "tmdb_5000_movies.csv", "credits": "tmdb_5000_credits.csv"}
    # tableDict = {"google": "src/goog.us.txt", "aapl": "src/aapl.us.txt"}

    for k, v in tableDict.items():
        if not tableExists(inspector, k):
            print("Adding table {}".format(k))
            csvToTable(v, tableName=k, db=db)
        else:
            print("Table {} already exists".format(k))
