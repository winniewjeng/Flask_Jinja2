import logging
import flask
import jinja2
import ORM
import OpenMovie
import sys

"""
Author: Winnie Wei Jeng
Assignment: Lab 8
Professor: Phil Tracton
Date: 11/16/2018

The lab demonstrate the uses of Flask, a micro-web framework,
 and Jinja, a template engine for Python, to provide interfaces 
 for environment and database from PostgreSQLs
"""

# collection of global variables
app = flask.Flask(__name__)
env = jinja2.Environment(
    loader=jinja2.PackageLoader(__name__, '/templates'))
app.secret_key = 'DontCryForMeArgentina'


def ask_for_movie():
    template = env.get_template('ask_movie.html')
    html = template.render()
    return html


# display movie info
def display_movie():
    template = env.get_template('display_movie.html')
    # get the MOVIE from the request form
    request_title = flask.request.form['MOVIE']
    openMovie = OpenMovie.OpenMovie(title=request_title)

    if openMovie is False:
        # log this, get error template, render it, return it
        logging.error("movie title not valid")
        print("movie title not valid")
        template = env.get_template('error.html')
        html = template.render()
        return html

    data = openMovie.getMovieTitleData()
    if data is False:
        # log this, get error template, render it, return it
        logging.error("movie data not in the database")
        print("movie data not in the database")
        template = env.get_template('error.html')
        html = template.render()
        return html

    # Get the display movie.html template, fill it in with the appropriate fields,
    movieTitleQuery = openMovie.getMovieTitleData()
    Director, crew = openMovie.getCrew()
    logging.info("Director:"+Director)
    Lead = openMovie.getCast()[0]['name']
    logging.info("Lead Actor/Actress:" + Lead)
    ReleaseDate = movieTitleQuery.release_date
    logging.info("Release Date:" + ReleaseDate)
    Budget = movieTitleQuery.budget
    logging.info("Budget:" + str(Budget))
    Revenue = movieTitleQuery.revenue
    logging.info("Revenue:" + str(Revenue))
    RunTime = movieTitleQuery.runtime
    logging.info("Run time:" + str(RunTime))

    # render and return it
    html = template.render(movie_title=request_title,
                           Director=Director,
                           Lead=Lead,
                           ReleaseDate=ReleaseDate,
                           Budget=Budget,
                           Revenue=Revenue,
                           RunTime=RunTime)
    return html


# create the front page
@app.route('/', methods=['GET', 'POST'])
def front_page():
    # if the flask request method is POST then return the output from display movie()
    if flask.request.method == 'POST':
        return display_movie()
    # else, return output from ask_for_movie()
    return ask_for_movie()


# program main
if __name__ == "__main__":

    # configure logging
    log_file = 'lab8.log'
    try:
        logging.basicConfig(filename=log_file, level=logging.INFO,
                            format='%(asctime)s,%(levelname)s,%(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
    except:
        print("Failed to open log file %s" % log_file)
        sys.exit(-1)

    logging.info("Program Starting")

    # database checking and table loading
    moviesCSVFile = "../tmdb-5000-movie-dataset/tmdb_5000_movies.csv"
    creditsCSVFile = "../tmdb-5000-movie-dataset/tmdb_5000_credits.csv"

    if not ORM.tableExists(ORM.inspector, "Movies"):
        ORM.csvToTable(moviesCSVFile, tableName="Movies", db=ORM.db)

    if not ORM.tableExists(ORM.inspector, "Credits"):
        ORM.csvToTable(creditsCSVFile, tableName="Credits", db=ORM.db)

    # application entry point
    app.run()
    # commented out alternative for debugging the program
    # use_debugger = True
    # app.run(debug=True)

