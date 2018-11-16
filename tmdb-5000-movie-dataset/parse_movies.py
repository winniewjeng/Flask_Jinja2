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



class Movies(base):
    __tablename__ = 'Movies'
    id = sqlalchemy.Column(sqlalchemy.Numeric, primary_key=True)
    budget = sqlalchemy.Column(sqlalchemy.Numeric)
    popularity = sqlalchemy.Column(sqlalchemy.Numeric)
    runtime = sqlalchemy.Column(sqlalchemy.Numeric)
    vote_average = sqlalchemy.Column(sqlalchemy.Numeric)
    vote_count = sqlalchemy.Column(sqlalchemy.Numeric)
    revenue = sqlalchemy.Column(sqlalchemy.Numeric)
    genre = sqlalchemy.Column(sqlalchemy.String)
    homepage = sqlalchemy.Column(sqlalchemy.String)
    title = sqlalchemy.Column(sqlalchemy.String)
    tagline = sqlalchemy.Column(sqlalchemy.String)
    status = sqlalchemy.Column(sqlalchemy.String)
    release_date = sqlalchemy.Column(sqlalchemy.String)


class Credits(base):
    __tablename__ = 'Credits'
    movie_id = sqlalchemy.Column(sqlalchemy.Numeric, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    cast = sqlalchemy.Column(sqlalchemy.String)
    crew = sqlalchemy.Column(sqlalchemy.String)


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


if __name__ == "__main__":

    tableDict = {"MOON": "tmdb_5000_movies.csv", "CREAM": "tmdb_5000_credits.csv"}
    # tableDict = {"google": "src/goog.us.txt", "aapl": "src/aapl.us.txt"}

    for k, v in tableDict.items():
        if not tableExists(inspector, k):
            print("Adding table {}".format(k))
            csvToTable(v, tableName=k, db=db)
        else:
            print("Table {} already exists".format(k))
