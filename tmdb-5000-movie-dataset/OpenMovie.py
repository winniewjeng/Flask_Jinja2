#!/usr/bin/env python3

import logging
import os
import re
import sys
import traceback
import urllib.request
import json
import sqlalchemy
import ORM
import parse_movies
import re

"""
File: Jeng_Winnie_Lab6.py
Author: Winnie Wei Jeng
Assignment: Lab 7
Professor: Phil Tracton
Date: 11/8/2018
Description: This simple GUI pulls up movie poster's image upon entering in the movie title

"""


class OpenMovie:
    """
        Author: Winnie Wei Jeng
        Assignment: Week 6
        Professor: Phil Tracton
        Date: 11/3/2018
        OpenMovie class takes in a string title and a string url and return an image
    """

    # constructor:
    def __init__(self, title=None, posterURL=None):
        '''
        constructor
        '''
        self.title = title
        self.posterURL = posterURL
        self.posterFileName = None
        self.path = "Posters"
        if os.path.isdir(self.path):
            pass
        else:
            os.mkdir(self.path)
            logging.info(" Successfully created the directory %s " % self.path)

    def getPoster(self):
        # log the event of calling getPoster() method
        logging.info(" getPoster() method is called")
        logging.info(" Poster's name: %s" % self.title)
        logging.info(" Poster's URL %s" % self.posterURL)

        # substitute every symbol and spaces in title with underline
        re.sub(r"[^a-zA-Z0-9]", "_", self.title)
        self.posterFileName = "Posters/%s.jpg" % self.title
        try:
            urllib.request.urlretrieve(self.posterURL, self.posterFileName)
            return True
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)
            logging.error("*** tb_lineno: {}".format(exc_traceback.tb_lineno))
            return False

    # user enters movie title in GUI, fxn gets the row from the instance's movie title
    def getMovieTitleData(self):
        self.title = "Avatar"  # testing purpose
        # query the ORM session for the ORM Movies
        result = ORM.session.query(ORM.Movies.title).filter(ORM.Movies.title == self.title)

        for x in result:
            # print(x)
            x = re.sub(r'[\W_]+', '', str(x))
            # if query works and ORM Movies title is equal to this class title, return resultx
            if x == self.title:
                result = x
                print(result)
                return result
            else:
                logging.error(" movie title {} is not found in the db".format(self.title))
                return False

    # get the cast information from this movie’s credits table
    def getCast(self):
        # self.title = "Iron Man"
        # try:
        #     moviesCreditsQuery = ORM.session.query(ORM.Credits.title, ORM.Credits.cast).filter(sqlalchemy.or_(ORM.Credits.title == self.title))
        #     # cast = json.loads(moviesCreditsQuery[0])
        #     # print(moviesCreditsQuery[0])
        #     #
        #     # for x in moviesCreditsQuery:
        #     #     print(x)
        #     # return moviesCreditsQuery
        # except:
        #     logging.error(" cannot query the movie from the db")

        # query the ORM session for the ORM Credits table
        # filter it on the ORM Credits title matching this class’s title
        # store the results in movieCreditsQuery
        self.title = "Iron Man"
        moviesCreditsQuery = ORM.session.query(ORM.Credits.title, ORM.Credits.cast)
        for x in moviesCreditsQuery:
            if x[0] == self.title:
                # print(x[1])
                # m = json.dumps(x[1])
                cast_info = json.loads(x[1])
                cast = cast_info[0]['name']
                print(cast)

    # get the crew information from this movie’s Credits table
    def getCrew(self):
        # query the ORM session for this ORM Credits and filter
        # where the ORM Credits title is the movie’s title and
        # store this in movieCreditsQuery

        self.title = "Avatar"  # testing purpose

        moviesCreditsQuery = ORM.session.query(ORM.Credits.title, ORM.Credits.crew)
        for x in moviesCreditsQuery:
            # print(x[1])  # print crew
            if x[0] == self.title:
                try:
                    crew_info = json.loads(x[1])
                    # get the crew
                    crew = crew_info[0]['name']
                    # print(crew)
                    try:
                        # get the director
                        for item in crew_info:
                            # print(item['job'])
                            if item['job'] == 'Director':
                                director = item['name']
                                logging.info(" successfully get crew and director")
                                print(director, crew)
                                return director, crew
                    except:
                        logging.warning(" could not find the director from the db")
                        return False, crew
                except:
                    logging.error(" could not json load the crew".format(self.title))
                    return False, False

            else:
                logging.error(" could not find movie title {} from the db".format(self.title))
                return False, False
        # print("get crew!")
        # # query the ORM session for this ORM Credits and filter
        # # where the ORM Credits title is the movie’s title and
        # # store this in movieCreditsQuery
        # self.title = "Avatar"
        # moviesCreditsQuery = ORM.session.query(ORM.Credits.title, ORM.Credits.crew)
        # for x in moviesCreditsQuery:
        #     # print(x[1])  # print crew
        #     if x[0] == self.title:
        #         crew_info = json.loads(x[1])
        #
        #         # get the crew
        #         crew = crew_info[0]['name']
        #         # print(crew)
        #         try:
        #             # get the director
        #             for item in crew_info:
        #                 # print(item['job'])
        #                 if item['job'] == 'Director':
        #                     director = item['name']
        #         except:
        #             return False, crew
        #         return director, crew
        #
        #     else:
        #         return False, False





        #     print(x)
        # if self.title is moviesCreditsQuery:
        #     logging.info(" movie credits title {} is queried from the db".format(self.title))
        # else:
        #     return False, False
        # try:
        #     crew = json.load(moviesCreditsQuery[0].crew)
        # except:
        #     logging.error(" could not load the crew info from the db".format(self.title))
        #     return False, False
        #
        # try:
        #     for key, value in crew.iteritems():
        #         if "Director" is value:
        #             # return crew[value+1]
        #             return value + 1, crew  # return the director's name and crew
        # except:
        #     logging.error(" cannot query the director's info")
        #     return False, False


if __name__ == "__main__":
    tableDict = {"Movies": "tmdb_5000_movies.csv", "Credits": "tmdb_5000_credits.csv"}

    for k, v in tableDict.items():
        if not parse_movies.tableExists(parse_movies.inspector, k):
            print("Adding table {}".format(k))
            parse_movies.csvToTable(v, tableName=k, db=parse_movies.db)
        else:
            print("Table {} already exists".format(k))

    parse_movies.base.metadata.create_all(parse_movies.db)
    openMovie = OpenMovie()
    print(openMovie.getCast())
