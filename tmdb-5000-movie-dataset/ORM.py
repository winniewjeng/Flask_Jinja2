#! /usr/bin/env python3

import logging
import pandas as pd
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

user = "postgres"
password = "python"
# password = os.environ['PASSWORD']
host = "localhost"
port = 5432
db = "postgres"  # database name
url = 'postgresql://{}:{}@{}:{}/{}'  # postgresql URL template
db_string = url.format(user, password, host, port, db)  # postgresql URL
db = sqlalchemy.create_engine(db_string)  # create a database
base = sqlalchemy.ext.declarative.declarative_base()  # create a base
inspector = sqlalchemy.inspect(db)  # create an inspector
Session = sqlalchemy.orm.sessionmaker(db)
session = Session()


# returns true if a table is already in the database and returns false if not
def tableExists(inspector=None, table=None):
    return table in inspector.get_table_names()


# loads a CSV file into postgresql db table
def csvToTable(fileName=None, tableName=None, db=None):
    try:
        df_csv = pd.read_csv(fileName)
        df_csv.columns = [c.lower() for c in df_csv.columns]
        df_csv.to_sql(tableName, db)  # convert csv file into database table
        logging.INFO(" Successfully turned the CSV file into table on Postgresql database")
        return True
    except:
        logging.ERROR(" Could not turn the CSV file into table on Postgresql database")
        return False


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


if __name__ == "__main__":
    base.metadata.create_all(db)  # 6-(c)-xi

