import OpenMovie
import configparser
import logging
import sys
import json
import PyQt5.QtWidgets
import UI

"""
File: Jeng_Winnie_Lab6.py
Author: Winnie Wei Jeng
Assignment: Lab 6
Professor: Phil Tracton
Date: 11/3/2018
Description: This simple GUI pulls up movie poster's image upon entering in the movie title

"""
if __name__ == "__main__":
    try:
        config = configparser.RawConfigParser()
        # read in the "movie.cfg" file
        config.read("movies.cfg")
    except:
        print("Config fail")
        logging.error("Config fail")
        sys.exit()

        # if the configuration has a section named ”LOGGING”,
        # read the LOG_FILE field of it and store the name in log_file_name
        # else set log file name to ”default.log”
    if config.has_section('LOGGING'):
        log_file_name = config.get('LOGGING', 'log_file')

    else:
        log_file_name = "default.log"

    # create a logging basiConfig
    logging.basicConfig(filename=log_file_name, level=logging.INFO,
                        format='%(asctime)s,%(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    # create a logging instance using log_file_name
    logging.info(" %s opens. Program starts." % log_file_name)

    try:
        contents = open('movies.json', 'r')
        print(" Opened the JSON file!")
        logging.info(" Opened the JSON file!")

    except:
        print("Failed to open JSON file")
        logging.error("Failed to open JSON file")
        sys.exit()

    # app is a PyQT5 QApplication instance
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    # gui is an instance of UI that takes in the json instance named contents
    gui = UI.UI(moviesJSON=contents)  # 5.(g)
    app.exec_()
    logging.INFO(" GUI ends!")

    """The rest below is not relevant to lab 6"""
    # data is a dictionary loaded from the ”movie_posters” field of json data
    data = json.load(contents)

    """test code to print out the data dictionary of json objects """

    # for each item in this dictionary, create an instance of OpenMovie,
    #  using the key for the title and the value for the posterURL call the getPoster method
    #  of this instance of OpenMovie and then delete this instance of OpenMovie
    for i in data['movie_posters']:
        instance = OpenMovie.OpenMovie(i, data['movie_posters'][i])
        instance.getPoster()
        del instance

    contents.close()


